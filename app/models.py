from app import db


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.current_timestamp())
    title = db.Column(db.String(128), nullable=False)
    content = db.Column(db.UnicodeText, nullable=False)
    attributes = db.Column(db.JSON, nullable=False)

    def __init__(self, title, content, attributes):
        self.title = title
        self.content = content
        self.attributes = attributes

    def __repr__(self):
        return f'<Note {self.title}, attr: {self.attributes}>'
