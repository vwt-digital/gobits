import os
import unittest

from gobits import Gobits
from unittest.mock import patch
from werkzeug.local import LocalProxy  # noqa: F401

X_GOOGLE_GCP_PROJECT = 'my-test-project'
X_GOOGLE_FUNCTION_NAME = 'my-test-function'
FUNCTION_TRIGGER_TYPE = 'http'
X_GOOGLE_FUNCTION_VERSION = '99'
HTTP_FUNCTION_EXECUTION_ID = '0123456789'
EXECUTION_TYPE = 'cloud_function'
MESSAGE_ID = '1234567890123456'
MESSAGE_PUBLISH_TIME = '2020-12-31T23:59:59.999Z'


class TestGobits(unittest.TestCase):

    @patch('werkzeug.local.LocalProxy')
    def setUp(self, mock_request):

        os.environ['X_GOOGLE_GCP_PROJECT'] = X_GOOGLE_GCP_PROJECT
        os.environ['X_GOOGLE_FUNCTION_NAME'] = X_GOOGLE_FUNCTION_NAME
        os.environ['FUNCTION_TRIGGER_TYPE'] = FUNCTION_TRIGGER_TYPE
        os.environ['X_GOOGLE_FUNCTION_VERSION'] = X_GOOGLE_FUNCTION_VERSION

        self.request = mock_request
        self.request.headers = {'Function-Execution-Id': HTTP_FUNCTION_EXECUTION_ID}
        self.message = {
            'messageId': MESSAGE_ID,
            'publishTime': MESSAGE_PUBLISH_TIME
        }

        self.gobits = Gobits(request=self.request, message=self.message)

    def test_processed(self):
        self.assertEqual(len(self.gobits.processed), 13),

    def test_gcp_project(self):
        self.assertEqual(self.gobits.gcp_project, X_GOOGLE_GCP_PROJECT)

    def test_execution_id(self):
        self.assertEqual(self.gobits.execution_id, HTTP_FUNCTION_EXECUTION_ID)

    def test_execution_type(self):
        self.assertEqual(self.gobits.execution_type, EXECUTION_TYPE)

    def test_execution_trigger_type(self):
        self.assertEqual(self.gobits.execution_trigger_type, FUNCTION_TRIGGER_TYPE)

    def test_function_name(self):
        self.assertEqual(self.gobits.function_name, X_GOOGLE_FUNCTION_NAME)

    def test_function_version(self):
        self.assertEqual(self.gobits.function_version, X_GOOGLE_FUNCTION_VERSION)

    def test_event_id(self):
        self.assertEqual(self.gobits.event_id, None)

    def test_message_id(self):
        self.assertEqual(self.gobits.message_id, MESSAGE_ID)

    def test_message_publish_time(self):
        self.assertEqual(self.gobits.message_publish_time, MESSAGE_PUBLISH_TIME)

    def test_to_json(self):
        bits = self.gobits.to_json()
        self.assertEqual(bits['gcp_project'], X_GOOGLE_GCP_PROJECT)
        self.assertEqual(bits['execution_id'], HTTP_FUNCTION_EXECUTION_ID)
        self.assertEqual(bits['execution_type'], EXECUTION_TYPE)
        self.assertEqual(bits['execution_trigger_type'], FUNCTION_TRIGGER_TYPE)
        self.assertEqual(bits['function_name'], X_GOOGLE_FUNCTION_NAME)
        self.assertEqual(bits['function_version'], X_GOOGLE_FUNCTION_VERSION)
        self.assertEqual(bits['message_id'], MESSAGE_ID)
        self.assertEqual(bits['message_publish_time'], MESSAGE_PUBLISH_TIME)

    def test_to_json_type(self):
        self.assertIsInstance(self.gobits.to_json(), dict)


if __name__ == '__main__':
    unittest.main()
