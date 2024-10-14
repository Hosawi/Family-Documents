# Call upload_document(self), save_document_to_storage(self) from FileUploader class
class FileUploader:
    def upload_document(self):
        # Ask the user to enter the source path of the file to upload
        self.source_path = input("Enter the path of the file you want to upload: ")

    def save_document_to_storage(self):
        # Ensure the img folder exists
        os.makedirs('data/img', exist_ok=True)
        try:
            # Save the document to the img folder
            destination_path = os.path.join('data/img', os.path.basename(self.source_path))
            with open(self.source_path, 'rb') as src_file:
                with open(destination_path, 'wb') as dest_file:
                    dest_file.write(src_file.read())
            print("Document uploaded and saved successfully.")
        except Exception as e:
            print(f"Error during upload: {e}")
            retry_choice = input("Do you want to try again? (Yes/No): ")
            if retry_choice.lower() == 'yes':
                self.upload_document()
                self.save_document_to_storage()
            else:
                print("Returning to main.py")