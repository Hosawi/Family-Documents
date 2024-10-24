# Notce: This file runs by the "end user" and imports other modules to make use of their functions/classes.

from DocumentRepository import DocumentRepository

class DocumentManagementSystem:
    def __init__(self):
        self.repo = DocumentRepository()

    def display_menu(self):
        print("\nDocument Management System")
        print("1. Create new document")
        print("2. Update existing document")
        print("3. Delete document")
        print("4. Search documents")
        print("5. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                self.repo.add_document_interactive()
            elif choice == '2':
                self.update_document()
            elif choice == '3':
                self.delete_document()
            elif choice == '4':
                self.search_documents()
            elif choice == '5':
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def update_document(self):
        self.repo.update_document_interactive()

    def delete_document(self):
        self.repo.remove_document()

    def search_documents(self):
        keyword = input("Enter a keyword to search for: ")
        results = self.repo.search_documents(keyword)



if __name__ == "__main__":
    dms = DocumentManagementSystem()
    dms.run()
