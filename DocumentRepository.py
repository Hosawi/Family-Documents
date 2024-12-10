import csv
from datetime import datetime
from pathlib import Path
from Document import Document

#----------------------------------------------
# Initialize the repository for managing documents
#----------------------------------------------
class DocumentRepository:
    def __init__(self, csv_file='data/document.csv'):
        """
        Initialize the DocumentRepository with a CSV file path.
        """
        self.documents = []  # Internal storage for document data
        self.csv_file = Path(csv_file)  # Path to the CSV file storing document data
        self.load_documents()  # Load existing documents at initialization

    #------------------------------------------
    # Load documents from CSV into memory
    #------------------------------------------
    def load_documents(self):
        """
        Load documents from the CSV file into memory.
        """
        if self.csv_file.exists():  # Check if the CSV file exists
            with self.csv_file.open('r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self._add_document_from_row(row)  # Convert each row into a Document object

    def _add_document_from_row(self, row):
        """
        Create a Document object from a CSV row and add it to the documents list.
        """
        cleaned_row = {k: v for k, v in row.items() if k and k != 'None'}  # Remove empty or invalid fields
        try:
            self.documents.append(Document(**cleaned_row))  # Instantiate and store the Document object
        except TypeError as e:
            print(f"Error loading document: {e}")  # Log errors during document creation
            print(f"Problematic row: {cleaned_row}")
            print("Skipping this document and continuing...")  # Skip invalid documents

    #------------------------------------------
    # Save current documents to the CSV file
    #------------------------------------------
    def save_documents(self):
        """
        Save all documents to the CSV file.
        """
        self.csv_file.parent.mkdir(parents=True, exist_ok=True)  # Ensure the directory exists
        with self.csv_file.open('w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=Document.get_fields())  # Get document fieldnames
            writer.writeheader()  # Write CSV header
            for doc in self.documents:
                writer.writerow(doc.to_dict())  # Save each document as a row

    #------------------------------------------
    # Add and manage document files
    #------------------------------------------
    def add_document(self, document):
        """
        Add a new document to the repository and save it.
        """
        self.documents.append(document)  # Append the new document
        self.save_documents()  # Persist the change
        self.create_document_txt_file(document)  # Create a corresponding text file

    def create_document_txt_file(self, document):
        """
        Create a text file containing the document's details.
        """
        txt_file_path = self._generate_txt_file_path(document.title)
        txt_file_path.parent.mkdir(parents=True, exist_ok=True)  # Ensure the directory exists
        with txt_file_path.open('w') as file:
            for field, value in document.to_dict().items():
                file.write(f"{field.capitalize()}: {value}\n")  # Write details in human-readable format

    def _generate_txt_file_path(self, title):
        """
        Generate a file path for the document's text file.
        """
        return Path('data/documents') / f"{title.replace(' ', '_').lower()}.txt"  # Standardize file naming

    #------------------------------------------
    # Display documents to the user
    #------------------------------------------
    def list_documents(self):
        """
        Print a list of all documents in the repository.
        """
        print("\nCurrent Documents:")
        for doc in self.documents:
            print(f"ID: {doc.id}, Title: {doc.title}")  # Display basic information for each document

    #------------------------------------------
    # Remove a document and its associated files
    #------------------------------------------
    def remove_document(self):
        """
        Remove a document from the repository based on user input.
        """
        self.list_documents()  # Show current documents
        doc_id = input("Enter the ID of the document to delete (or 'cancel' to abort): ")
        
        if doc_id.lower() == 'cancel':
            print("Deletion cancelled.")  # Abort deletion if requested
            return

        document = self.get_document_by_id(doc_id)  # Retrieve document by ID
        if document:
            if self._confirm_deletion(document):  # Confirm before deleting
                self._delete_document_files(document)  # Remove associated files
                self._remove_document_from_list(doc_id)  # Remove from repository
                self.save_documents()  # Persist changes
                print("\nUpdated list of documents:")
                self.list_documents()
        else:
            print(f"No document found with ID {doc_id}.")  # Handle invalid IDs

    def _confirm_deletion(self, document):
        """
        Ask for user confirmation before deleting a document.
        """
        confirm = input(f"Are you sure you want to delete '{document.title}'? (yes/no): ")
        return confirm.lower() == 'yes'  # Proceed only with explicit confirmation

    def _delete_document_files(self, document):
        """
        Delete the text and PDF files associated with a document.
        """
        deleted_files = []
        txt_file_path = self._generate_txt_file_path(document.title)  # Get text file path
        pdf_file_path = Path(document.file_path)  # Get PDF file path

        for file_path in [txt_file_path, pdf_file_path]:
            if file_path.exists():
                file_path.unlink()  # Remove the file
                deleted_files.append(str(file_path))

        print(f"\nDocument '{document.title}' has been deleted.")
        print("The following files have been removed:")
        for file in deleted_files:
            print(f"- {file}")

    #------------------------------------------
    # Search and retrieve documents
    #------------------------------------------
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
            print("No documents found matching the keyword.")  # Notify if no matches found
        
        return results

    def _basic_search(self, keyword):
        """
        Perform a basic search on all document fields.
        """
        return [
            doc for doc in self.documents
            if any(keyword in str(value).lower() for value in doc.to_dict().values())  # Match any field
        ]

    def get_document_by_id(self, document_id):
        """
        Retrieve a document by its ID.
        """
        return next((doc for doc in self.documents if doc.id == document_id), None)  # Find document by ID
