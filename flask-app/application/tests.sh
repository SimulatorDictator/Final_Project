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
        self.assertIn(b"TestName1", response.data)

# These are tests for the CREATE functionality.
class TestViews(TestBase):
    def test_gameadd_get(self):
        response = self.client.get(url_for('gameadd'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"TestGame1", response.data)

class TestViews(TestBase):
    def test_gameadd_post(self):
        response = self.client.post(url_for('gameadd'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"TestGame1", response.data)

class TestViews(TestBase):
    def test_add_get(self):
        response = self.client.get(url_for('add'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"TestName1", response.data)

class TestViews(TestBase):
    def test_add_post(self):
        response = self.client.post(url_for('add'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"TestName1", response.data)

# These are tests for the UPDATE functionality.
class TestViews(TestBase):
    def test_updategame_get(self):
        response = self.client.get(url_for('updategame'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"TestName1", 1, response.data)

# class TestViews(TestBase):
    def test_updategame_post(self):
        response = self.client.post(url_for('updategame'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"TestName1", 1, response.data)

# class TestViews(TestBase):
    def test_update_get(self):
        response = self.client.get(url_for('update'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"TestName1", 1, response.data)

# class TestViews(TestBase):
    def test_update_post(self):
        response = self.client.post(url_for('update'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"TestName1", 1, response.data)

# These are tests for the DELETE functionality.
class TestViews(TestBase):
    def test_removegame_post(self):
        response = self.client.get(url_for('removegame'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"TestGame1", 1, response.data)

# class TestViews(TestBase):
    def test_delete_post(self):
        response = self.client.post(url_for('delete'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"TestName1", 1, response.data)
