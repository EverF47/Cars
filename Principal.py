from app import db

class CarsModel(db.Model):
    __tablenam__='carros'
    id = db.Column(db.Integer,prymari_key=True)
    name = db.Column(db.String())
    model= db.Column(db.String())
    doors = db.Column(db.Integer())
    def __init__(self,name,model,doors):
        self.name = name
        self.model = model
        self.doors = doors
    def __repr__(self):
        return f"<Car {self.name}>"