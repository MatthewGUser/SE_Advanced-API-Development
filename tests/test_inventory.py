import unittest
from server import create_app, db
from server.models.inventory import Inventory

class InventoryTestCase(unittest.TestCase):
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

    def test_create_inventory(self):
        response = self.client.post('/inventory', json={
            'name': 'Part A',
            'price': 10.0
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.get_json())

    def test_get_inventory(self):
        part = Inventory(name='Part A', price=10.0)
        db.session.add(part)
        db.session.commit()
        response = self.client.get(f'/inventory/{part.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['name'], 'Part A')

if __name__ == '__main__':
    unittest.main()