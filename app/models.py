from app import db


# Flask shell
# > from app import db
# > db.create_all()

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.current_timestamp())

    title = db.Column(db.String(128), nullable=False)
    content = db.Column(db.UnicodeText, nullable=False)
    language = db.Column(db.String(16), nullable=False)
    size = db.Column(db.Integer, nullable=False)

    def __init__(self, title, content, language, size):
        self.title = title
        self.content = content
        self.language = language
        self.size = size

    def __repr__(self):
        return f'<Note {self.title}, language: {self.language}, size: {self.size}>'
