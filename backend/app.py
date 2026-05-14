from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "FocusFlow AI is running!"})
from flask import Flask, request, jsonify
from flask_cors import CORS
from classifier import StudyClassifier

app = Flask(__name__)
CORS(app)

# Initialize classifier
classifier = StudyClassifier()

# Timer state
timer_running = False
current_session_id = None

@app.route('/')
def home():
    return jsonify({"message": "FocusFlow AI is running!"})

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

@app.route('/classify', methods=['POST'])
def classify():
    data = request.json
    
    app_name = data.get('app_name', '')
    window_title = data.get('window_title', '')
    url = data.get('url', '')
    tab_title = data.get('tab_title', '')
    
    result = classifier.predict(app_name, window_title, url, tab_title)
    
    return jsonify(result)

@app.route('/timer/start', methods=['POST'])
def start_timer():
    global timer_running
    timer_running = True
    return jsonify({"timer_running": True})

@app.route('/timer/stop', methods=['POST'])
def stop_timer():
    global timer_running
    timer_running = False
    return jsonify({"timer_running": False})

@app.route('/timer/status', methods=['GET'])
def timer_status():
    return jsonify({"timer_running": timer_running})

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
@app.route('/health')
def health():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)