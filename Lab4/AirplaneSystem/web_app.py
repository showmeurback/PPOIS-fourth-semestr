from flask import Flask, render_template, request, redirect, url_for
from Source.airplane import Airplane
from Source.runway import Runway
from Source.passenger import Passenger
from Source.ticket import Ticket
from Source.crew import Crew
from Source.inflight_service import InflightService
from Source.flight_operations import FlightOperations

app = Flask(__name__, template_folder='templates')
airplanes = [Airplane("Boeing 737", 200)]
runways = [Runway()]

@app.route('/')
def index():
    return render_template('index.html', airplanes=airplanes, runways=runways)

@app.route('/airplanes/<int:id>')
def airplane_details(id):
    if id < len(airplanes):
        return render_template('airplane_details.html', airplane=airplanes[id], id=id)
    return "Airplane not found", 404

@app.route('/airplanes/add', methods=['GET', 'POST'])
def add_airplane():
    if request.method == 'POST':
        model = request.form['model']
        capacity = int(request.form['capacity'])
        airplanes.append(Airplane(model, capacity))
        return redirect(url_for('index'))
    return render_template('add_airplane.html')

@app.route('/airplanes/<int:id>/add_passenger', methods=['POST'])
def add_passenger(id):
    if id < len(airplanes):
        name = request.form['name']
        flight_number = request.form['flight_number']
        seat = request.form['seat']
        ticket = Ticket(flight_number, seat)
        passenger = Passenger(name, ticket)
        airplanes[id].add_passenger(passenger)
        return redirect(url_for('airplane_details', id=id))
    return "Airplane not found", 404

@app.route('/airplanes/<int:id>/add_crew', methods=['POST'])
def add_crew(id):
    if id < len(airplanes):
        name = request.form['name']
        role = request.form['role']
        crew_member = Crew(name, role)
        airplanes[id].add_crew(crew_member)
        return redirect(url_for('airplane_details', id=id))
    return "Airplane not found", 404

@app.route('/airplanes/<int:id>/take_off', methods=['POST'])
def take_off(id):
    if id < len(airplanes):
        airplanes[id].take_off()
        return redirect(url_for('airplane_details', id=id))
    return "Airplane not found", 404

@app.route('/airplanes/<int:id>/land', methods=['POST'])
def land(id):
    if id < len(airplanes):
        airplanes[id].land()
        return redirect(url_for('airplane_details', id=id))
    return "Airplane not found", 404

@app.route('/inflight/serve_meal', methods=['POST'])
def serve_meal():
    InflightService.serve_meal()
    return redirect(url_for('index'))

@app.route('/inflight/serve_drinks', methods=['POST'])
def serve_drinks():
    InflightService.serve_drinks()
    return redirect(url_for('index'))

@app.route('/flight_operations/plan_route', methods=['POST'])
def plan_route():
    start = request.form['start']
    destination = request.form['destination']
    FlightOperations.plan_route(start, destination)
    return redirect(url_for('index'))

@app.route('/runways/<int:id>/occupy', methods=['POST'])
def occupy_runway(id):
    if id < len(runways):
        runways[id].occupy()
        return redirect(url_for('index'))
    return "Runway not found", 404

@app.route('/runways/<int:id>/free', methods=['POST'])
def free_runway(id):
    if id < len(runways):
        runways[id].free()
        return redirect(url_for('index'))
    return "Runway not found", 404

@app.route('/airplanes/<int:id>/save_state', methods=['POST'])
def save_state(id):
    if id < len(airplanes):
        filename = request.form['filename']
        airplanes[id].save_state(filename)
        return redirect(url_for('airplane_details', id=id))
    return "Airplane not found", 404

@app.route('/airplanes/load_state', methods=['POST'])
def load_state():
    filename = request.form['filename']
    airplane = Airplane.load_state(filename)
    if airplane:
        airplanes.append(airplane)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)