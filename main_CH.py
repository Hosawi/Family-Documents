# This file runs by the "end user" and imports other modules to make use of their functions/classes.

from user import User 
#from document import Document 
#from documentRepository import DocumentRepository 
#from metadataManager import MetadataManager
#from fileUploader import FileUploader
import os # To use some OS functions 
from DocumentRepository import DocumentRepository
dr = DocumentRepository()
#def main():
    
#-----  My test center ------: 
### Testing User input ### 
def clear_screen():
    # This works for Windows and Unix-based systems
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome_user(user):
    print(f"Welcome, {user.username}!, email: ,{user.email}, pass:,{user.password} ")
  
def display_menu():
    print("Menu:")
    print("(1) Create a new document.")
    print("(2) Search for a document.")
    print("(3) List documents")
    print("(4) Remove documents")
    print("(X) Exit the system.")

## ------ 
def main():
    user = User("Abdul Hosawi", "hosawi@iastate.edu", "I can't give you my secure_password :-)")
    clear_screen()
    welcome_user(user)

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip().upper()
        
        if choice == '1':
            dr.add_document_interactive()
        elif choice == '2':
            st = input("Enter the search term: ")
            dr.search_documents(st)  # doesn't work
        elif choice == '3':
            print(dr.documents)
        elif choice == '4':
            id = input("Document ID?")
            dr.remove_document(id)
        elif choice == 'X':
            print("Exiting the system...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
