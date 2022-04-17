from app import app, hashids
from flask import render_template, request, redirect, url_for, make_response

from .config import Config
from .texts import Texts
from .forms import NewShareForm


@app.route('/', methods=('GET', 'POST'))
def index():

    form = NewShareForm(request.form)

    if form.validate_on_submit():

        # get values from Form
        title = form.title.data
        lang = form.languageSelector.data
        editor = form.editor.data
        no_human = form.nh.data

        # Is this request from a bot?
        if no_human != '':
            return redirect(url_for('index'))

        # are values correct?
        if len(title) >= Config.TITLE_MAX_LEN:
            pass

        if lang not in Config.PROGRAM_LANGUAGES:
            pass

        if len(editor) > Config.EDITOR_MAX_LEN:
            pass

        # save data to the DB and get record ID
        record_id = hashids.encode(101)

        # return page

        response = make_response(f'form.title.data: {title};\n'
                                 f'form.languageSelector.data: {lang};\n'
                                 f'form.editor.data: {editor}', 200)
        response.mimetype = 'text/plain'
        return response

    response = render_template('index.html', title=Texts.TITLE, description=Texts.DESCRIPTION, form=form)
    return response


@app.route('/about')
def about():
    return render_template('about.html', title=Texts.TITLE, description=Texts.DESCRIPTION)


@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('index'))


@app.route('/clone', methods=['GET'])
def clone():
    key = request.args.get('id', '')

    if len(key) <= 0:
        return redirect(url_for('index'))

    # TODO:try get data by ID from DB
    # TODO: if ok then
    return render_template('index.html',
                           title=Texts.TITLE,
                           description=Texts.DESCRIPTION,
                           code_title='Title of the code',
                           code_body='Body of the code',
                           code_style='python'
                           )


@app.route('/<string:key>')
def page(key: str):
    id = hashids.decode(key)

    # try get data from DB by ID
    # if ok then:

    key_type = request.args.get('type', '')

    if key_type == 'row':
        response = make_response(Texts.ABOUT, 200)
        response.mimetype = 'text/plain'
        return response

    if key_type == '':
        response = render_template('page.html',
                                   title=Texts.TITLE,
                                   description='description',
                                   key=key,
                                   created_time='10 minute\'s ago',
                                   code_title='Hi there!',
                                   code_body=Texts.ABOUT,
                                   code_style='text',
                                   code_views=146)
        return response

    return redirect(url_for('index'))
