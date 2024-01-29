from flask import Flask, jsonify, request
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def handle_requests():
    if request.method == 'POST':
        # Handle POST request to trigger CPU stress
        start_cpu_stress()
        return jsonify({'message': 'CPU stress started successfully'})

    elif request.method == 'GET':
        # Handle GET request to return private IP address
        private_ip = get_private_ip()
        return jsonify({'private_ip': private_ip})

def start_cpu_stress():
    try:
        # Use subprocess.Popen() to run stress_cpu.py in a separate process
        subprocess.Popen(['python', 'stress_cpu.py'])
    except Exception as e:
        return jsonify({'error': f'Failed to start CPU stress: {str(e)}'})

def get_private_ip():
    try:
        # Use socket.gethostbyname() to get the private IP address
        private_ip = socket.gethostbyname(socket.gethostname())
        return private_ip
    except Exception as e:
        return jsonify({'error': f'Failed to get private IP address: {str(e)}'})

if __name__ == '__main__':
    # Run the app on port 80
    app.run(debug=True, host='0.0.0.0', port=8080)

