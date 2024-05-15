from flask import Flask, jsonify,request
from common import send_slack_notif

app = Flask(__name__)

@app.route('/api/health', methods=['GET'])
def get_health():
    return 'Application is running..', 200

@app.route('/api/slack', methods=['POST'])
def post_slack_notif():
    req_data = request.get_json()
    if 'webhook_url' not in req_data or 'message' not in req_data:
        return jsonify({'error': 'Missing parameters: webhook_url and message required.'}), 400
    webhook_url = req_data['webhook_url']
    message = req_data['message']

    result, status_code = send_slack_notif.send_notification(webhook_url, message)
    return jsonify({'message': result}), status_code


if __name__ == "__main__":
    app.run(debug=True)