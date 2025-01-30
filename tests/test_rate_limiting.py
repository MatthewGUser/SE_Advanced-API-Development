import unittest
from server import create_app, db

class RateLimitingTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('TestingConfig')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_rate_limited_route(self):
        for _ in range(5):
            response = self.client.get('/rate_limit/limited-route')
            self.assertEqual(response.status_code, 200)
        response = self.client.get('/rate_limit/limited-route')
        self.assertEqual(response.status_code, 429)

if __name__ == '__main__':
    unittest.main()