import unittest
from server import create_app, db
from server.models.customer import Customer

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('TestingConfig')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.create_test_user()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def create_test_user(self):
        user = Customer(email='test@example.com', password='password')
        db.session.add(user)
        db.session.commit()

    def test_login(self):
        response = self.client.post('/auth/login', json={
            'email': 'test@example.com',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.get_json())

if __name__ == '__main__':
    unittest.main()