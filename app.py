from flask import Flask, jsonify,request
from common import send_slack_notif
from common import authenticate
from common import require_token
import sentry_sdk
import requests

app = Flask(__name__)

sentry_sdk.init(
    dsn="https://c8e14adcb4626bf7a0e5bcefe295bf8c@o4507265623654400.ingest.de.sentry.io/4507265720189008",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

@app.route('/api/github/<int:pr_id>', methods=['POST'])
@require_token.check_token
def pr_merge(pr_id):
    headers = {
        "Authorization": f"token <token>"
    }
    url = f"https://api.github.com/repos/celiksoner/trial-app/pulls/{pr_id}/merge"

    response = requests.put(url, headers=headers)
    if response.status_code == 200:
        return jsonify({"message": f"PR {pr_id} merge successfully!"}), 200
    else:
        return jsonify({"error": f"PR {pr_id} merge failed. Status code: {response.status_code}"}), 500


@app.route('/api/sentry-test', methods=['GET'])
@require_token.check_token
def throw_exception():
    1/0
    return 'Error log test.'

@app.route('/api/get-token', methods=['POST'])
def get_auth_token():
    auth = request.get_json()
    username = auth.get('username', None)
    password = auth.get('password', None)

    if not username or not password or not authenticate.check_user(username, password):
        return jsonify({'Error': 'Username or password does not match!'}), 401
    
    token = authenticate.check_user(username,password)
    return jsonify({'Token': token}), 200


@app.route('/api/health', methods=['GET'])
def get_health():
    return 'Application is running...', 200

@app.route('/api/slack', methods=['POST'])
@require_token.check_token
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
