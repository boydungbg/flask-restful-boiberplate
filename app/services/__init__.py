from database import db

def save_change(data: object):
    db.session.add(data)
    db.session.commit()