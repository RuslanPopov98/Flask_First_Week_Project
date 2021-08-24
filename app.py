from flask import Flask, render_template
import data

app = Flask(__name__)


@app.route('/')
def render_main():
    #return "Здесь будет главная"
    return render_template("index.html")


@app.route('/departures/<departure>/')
def render_departures():
    #return "Здесь будет направление"
    return render_template("departure.html")


@app.route('/tours/<id>/')
def render_tours():
    #return "Здесь будет тур"
    return render_template("tour.html")


@app.route('/data/')
def render_data():
    return render_template("data_render.html", tours=data.tours)


@app.route('/data/departures/<departure>/')
def render_data_departure(departure):
    return render_template("data_departures.html", dep=departure, data=data)


@app.route('/data/tours/<id>/')
def render_data_tours(id):
    return render_template("data_tours.html", dic=data.tours[int(id)])


app.run(debug=True)

