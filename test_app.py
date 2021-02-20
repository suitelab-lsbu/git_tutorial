import unittest
from app import app


class TestApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.tester = app.test_client(cls)

    def test_index(self):
        response = self.tester.get('/')
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_add(self):
        response = self.tester.get('/add/10/10')
        self.assertEqual(response.json['result'], 10 + 10)
        response = self.tester.get('/add/-1/-1')
        self.assertEqual(response.json['result'], -1 + -1)
        response = self.tester.get('/add/-0/-0')
        self.assertEqual(response.json['result'], -0 + -0)
        response = self.tester.get('/add/s/s')
        self.assertEqual(response.json['Value Error'], "Only numbers Please")

    def test_multiply(self):
        response = self.tester.get('/multiply/10/10')
        self.assertEqual(response.json['result'], 10 * 10)
        response = self.tester.get('/multiply/-1/-1')
        self.assertEqual(response.json['result'], -1 * -1)
        response = self.tester.get('/multiply/-0/-0')
        self.assertEqual(response.json['result'], -0 * -0)
        response = self.tester.get('/multiply/s/s')
        self.assertEqual(response.json['Value Error'], "Only numbers Please")

    def test_subtract(self):
        response = self.tester.get('/subtract/10/10')
        self.assertEqual(response.json['result'], 10 - 10)
        response = self.tester.get('/subtract/-1/-1')
        self.assertEqual(response.json['result'], -1 - -1)
        response = self.tester.get('/subtract/-0/-0')
        self.assertEqual(response.json['result'], -0 - -0)
        response = self.tester.get('/subtract/s/s')
        self.assertEqual(response.json['Value Error'], "Only numbers Please")

    def test_divide(self):
        response = self.tester.get('/divide/10/10')
        self.assertEqual(response.json['result'], 10 / 10)
        response = self.tester.get('/divide/-1/-1')
        self.assertEqual(response.json['result'], -1 / -1)
        response = self.tester.get('/divide/-0/-0')
        self.assertEqual(response.json['Value Error'], "Cannot divide by zero")
        response = self.tester.get('/divide/s/s')
        self.assertEqual(response.json['Value Error'], "Only numbers Please")

    def test_modulus(self):
        response = self.tester.get('/mod/10/10')
        self.assertEqual(response.json['result'], 10 % 10)
        response = self.tester.get('/mod/-1/-1')
        self.assertEqual(response.json['result'], -1 % -1)
        response = self.tester.get('/mod/-0/-0')
        self.assertEqual(response.json['Value Error'], "Cannot modulo by zero")
        response = self.tester.get('/mod/s/s')
        self.assertEqual(response.json['Value Error'], "Only numbers Please")


if __name__ == '__main__':
    unittest.main()
