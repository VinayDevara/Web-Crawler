# app.py

from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import psutil
import threading
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Function to log system usage and emit to socket
def log_system_usage():
    while True:
        cpu_percent = psutil.cpu_percent(interval=1)
        memory_percent = psutil.virtual_memory().percent
        socketio.emit('system_usage', {'cpu': cpu_percent, 'memory': memory_percent})
        time.sleep(1)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    monitoring_thread = threading.Thread(target=log_system_usage)
    monitoring_thread.daemon = True
    monitoring_thread.start()
    socketio.run(app, debug=True)
