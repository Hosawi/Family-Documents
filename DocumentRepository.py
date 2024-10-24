import csv
from datetime import datetime
from pathlib import Path
from Document import Document

class DocumentRepository:
    def __init__(self, csv_file='data/document.csv'):
        """
        Initialize the DocumentRepository with a CSV file path.
        """
        self.documents = []
        self.csv_file = Path(csv_file)
        self.load_documents()

    def load_documents(self):
        """
        Load documents from the CSV file into memory.
        """
        if self.csv_file.exists():
            with self.csv_file.open('r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self._add_document_from_row(row)

    def _add_document_from_row(self, row):
        """
        Create a Document object from a CSV row and add it to the documents list.
        """
        cleaned_row = {k: v for k, v in row.items() if k and k != 'None'}
        try:
            self.documents.append(Document(**cleaned_row))
        except TypeError as e:
            print(f"Error loading document: {e}")
            print(f"Problematic row: {cleaned_row}")
            print("Skipping this document and continuing...")

    def save_documents(self):
        """
        Save all documents to the CSV file.
        """
        self.csv_file.parent.mkdir(parents=True, exist_ok=True)
        with self.csv_file.open('w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=Document.get_fields())
            writer.writeheader()
            for doc in self.documents:
                writer.writerow(doc.to_dict())

    def add_document(self, document):
        """
        Add a new document to the repository and save it.
        """
        self.documents.append(document)
        self.save_documents()
        self.create_document_txt_file(document)

    def create_document_txt_file(self, document):
        """
        Create a text file containing the document's details.
        """
        txt_file_path = self._generate_txt_file_path(document.title)
        txt_file_path.parent.mkdir(parents=True, exist_ok=True)
        with txt_file_path.open('w') as file:
            for field, value in document.to_dict().items():
                file.write(f"{field.capitalize()}: {value}\n")

    def _generate_txt_file_path(self, title):
        """
        Generate a file path for the document's text file.
        """
        return Path('data/documents') / f"{title.replace(' ', '_').lower()}.txt"

    def list_documents(self):
        """
        Print a list of all documents in the repository.
        """
        print("\nCurrent Documents:")
        for doc in self.documents:
            print(f"ID: {doc.id}, Title: {doc.title}")

    def remove_document(self):
        """
        Remove a document from the repository based on user input.
        """
        self.list_documents()
        doc_id = input("Enter the ID of the document to delete (or 'cancel' to abort): ")
        
        if doc_id.lower() == 'cancel':
            print("Deletion cancelled.")
            return

        document = self.get_document_by_id(doc_id)
        if document:
            if self._confirm_deletion(document):
                self._delete_document_files(document)
                self._remove_document_from_list(doc_id)
                self.save_documents()
                print("\nUpdated list of documents:")
                self.list_documents()
        else:
            print(f"No document found with ID {doc_id}.")

    def _confirm_deletion(self, document):
        """
        Ask for user confirmation before deleting a document.
        """
        confirm = input(f"Are you sure you want to delete '{document.title}'? (yes/no): ")
        return confirm.lower() == 'yes'

    def _delete_document_files(self, document):
        """
        Delete the text and PDF files associated with a document.
        """
        deleted_files = []
        txt_file_path = self._generate_txt_file_path(document.title)
        pdf_file_path = Path(document.file_path)

        for file_path in [txt_file_path, pdf_file_path]:
            if file_path.exists():
                file_path.unlink()
                deleted_files.append(str(file_path))

        print(f"\nDocument '{document.title}' has been deleted.")
        print("The following files have been removed:")
        for file in deleted_files:
            print(f"- {file}")

    def _remove_document_from_list(self, doc_id):
        """
        Remove a document from the documents list based on its ID.
        """
        self.documents = [doc for doc in self.documents if doc.id != doc_id]

    def search_documents(self, keyword):
        """
        Search for documents containing the given keyword.
        """
        keyword = keyword.lower()
        results = self._basic_search(keyword)

        if results:
            print(f"\nFound {len(results)} document(s):")
            for doc in results:
                print(f"ID: {doc.id}, Title: {doc.title}, Classification: {doc.classification}")
        else:
            print("No documents found matching the keyword.")
        
        return results

    def _basic_search(self, keyword):
        """
        Perform a basic search on all document fields.
        """
        return [
            doc for doc in self.documents
            if any(keyword in str(value).lower() for value in doc.to_dict().values())
        ]

    def get_document_by_id(self, document_id):
        """
        Retrieve a document by its ID.
        """
        return next((doc for doc in self.documents if doc.id == document_id), None)

    def add_document_interactive(self):
        """
        Interactively add a new document to the repository.
        """
        print("Enter the details of the new document:")
        title = input("Title: ")
        description = input("Description: ")
        classification = input("Classification: ")
        
        doc_id = self.generate_unique_id()
        file_path = self.generate_file_path(title)
        upload_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        new_doc = Document(id=doc_id, title=title, description=description, 
                           classification=classification, file_path=file_path, 
                           upload_date=upload_date)
        self.add_document(new_doc)
        print("Document added successfully.")

    def generate_unique_id(self):
        """
        Generate a unique ID for a new document.
        """
        return str(max((int(doc.id) for doc in self.documents), default=0) + 1)

    def generate_file_path(self, title):
        """
        Generate a file path for a new document's PDF file.
        """
        base_path = Path('data/documents')
        base_path.mkdir(parents=True, exist_ok=True)
        file_name = f"{title.replace(' ', '_').lower()}.pdf"
        return str(base_path / file_name)

    def update_document_interactive(self):
        """
        Interactively update an existing document in the repository.
        """
        self.list_documents()
        doc_id = input("\nEnter the ID of the document you want to update (or 'cancel' to abort): ")
        
        if doc_id.lower() == 'cancel':
            print("Update cancelled.")
            return

        document = self.get_document_by_id(doc_id)
        if document:
            print(f"\nCurrent information for document '{document.title}':")
            for field, value in document.to_dict().items():
                print(f"{field.capitalize()}: {value}")
            
            print("\nEnter new information (press Enter to keep current value):")
            title = input(f"Title [{document.title}]: ") or document.title
            description = input(f"Description [{document.description}]: ") or document.description
            classification = input(f"Classification [{document.classification}]: ") or document.classification

            # Update the document
            document.title = title
            document.description = description
            document.classification = classification
            document.upload_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Update the text file
            old_txt_path = self._generate_txt_file_path(document.title)
            new_txt_path = self._generate_txt_file_path(title)
            if old_txt_path != new_txt_path:
                if old_txt_path.exists():
                    old_txt_path.unlink()
            self.create_document_txt_file(document)

            # Save changes
            self.save_documents()
            print(f"\nDocument '{title}' has been updated successfully.")
        else:
            print(f"No document found with ID {doc_id}.")

