# Notice: This file is the main entry point for the Document Management System # Provides user interaction and program flow
# Imports the core repository for document management # Central component for handling document operations
from DocumentRepository import DocumentRepository


# Main class to manage the document management system # Orchestrates user interactions and system functionality
class DocumentManagementSystem:
    # Initialize the document management system # Sets up the core repository for document operations
    def __init__(self):
        self.repo = DocumentRepository()  # Create a repository instance to handle documents # Like a digital filing cabinet


    # Display the main menu options to the user # Provides a clear interface for user interaction
    def display_menu(self):
        print("\nDocument Management System")  # Main menu title # Clearly identifies the application
        print("1. Create new document")       # Option to add new documents # Expanding the digital filing system
        print("2. Update existing document")  # Option to modify document details # Keeping information current
        print("3. Delete document")           # Option to remove documents # Maintaining a clean document collection
        print("4. Search documents")          # Option to find specific documents # Quick retrieval of information
        print("5. Exit")                      # Option to close the application # Graceful program termination


    # Main program loop to handle user interactions # Drives the entire document management process
    def run(self):
        while True:
            self.display_menu()  # Show the menu options # Continuous user guidance
            choice = input("Enter your choice (1-5): ")  # Capture user input # Determine next action


            # Route user choices to appropriate methods # Like a switchboard directing calls
            if choice == '1':
                self.repo.add_document_interactive()  # Create a new document # Adding to the digital archive
            elif choice == '2':
                self.update_document()  # Update an existing document # Keeping information up-to-date
            elif choice == '3':
                self.delete_document()  # Remove a document # Maintaining document collection
            elif choice == '4':
                self.search_documents()  # Search for documents # Finding specific information quickly
            elif choice == '5':
                print("Exiting the program. Goodbye!")  # Farewell message # Polite program exit
                break  # Terminate the program loop # Graceful shutdown
            else:
                print("Invalid choice. Please try again.")  # Error handling # Guiding user back to correct input


    # Delegate method to update an existing document # Wrapper for repository update functionality
    def update_document(self):
        self.repo.update_document_interactive()  # Call repository method to update document # Modifying document details


    # Delegate method to delete a document # Wrapper for repository deletion functionality
    def delete_document(self):
        self.repo.remove_document()  # Call repository method to remove document # Cleaning up document collection


    # Method to search for documents # Provides user-driven document search
    def search_documents(self):
        keyword = input("Enter a keyword to search for: ")  # Capture search term # User-defined search criteria
        results = self.repo.search_documents(keyword)  # Perform search in repository # Retrieve matching documents


# Entry point of the application # Starts the document management system
if __name__ == "__main__":
    dms = DocumentManagementSystem()  # Create an instance of the management system # Initialize the application
    dms.run()  # Start the main program loop # Begin user interaction
