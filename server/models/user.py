from database import db
from sqlalchemy_serializer import SerializerMixin

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    phone = db.Column(db.String)
    email = db.Column(db.String)
    location = db.Column(db.String)
    title = db.Column(db.String)
    admin = db.Column(db.Boolean, default=False)
    password = db.Column(db.String)
    about = db.Column(db.String)
    image = db.Column(db.String)

    events = db.relationship('Event', secondary = 'user_event_association', back_populates='users')

    def __repr__(self) -> str:
        return f'<User {self.id}, {self.first_name}, {self.last_name}, {self.phone}, {self.email}, {self.location}, {self.title}, {self.image} ,{self.about}, {self.password}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone': self.phone,
            'title': self.title,
            'location': self.location,
            'email': self.email,
            'about': self.about,
            'image': self.image,    
        }