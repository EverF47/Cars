from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Ew5uz186@localhost:5432/Carsm"
CORS(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from CarsModel import CarsModel
from app import db


class CarsModel(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    model = db.Column(db.String())
    doors = db.Column(db.Integer())

    def __init__(self, name, model, doors):
        self.name = name
        self.model = model
        self.doors = doors

    def __repr__(self):
        return f"<Car {self.name}>"

@app.route('/')
def saludo():
    return 'Hola'

@app.route('/cars', methods=["GET"])
def handle_car():
    cars = CarsModel.query.all()
    results = [
        {
            "name": car.name,
            "model": car.model,
            "doors": car.doors
        }
        for car in cars
    ]
    return {"count": len(results), "cars": results}

@app.route('/cars', methods=["POST"])
def post_car():
    if request.is_json:
        data = request.get_json()
        print(data)
        new_car = CarsModel(name=data['name'], model=data['model'], doors=data['doors'])
        db.session.add(new_car)
        db.session.commit()
        return {"message": "New car created"}
    else:
        return {"message_error": "Error"}

@app.route('/cars', methods=["PUT"])
def put_car():
    if request.is_json:
        data = request.get_json()
        car_id = data.get('id')
        car = CarsModel.query.get(car_id)
        if car:
            car.name = data.get('name', car.name)
            car.model = data.get('model', car.model)
            car.doors = data.get('doors', car.doors)
            db.session.commit()
            return {"message": f"Car with id {car_id} updated"}
        else:
            return {"message": f"Car with id {car_id} not found"}
    else:
        return {"message_error": "Error"}

@app.route('/cars/<int:car_id>', methods=["DELETE"])
def delete_car(car_id):
    car = CarsModel.query.get(car_id)
    if car:
        db.session.delete(car)
        db.session.commit()
        return {"message": f"Car with id {car_id} deleted"}
    else:
        return {"message": f"Car with id {car_id} not found"}
