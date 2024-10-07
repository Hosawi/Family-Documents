# This file runs by the "end user" and imports other modules to make use of their functions/classes.

from user import User 
from document import Document 
from documentRepository import DocumentRepository 
from metadataManager import MetadataManager
from fileUploader import FileUploader


def main():
    
#-----  My test center ------: 
###v Runnin functions W/ simulated user input ###
# ======  Testing document class methods =========
# ======  Testing user class methods =========
# ======  Testing documnet class methods =========
# ======  Testing documentRepository class methods =========
# ======  Testing metadataManager class methods =========
# ======  Testing FileUploader class methods =========
 if __name__ == "__main__":
    main()

"""
 Sequence Diagram  
    participant User  
    participant FileUploader  
    participant DocumentRepository  
    participant MetadataManager  
 -----------------------------------
 User->>FileUploader: Upload document  
    FileUploader->>DocumentRepository: Create new document  
    DocumentRepository->>MetadataManager: Get metadata from user  
    MetadataManager-->DocumentRepository: Return metadata  
    DocumentRepository->>FileUploader: Save document to storage  
    FileUploader-->DocumentRepository: Return document ID  
    DocumentRepository-->User: Document uploaded successfully  
"""