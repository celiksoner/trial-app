from flask import Flask
app = Flask(__name__)

@app.route('/api/health', methods=['GET'])
def get_health():
    return 'application is running', 200