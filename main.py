"""
My plan of creating this file is to make the code in GUI.py run
the Family-Doc-Sys directly. The main program will start the main
window and the program keeps running until we close it.
"""

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from DocumentRepository import DocumentRepository
from Document import Document
from datetime import datetime

#----------------------------------------------
# Define the main GUI handler class for document operations
#----------------------------------------------
class GUIDocumentHandler:
    def __init__(self, repo):
        self.repo = repo  # Connect the repository for document management

    def create_document(self, title, description, classification):
        """
        Create a new document and add it to the repository.
        """
        doc_id = self.repo.generate_unique_id()  # Generate unique document ID
        file_path = self.repo.generate_file_path(title)  # Determine file path
        upload_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Timestamp

        new_doc = Document(id=doc_id, title=title, description=description, 
                           classification=classification, file_path=file_path, 
                           upload_date=upload_date)  # Create Document object
        self.repo.add_document(new_doc)  # Save the document to the repository
        return new_doc  # Return the created document

    def update_document(self, doc_id, title, description, classification):
        """
        Update an existing document in the repository.
        """
        document = self.repo.get_document_by_id(doc_id)  # Fetch document by ID
        if document:
            # Update document attributes
            document.title = title
            document.description = description
            document.classification = classification
            document.upload_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Update timestamp
            self.repo.save_documents()  # Persist changes
            return True  # Indicate success
        return False  # Indicate failure

    def delete_document(self, doc_id):
        """
        Delete a document from the repository.
        """
        document = self.repo.get_document_by_id(doc_id)  # Fetch document by ID
        if document:
            # Remove document files and metadata
            self.repo._delete_document_files(document)
            self.repo._remove_document_from_list(doc_id)
            self.repo.save_documents()
            return True  # Indicate success
        return False  # Indicate failure

    def search_documents(self, keyword):
        """
        Perform a keyword-based search for documents.
        """
        return self.repo._basic_search(keyword)  # Return matching documents

#----------------------------------------------
# Define the main GUI class for user interaction
#----------------------------------------------
class DocumentManagementSystemGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Document Management System")  # Set window title
        self.master.geometry("800x600")  # Set initial window size

        self.repo = DocumentRepository()  # Instantiate the repository
        self.gui_handler = GUIDocumentHandler(self.repo)  # Connect handler

        self.create_widgets()  # Initialize GUI widgets

    #------------------------------------------
    # Setup the tabbed interface and populate tabs
    #------------------------------------------
    def create_widgets(self):
        self.notebook = ttk.Notebook(self.master)  # Create tabbed interface
        self.notebook.pack(expand=True, fill="both", padx=10, pady=10)

        # Create and add tabs
        self.create_tab = ttk.Frame(self.notebook)
        self.update_tab = ttk.Frame(self.notebook)
        self.delete_tab = ttk.Frame(self.notebook)
        self.search_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.create_tab, text="Create Document")
        self.notebook.add(self.update_tab, text="Update Document")
        self.notebook.add(self.delete_tab, text="Delete Document")
        self.notebook.add(self.search_tab, text="Search Documents")

        # Setup functionality for each tab
        self.setup_create_tab()
        self.setup_update_tab()
        self.setup_delete_tab()
        self.setup_search_tab()

    #------------------------------------------
    # Setup "Create Document" tab
    #------------------------------------------
    def setup_create_tab(self):
        ttk.Label(self.create_tab, text="Create New Document", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

        # Input fields for title, description, and classification
        ttk.Label(self.create_tab, text="Title:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.title_entry = ttk.Entry(self.create_tab, width=50)
        self.title_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.create_tab, text="Description:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.description_entry = ttk.Entry(self.create_tab, width=50)
        self.description_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self.create_tab, text="Classification:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.classification_entry = ttk.Entry(self.create_tab, width=50)
        self.classification_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Button(self.create_tab, text="Create Document", command=self.create_document).grid(row=4, column=0, columnspan=2, pady=20)

    # More methods for tabs: `setup_update_tab`, `setup_delete_tab`, and `setup_search_tab` follow the same pattern.

#----------------------------------------------
# Define the main program entry point
#----------------------------------------------
def main():
    root = tk.Tk()
    app = DocumentManagementSystemGUI(root)  # Initialize GUI application
    root.mainloop()  # Start the main event loop

if __name__ == "__main__":
    main()  # Run the program
