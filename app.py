import flask
import grovepi

app = flask.Flask('sensor_api')

@app.route('/V1/enviroment')
def enviroment_handler():
    (temperature, humidity) = grovepi.dht(8, 0)
    return flask.jsonify(temperature=temperature, humidity=humidity)

if __name__ == '__main__':
    app.run()
