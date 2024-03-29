from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:Ew5uz186@localhost:5432/Carsm"
db=SQLAlchemy(app)
migrate=Migrate(app,db)

class CarsModel(db.Model):
    __tablename__='cars'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String())
    model=db.Column(db.String())
    doors=db.Column(db.Integer())

    def __init__(self,name,model,doors):
        self.nasme=name
        self.model=model
        self.doors=doors
    
    def __repr__(self):
        return f"<Car{self.name}>"
    