# info. 
# 'notes' vaible is deleted 
class Document:
    def __init__(self, id, title, description, classification, file_path, upload_date, status):
        self.id = id
        self.title = title
        self.description = description
        self.classification = classification
        self.file_path = file_path
        self.upload_date = upload_date
        self.status = status
        

    def __str__(self):
        return f"Document(id={self.id}, title={self.title}, classification={self.classification}, status={self.status})"

# Test, 
doc1 = Document(1, "My first document", "Py class with Dr Chris", "Education", "/docs/project_plan.pdf", "2024-10-01", "Available")
print(doc1)
