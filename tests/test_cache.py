import unittest
from server import create_app, db

class CacheTestCase(unittest.TestCase):
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

    def test_cached_route(self):
        response = self.client.get('/cache/cached-route')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"message": "This is a cached response"})

if __name__ == '__main__':
    unittest.main()