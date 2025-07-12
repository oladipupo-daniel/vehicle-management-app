from flask import Flask, render_template, request
import random

app = Flask(__name__)

class Vehicle:
    def __init__(self, name, brand, model, year, color, wheels):
        self.name = name
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.wheels = wheels

    def display_info(self):
        return f"{self.year} {self.color} {self.brand} {self.model} with {self.wheels} wheels"

def get_wheels(vehicle_type):
    # Map vehicle type to number of wheels
    vehicle_wheels = {
        'car': 4,
        'motorcycle': 2,
        'bicycle': 2,
        'bus': 6,
        'truck': 6
    }
    # Default to 4 if not found
    return vehicle_wheels.get(vehicle_type.lower(), 4)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        vehicle_type = request.form['vehicle_type']
        name = request.form['name']
        brand = request.form['brand']
        model = request.form['model']
        year_choice = request.form['year']
        color = request.form['color']
        wheels = get_wheels(vehicle_type)

        if year_choice.lower() == 'yes':
            year = random.randint(2020, 2023)
        else:
            year = random.randint(2000, 2019)

        my_vehicle = Vehicle(name, brand, model, year, color, wheels)
        price = random.randint(15000, 50000)
        return render_template('result.html', vehicle=my_vehicle, price=price)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)