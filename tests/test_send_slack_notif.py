import unittest
from unittest.mock import patch
from common.send_slack_notif import send_notification

class TestSendSlackNotification(unittest.TestCase):

    def setUp(self):
        self.webhook_url = "https://hooks.slack.com/services/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"
        self.message = "Test message"

    @patch('common.send_slack_notif.requests.post')
    def test_send_slack_notification_check(self, mock_post):
        mock_post.return_value.status_code = 200
        
        result, status_code = send_notification(self.webhook_url, self.message)
        self.assertEqual(status_code, 200)
        self.assertEqual(result, "Message sended.")
        mock_post.assert_called_once_with(self.webhook_url, json={"text": self.message})

    @patch('common.send_slack_notif.requests.post')
    def test_send_slack_notification_failure(self, mock_post):
        mock_post.return_value.status_code = 400
        mock_post.return_value.text = "Bad Request"
        
        result, status_code = send_notification(self.webhook_url, self.message)
        self.assertEqual(status_code, 500)
        self.assertEqual(result, "Failed send message to Slack: Bad Request")
        mock_post.assert_called_once_with(self.webhook_url, json={"text": self.message})

if __name__ == '__main__':
    unittest.main()