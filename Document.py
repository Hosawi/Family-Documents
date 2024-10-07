# info. 
# 'notes' member varible is deleted 
class Document:
    def __init__(self, id, title, description, classification, file_path, upload_date, status):
        self.id = id
        self.title = title
        self.description = description
        self.classification = classification
        self.file_path = file_path   #I'm thinking to delet this mem. var. and follwo the idea of Dr. Chris (Make a floder for E/file+ DB)
        self.upload_date = upload_date
        self.status = status
        
# Temp codes:
# Test, 
    def __str__(self):
        return f"Document(id={self.id}, title={self.title}, classification={self.classification}, status={self.status})"

#Obje1
doc1 = Document(1, "My first document", "Py class with Dr. Chris", "Education", "/docs/project_plan.pdf", "2024-10-01", "Available")
print(doc1)
