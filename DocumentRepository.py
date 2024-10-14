import csv
import os
from fileUploader import FileUploader


class DocumentRepository:
    def __init__(self):
        self.documents = []

    def add_document(self, document):
        self.documents.append(document)

    def remove_document(self, document_id):
        # Update the documents list by excluding the document with the given id
        self.documents = [doc for doc in self.documents if doc.id != document_id]

    def search_documents(self, keyword):
        keyword_lower = keyword.lower()
        # Return documents where the keyword is found in any of the specified fields
        return [
            doc for doc in self.documents
            if keyword_lower in doc.title.lower()
            or keyword_lower in doc.description.lower()
            or keyword_lower in str(doc.id).lower()
            or keyword_lower in doc.classification.lower()
            or keyword_lower in str(doc.upload_date).lower()
        ]

    def get_document_by_id(self, document_id):
        # Return the document with the given id, if it exists
        for doc in self.documents:
            if doc.id == document_id:
                return doc
        return None

    def add_document_interactive(self):
        # Prompt the user to enter document details
        print("Enter the details of the new document:")
        doc_id = input("ID: ")
        title = input("Title: ")
        description = input("Description: ")
        classification = input("Classification: ")
        file_path = input("File Path: ")
        upload_date = input("Upload Date: ")
        status = input("Status: ")

        # Create a new document dictionary
        document = {
            'id': doc_id,
            'title': title,
            'description': description,
            'classification': classification,
            'file_path': file_path,
            'upload_date': upload_date,
            'status': status
        }

        # Add the document to the repository
        self.add_document(document)

        # Ensure the data folder exists
        os.makedirs('data', exist_ok=True)

        # Write the document details to document.csv
        with open('data/document.csv', mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=document.keys())
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(document)

        # Create a new folder named after the file
        new_folder = os.path.join('data', os.path.splitext(os.path.basename(file_path))[0])
        os.makedirs(new_folder, exist_ok=True)

        print("Document added successfully.")
        upload_choice = input("Do you want to upload a copy of the document in PDF format? (Yes/No): ")
        if upload_choice.lower() == 'yes':
            uploader = FileUploader()
            uploader.upload_document()
            uploader.save_document_to_storage()
        else:
            print("Returning to main.py")


# Test- example usage
if __name__ == "__main__":
    repo = DocumentRepository()
    repo.add_document_interactive()
