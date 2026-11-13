from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/sensor')
def sensor():
    return render_template('sensor.html')

@socketio.on('sensor_data')
def handle_data(data):
    socketio.emit('update_dashboard', data)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)