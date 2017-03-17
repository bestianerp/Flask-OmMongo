from ommongo import document

def make_document_class(session, document_class):
    class_dict = document_class.__dict__.copy()
    class_dict.update({'_session': session})
    return type("Document", (document.Document,), class_dict)
