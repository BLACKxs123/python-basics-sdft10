from main import db

class Member(db.Model):
    __tablename__ = 'members'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(256), nullable=False)
    member_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Member {self.id}"