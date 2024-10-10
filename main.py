# This file runs by the "end user" and imports other modules to make use of their functions/classes.

from user import User 
#from document import Document 
#from documentRepository import DocumentRepository 
#from metadataManager import MetadataManager
#from fileUploader import FileUploader
import os # To use some OS functions 


#def main():
    
#-----  My test center ------: 
### Testing User input ### 
def clear_screen():
    # This works for Windows and Unix-based systems
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome_user(user):
    print(f"Welcome, {user.username}!, email: ,{user.email}, pass:,{user.password} ")
  
## ------ 
def main():
    user = User("Abdul Hosawi", "hosawi@iastate.edu", "I can't give you my secure_password :-)")
    clear_screen()
    welcome_user(user)

""""
I want to create a loop within main to show a menu with the following options:
(1) Create a new document.
(2) Search for a document.
(3) Update document data.
(X) to exit the system.
User is asked to select a number from the menu.
"""
# ======  Testing document class methods =========

#---------------------------------------
if __name__ == "__main__":
    main()


# ======  Testing user class methods =========
# ======  Testing documnet class methods =========
# ======  Testing documentRepository class methods =========
# ======  Testing metadataManager class methods =========
# ======  Testing FileUploader class methods =========
 #if __name__ == "__main__":
  #  main()

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