from flask import Flask
from ommongo import fields
from ommongo.session import Session

from flask.ext.ommongo import BaseQuery, ImproperlyConfiguredError, OmMongo
from . import BaseTestCase


class OmMongoObjectTestCase(BaseTestCase):
    "OmMongo itself object tests"

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['OMMONGO_DATABASE'] = 'testing'
        self.app.config['TESTING'] = True

    def tearDown(self):
        del(self.app)

    def test_should_provide_a_Document_class_to_be_extended_inside_the_OmMongo_object(self):
        db = OmMongo()
        assert db.Document is not None

    def test_should_provide_a_query_object_for_queries_on_a_document(self):
        db = OmMongo(self.app)

        class Todo(db.Document):
            description = db.StringField()

        self.assertIsInstance(Todo.query, BaseQuery)

    def test_should_provide_a_session_object_on_mongoalchemy_instance(self):
        db = OmMongo(self.app)
        self.assertIsInstance(db.session, Session)

    def test_should_be_possible_to_create_a_customized_query_class(self):
        db = OmMongo(self.app)

        class Query(BaseQuery):
            pass

        class Todo(db.Document):
            description = db.StringField()
            query_class = Query

        self.assertIsInstance(Todo.query, Query)

    def test_invalid_query_is_none(self):
        db = OmMongo()

        class Query(object):
            pass

        class Todo(db.Document):
            description = db.StringField()
            query_class = Query

        assert Todo.query is None

    def test_should_include_all_mongo_alchemy_fields_objects(self):
        db = OmMongo()
        for key in dir(fields):
            assert hasattr(db, key), "should have the %s attribute" % key
        assert hasattr(db, 'DocumentField'), "should have the DocumentField attribute"

    def test_should_be_able_to_instantiate_passing_the_app(self):
        db = OmMongo(self.app)
        assert db.session is not None

    def test_should_be_able_to_instantiate_without_passing_the_app_and_set_it_later(self):
        db = OmMongo()
        assert db.session is None
        db.init_app(self.app)
        assert db.session is not None

    def test_should_contain_a_not_none_query(self):
        "Document.query should never be None"
        db = OmMongo()
        db.init_app(self.app)

        class Person(db.Document):
            name = db.StringField()

        p = Person()
        assert p.query is not None

    def test_should_not_be_able_to_work_without_providing_a_database_name(self):
        with self.assertRaises(ImproperlyConfiguredError):
            app = Flask(__name__)
            OmMongo(app)

    def test_loads_without_database_connection_data(self):
        app = Flask(__name__)
        app.config['OMMONGO_DATABASE'] = 'my_database'
        OmMongo(app)
        self.assertEqual(app.config['OMMONGO_SERVER'], 'localhost')
        self.assertEqual(app.config['OMMONGO_PORT'], '27017')
        self.assertEqual(app.config['OMMONGO_USER'], None)
        self.assertEqual(app.config['OMMONGO_PASSWORD'], None)
        self.assertEqual(app.config['OMMONGO_REPLICA_SET'], '')

    def test_should_be_able_to_create_two_decoupled_mongoalchemy_instances(self):
        app = Flask(__name__)
        app.config['OMMONGO_DATABASE'] = 'my_database'
        db1 = OmMongo(app)
        db2 = OmMongo(app)
        assert db1.Document is not db2.Document, "two documents should not be the same object"
