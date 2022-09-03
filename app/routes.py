from app import app, hashids, db
from flask import render_template, request, redirect, url_for, make_response

from .config import Config
from .texts import Texts
from .forms import NewShareForm
from .models import Note


@app.route('/', methods=('GET', 'POST'))
def index():
    form = NewShareForm(request.form)

    if not form.validate_on_submit():
        meta = {
            'title': Texts.TITLE,
            'description': Texts.DESCRIPTION
        }
        attr = {
            'total_notes': db.session.query(Note).count()
        }

        return render_template('index.html', form=form, attr=attr, meta=meta)

    # Firstly check for humans
    no_human = form.nh.data
    if no_human != '':
        return redirect(url_for('index'))

    # Get submitted data
    title = form.title.data
    content = form.editor.data
    language = form.languageSelector.data
    is_public = True if form.privacySelector.data == 'public' else False

    # Check submitted values for success conditions
    if len(title) > Config.TITLE_MAX_LENGTH or \
       language not in Config.PROGRAM_LANGUAGES or \
       len(content) > Config.EDITOR_MAX_LENGTH:

        return redirect(url_for('index'))

    # Save new note to the DB
    note = Note(title, content, language, len(content), is_public)
    db.session.add(note)
    db.session.flush()
    key = hashids.encode(note.id)
    db.session.commit()

    return redirect(url_for('page', key=key))


@app.route('/about')
def about():
    attr = {
        'total_notes': db.session.query(Note).count()
    }
    meta = {
        'title': Texts.TITLE,
        'description': Texts.DESCRIPTION
    }

    return render_template('about.html', attr=attr, meta=meta)


@app.route('/ext')
def ext():
    attr = {
        'total_notes': db.session.query(Note).count()
    }
    meta = {
        'title': Texts.TITLE,
        'description': Texts.DESCRIPTION
    }

    return render_template('ext.html', attr=attr, meta=meta)


@app.route('/history')
def history():

    # Get last notes from DB
    columns = [Note.id, Note.created_at, Note.title, Note.language]
    response = db.session.query(Note) \
        .with_entities(*columns) \
        .filter(Note.privacy.is_(True)) \
        .order_by(Note.created_at.desc()).limit(Config.HISTORY_NOTES_LIMIT).all()

    # Convert to human format
    title_length_limit = Config.HISTORY_NOTES_TITLE_LIMIT
    last_notes = [{'id': hashids.encode(id),
                   'created_at': created_at.strftime(Config.GENERAL_DATE_FORMAT),
                   'title': title if len(title) <= title_length_limit else f'{title[:title_length_limit]}...',
                   'language': language
                   } for (id, created_at, title, language) in response]

    attr = {
        'total_notes': db.session.query(Note).count(),
        'last_notes': last_notes
    }
    meta = {
        'title': Texts.TITLE,
        'description': Texts.DESCRIPTION
    }

    return render_template('history.html', attr=attr, meta=meta)


@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('index'))


@app.route('/clone', methods=['GET'])
def clone():
    key = request.args.get('key', '')

    try:
        note_id = hashids.decode(key)
        note = db.session.query(Note).get(note_id)

    except Exception as e:
        return redirect(url_for('index'))

    return render_template('index.html',
                           title=Texts.TITLE,
                           description=Texts.DESCRIPTION,
                           code_title='Title of the code',
                           code_body='Body of the code',
                           code_style='python'
                           )


@app.route('/<string:key>')
def page(key: str):
    try:
        note_id = hashids.decode(key)
        note = db.session.query(Note).get(note_id)

    except Exception as e:
        return redirect(url_for('index'))

    if note is None:
        return redirect(url_for('index'))

    key_type = request.args.get('type', 'json')

    if key_type == 'row':
        response = make_response(note.content, 200)
        response.mimetype = 'text/plain'
        return response

    if key_type == 'json':
        title = note.title
        content = note.content
        language = note.language

        size = note.size
        s_size = f'{size} B' if size < 100 else f'{(size/1000):.2f} KB'

        created_at = note.created_at
        s_create_at = created_at.strftime(Config.GENERAL_DATE_FORMAT)

        attr = {
            'key': key,
            'created_at': s_create_at,
            'total_notes': db.session.query(Note).count(),
            'size': s_size
        }

        meta = {
            'title': Texts.TITLE,
            'description': Texts.DESCRIPTION
        }

        return render_template('page.html', title=title, content=content, language=language, attr=attr, meta=meta)

    return redirect(url_for('index'))
