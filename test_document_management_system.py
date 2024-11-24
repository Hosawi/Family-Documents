#test_document_management_system.py
"""
I'm plan to create a code that will be used to test the functionality of a Document Management System (DMS) ver 2. The primary goal of this testing process will be to verify that the system meets its key requirements, including the ability to create, update, delete, and search for documents effectively. 

To achieve this, I will follow a structured approach. First, I will set up the testing environment by initializing the necessary components within the FDS framework. This will include creating a test CSV file and any other essential elements required for the process. Next, I will run tests to evaluate the functionality of each feature, such as adding documents to the repository. Additionally, I will create a mock user to interact with the system, allowing me to verify the operation of various features under simulated real-world conditions. 

Finally, I will clean up the test files to ensure a tidy and reusable environment for future testing. By following these steps, I aim to validate the effectiveness of the DMS Ver2 testing process, ensuring that the system meets its intended requirements.
""" 
#-- Imports lists 
from DocumentRepository import DocumentRepository
from Document import Document
from main import DocumentManagementSystem  #The file is named 'main.py'

class TestDocumentManagementSystem(unittest.TestCase):

    def setUp(self):

