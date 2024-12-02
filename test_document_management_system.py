#test_document_management_system.py
"""
I'm plan to create a code that will be used to test the functionality of a Document Management System (DMS) ver 2. The primary goal of this testing process will be to verify that the system meets its key requirements, including the ability to create, update, delete, and search for documents effectively. 

To achieve this, I will follow a structured approach. First, I will set up the testing environment by initializing the necessary components within the FDS framework. This will include creating a test CSV file and any other essential elements required for the process. Next, I will run tests to evaluate the functionality of each feature, such as adding documents to the repository. Additionally, I will create a mock user to interact with the system, allowing me to verify the operation of various features under simulated real-world conditions. 

Finally, I will clean up the test files to ensure a tidy and reusable environment for future testing. By following these steps, I aim to validate the effectiveness of the DMS Ver2 testing process, ensuring that the system meets its intended requirements.
""" 
#-- Imports lists 
import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from pathlib import Path
import csv
from datetime import datetime
#-----------------------------------
from DocumentRepository import DocumentRepository
from Document import Document
from main import DocumentManagementSystem  #The file is named 'main.py'

class TestDocumentManagementSystem(unittest.TestCase):

    def setUp(self):
        self.test_csv_file = 'test_documents.csv'
        self.repo = DocumentRepository(self.test_csv_file)
        self.dms = DocumentManagementSystem()
        self.dms.repo = self.repo

    def tearDown(self):
        # Clean up test files
        Path(self.test_csv_file).unlink(missing_ok=True)
        for file in Path('data/documents').glob('*.txt'):
            file.unlink()
        for file in Path('data/documents').glob('*.pdf'):
            file.unlink()

    def test_add_document(self):
        doc = Document("1", "Test Doc", "A test document", "Confidential", "test.pdf", "2023-04-15 10:00:00")
        self.repo.add_document(doc)
        self.assertEqual(len(self.repo.documents), 1)
        self.assertEqual(self.repo.documents[0].title, "Test Doc")

    def test_remove_document(self):
        doc = Document("1", "Test Doc", "A test document", "Confidential", "test.pdf", "2023-04-15 10:00:00")
        self.repo.add_document(doc)
        
        with patch('builtins.input', side_effect=['1', 'yes']):
            self.repo.remove_document()
        
        self.assertEqual(len(self.repo.documents), 0)

    def test_search_documents(self):
        doc1 = Document("1", "Python Guide", "A guide to Python", "Public", "python.pdf", "2023-04-15 10:00:00")
        doc2 = Document("2", "Java Tutorial", "A Java tutorial", "Public", "java.pdf", "2023-04-15 11:00:00")
        self.repo.add_document(doc1)
        self.repo.add_document(doc2)

        results = self.repo.search_documents("Python")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Python Guide")

    def test_update_document(self):
        doc = Document("1", "Old Title", "Old description", "Public", "old.pdf", "2023-04-15 10:00:00")
        self.repo.add_document(doc)

        with patch('builtins.input', side_effect=['1', 'New Title', 'New description', 'Confidential']):
            self.repo.update_document_interactive()

        updated_doc = self.repo.get_document_by_id("1")
        self.assertEqual(updated_doc.title, "New Title")
        self.assertEqual(updated_doc.description, "New description")
        self.assertEqual(updated_doc.classification, "Confidential")

    def test_load_documents(self):
        # Create a test CSV file
        with open(self.test_csv_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=Document.get_fields())
            writer.writeheader()
            writer.writerow({
                "id": "1",
                "title": "Test Doc",
                "description": "A test document",
                "classification": "Confidential",
                "file_path": "test.pdf",
                "upload_date": "2023-04-15 10:00:00"
            })

        repo = DocumentRepository(self.test_csv_file)
        self.assertEqual(len(repo.documents), 1)
        self.assertEqual(repo.documents[0].title, "Test Doc")

    def test_save_documents(self):
        doc = Document("1", "Test Doc", "A test document", "Confidential", "test.pdf", "2023-04-15 10:00:00")
        self.repo.add_document(doc)
        self.repo.save_documents()

        # Check if the CSV file was created and contains the correct data
        with open(self.test_csv_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]['title'], "Test Doc")

    def test_create_document_txt_file(self):
        doc = Document("1", "Test Doc", "A test document", "Confidential", "test.pdf", "2023-04-15 10:00:00")
        self.repo.create_document_txt_file(doc)

        txt_file_path = Path('data/documents/test_doc.txt')
        self.assertTrue(txt_file_path.exists())

        with txt_file_path.open('r') as file:
            content = file.read()
            self.assertIn("Title: Test Doc", content)
            self.assertIn("Description: A test document", content)

    def test_generate_unique_id(self):
        doc1 = Document("1", "Doc 1", "First document", "Public", "doc1.pdf", "2023-04-15 10:00:00")
        doc2 = Document("2", "Doc 2", "Second document", "Public", "doc2.pdf", "2023-04-15 11:00:00")
        self.repo.add_document(doc1)
        self.repo.add_document(doc2)

        new_id = self.repo.generate_unique_id()
        self.assertEqual(new_id, "3")

    def test_generate_file_path(self):
        title = "My Test Document"
        file_path = self.repo.generate_file_path(title)
        expected_path = str(Path('data/documents/my_test_document.pdf'))
        self.assertEqual(file_path, expected_path)

    @patch('builtins.input', side_effect=['Test Doc', 'A test document', 'Confidential'])
    def test_add_document_interactive(self, mock_input):
        self.repo.add_document_interactive()
        self.assertEqual(len(self.repo.documents), 1)
        self.assertEqual(self.repo.documents[0].title, "Test Doc")

    @patch('builtins.print')
    def test_list_documents(self, mock_print):
        doc1 = Document("1", "Doc 1", "First document", "Public", "doc1.pdf", "2023-04-15 10:00:00")
        doc2 = Document("2", "Doc 2", "Second document", "Public", "doc2.pdf", "2023-04-15 11:00:00")
        self.repo.add_document(doc1)
        self.repo.add_document(doc2)

        self.repo.list_documents()
        mock_print.assert_any_call("ID: 1, Title: Doc 1")
        mock_print.assert_any_call("ID: 2, Title: Doc 2")

    @patch('sys.stdout', new_callable=StringIO)
    def test_run_dms(self, mock_stdout):
        with patch('builtins.input', side_effect=['5']):
            self.dms.run()
        self.assertIn("Exiting the program. Goodbye!", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()


