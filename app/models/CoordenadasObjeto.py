from app import db

class coordenadas(db.Model):
    __tablename__ = "coordenadas"

    cod = db.Column(db.Integer, primary_key=True, autoincrement=True)
    latitude = db.Column(db.Integer)
    longitude = db.Column(db.Integer)

    def __init__(self, cod, latitude, longitude):
        self.cod = cod
        self.latitude = latitude
        self.longitude = longitude
