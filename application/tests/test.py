from flask import url_for 
from flask_testing import TestCase
from application import app, db
from application.models import Games, Customers

# This creates the test base class.
class TestBase(TestCase):
    def create_app(self):
        # Adding the testing configurations.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    #This will be called before every test. It is creating a database with a test game and a test customer.
    def setUp(self):
        db.create_all()
        game1 = Games(name="TestGame1")
        customer1 = Customers(name="TestName1", table="1", fk_gid="1")
        db.session.add(game1)
        db.session.add(customer1)
        db.session.commit()

    # This will be called after every test to close the database session and remove its contents.
    def tearDown(self):
        db.session.remove()
        db.drop_all()

# This is a test class for READ functionality.
class TestViews(TestBase):
    def test_index_get(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"TestGame1", response.data)
        self.assertIn(b"TestName1", 1, 1, response.data)

# This is a test class for the CREATE functionality.
class TestViews(TestBase):
    def test_addgame_get(self):
        response = self.client.get(url_for('addgame'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"TestGame1", response.data)

class TestViews(TestBase):
    def test_addgame_post(self):
        response = self.client.post(url_for('addgame'), data=dict(name="TestGame1"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"TestGame1", response.data)

class TestViews(TestBase):
    def test_reservegame_get(self):
        response = self.client.get(url_for('reservegame'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"TestName1", 1, 1, response.data)

class TestViews(TestBase):
    def test_reservegame_post(self):
        response = self.client.post(url_for('reservegame'), data=dict(name="TestName1"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"TestName1", response.data)