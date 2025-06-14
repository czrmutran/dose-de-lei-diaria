# -*- coding: utf-8 -*-
from src.models.user import db # Import db from a central place if possible

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    laws = db.relationship("Law", backref="subject", lazy=True)

    def __repr__(self):
        return f"<Subject {self.name}>"

class Law(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    content = db.Column(db.Text, nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey("subject.id"), nullable=True) # Allow nullable initially for existing laws

    def __repr__(self):
        return f"<Law {self.title}>"

