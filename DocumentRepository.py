# Info .. 
class DocumentRepository:
    def __init__(self):
        self.documents = []

    def add_document(self, document):
        self.documents.append(document)

##Defining `remove_document` method that updates the `documents` attribute of the class instance by creating a new list of documents. The new list includes only those documents whose `id` is not  equal to `document_id`.
    def remove_document(self, document_id):
        self.documents = [doc for doc in self.documents if doc.id != document_id]

# Defining a search method that searches through the documents list of the class instance and returns a list of documents where the keyword is found(id, classification, Upload date, title, and description, ).

 #   def search_documents(self, keyword):
 #       return [doc for doc in self.documents if keyword.lower() in doc.title.lower() or keyword.lower() in doc.description.lower()]
#   -------     
def search_documents(self, keyword):
    keyword_lower = keyword.lower()
    return [
        doc for doc in self.documents
        if keyword_lower in doc.title.lower()
        or keyword_lower in doc.description.lower()
        or keyword_lower in str(doc.id).lower()
        or keyword_lower in doc.classification.lower()
        or keyword_lower in str(doc.upload_date).lower()
    ]

#------
def get_document_by_id(self, document_id):
        for doc in self.documents:
            if doc.id == document_id:
                return doc
        return None

# --------- local test:
doc1 = Document(1, "Project Plan", "Detailed project plan", "Confidential", "/docs/project_plan.pdf", "2024-10-05", "Draft", "Initial draft")
doc2 = Document(2, "Budget Report", "Annual budget report", "Public", "/docs/budget_report.pdf", "2024-09-30", "Final", "Approved by finance")

repo = DocumentRepository()
repo.add_document(doc1)
repo.add_document(doc2)

print(repo.get_document_by_id(1))
print(repo.search_documents("budget"))
repo.remove_document(1)
print(repo.get_document_by_id(1))