import unittest
from server import create_app, db
from server.models.customer import Customer

class QueriesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('TestingConfig')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.create_test_customers()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def create_test_customers(self):
        for i in range(10):
            customer = Customer(email=f'test{i}@example.com', password='password')
            db.session.add(customer)
        db.session.commit()

    def test_get_customers_with_pagination(self):
        response = self.client.get('/queries/customers?page=1&per_page=5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 5)

if __name__ == '__main__':
    unittest.main()