from __future__ import absolute_import

from ommongo import document

from flask.ext.ommongo import Document
from flask.ext.ommongo.meta import make_document_class
from tests import BaseAppTestCase


class MetaTestCase(BaseAppTestCase):
    "meta.py test case"

    def test_should_be_able_to_create_a_new_document(self):
        MyDocument = make_document_class(self.db, Document)
        assert issubclass(MyDocument, document.Document)
