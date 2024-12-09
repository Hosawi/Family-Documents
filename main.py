""" My plan of creating this file is to make the code in GUI.py runs 
the Family-Doc-Sys directly. The main program will start the main
 window and the program keeps running until we close it. 
"""
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from DocumentRepository import DocumentRepository
from Document import Document
from datetime import datetime

class GUIDocumentHandler:
    def __init__(self, repo):
        self.repo = repo

    def create_document(self, title, description, classification):
        doc_id = self.repo.generate_unique_id()
        file_path = self.repo.generate_file_path(title)
        upload_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        new_doc = Document(id=doc_id, title=title, description=description, 
                           classification=classification, file_path=file_path, 
                           upload_date=upload_date)
        self.repo.add_document(new_doc)
        return new_doc

    def update_document(self, doc_id, title, description, classification):
        document = self.repo.get_document_by_id(doc_id)
        if document:
            document.title = title
            document.description = description
            document.classification = classification
            document.upload_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.repo.save_documents()
            return True
        return False

    def delete_document(self, doc_id):
        document = self.repo.get_document_by_id(doc_id)
        if document:
            self.repo._delete_document_files(document)
            self.repo._remove_document_from_list(doc_id)
            self.repo.save_documents()
            return True
        return False

    def search_documents(self, keyword):
        return self.repo._basic_search(keyword)


class DocumentManagementSystemGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Document Management System")
        self.master.geometry("800x600")
        
        self.repo = DocumentRepository()
        self.gui_handler = GUIDocumentHandler(self.repo)
        
        self.create_widgets()

    def create_widgets(self):
        # Create a notebook (tabbed interface)
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(expand=True, fill="both", padx=10, pady=10)

        # Create tabs
        self.create_tab = ttk.Frame(self.notebook)
        self.update_tab = ttk.Frame(self.notebook)
        self.delete_tab = ttk.Frame(self.notebook)
        self.search_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.create_tab, text="Create Document")
        self.notebook.add(self.update_tab, text="Update Document")
        self.notebook.add(self.delete_tab, text="Delete Document")
        self.notebook.add(self.search_tab, text="Search Documents")

        # Populate tabs
        self.setup_create_tab()
        self.setup_update_tab()
        self.setup_delete_tab()
        self.setup_search_tab()

    def setup_create_tab(self):
        ttk.Label(self.create_tab, text="Create New Document", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

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

    def setup_update_tab(self):
        ttk.Label(self.update_tab, text="Update Existing Document", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

        # Create a frame for the document list
        list_frame = ttk.Frame(self.update_tab)
        list_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Create a scrollbar
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create a listbox with scrollbar
        self.update_listbox = tk.Listbox(list_frame, width=70, height=10, yscrollcommand=scrollbar.set)
        self.update_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.update_listbox.yview)

        # Bind double-click event to the listbox
        self.update_listbox.bind('<Double-1>', self.on_document_select)

        # Add a refresh button
        ttk.Button(self.update_tab, text="Refresh Document List", command=self.refresh_update_list).grid(row=2, column=0, pady=10)

        # Create a frame for the update form
        self.update_frame = ttk.Frame(self.update_tab)
        self.update_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Initial population of the listbox
        self.refresh_update_list()

    def refresh_update_list(self):
        self.update_listbox.delete(0, tk.END)
        for doc in self.repo.documents:
            self.update_listbox.insert(tk.END, f"{doc.id}: {doc.title}")

    def on_document_select(self, event):
        selection = self.update_listbox.curselection()
        if selection:
            doc_id = self.update_listbox.get(selection[0]).split(":")[0]
            document = self.repo.get_document_by_id(doc_id)
            if document:
                self.show_update_form(document)



    def setup_delete_tab(self):
        ttk.Label(self.delete_tab, text="Delete Document", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

        self.delete_listbox = tk.Listbox(self.delete_tab, width=70, height=15)
        self.delete_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        ttk.Button(self.delete_tab, text="Refresh Document List", command=self.refresh_delete_list).grid(row=2, column=0, pady=10)
        ttk.Button(self.delete_tab, text="Delete Selected Document", command=self.delete_document).grid(row=2, column=1, pady=10)

        self.refresh_delete_list()

    def setup_search_tab(self):
        ttk.Label(self.search_tab, text="Search Documents", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Label(self.search_tab, text="Keyword:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.search_entry = ttk.Entry(self.search_tab, width=50)
        self.search_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(self.search_tab, text="Search", command=self.search_documents).grid(row=2, column=0, columnspan=2, pady=20)

        self.search_result = tk.Text(self.search_tab, width=70, height=15)
        self.search_result.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def create_document(self):
        title = self.title_entry.get()
        description = self.description_entry.get()
        classification = self.classification_entry.get()

        if not all([title, description, classification]):
            messagebox.showerror("Error", "All fields are required")
            return

        new_doc = self.gui_handler.create_document(title, description, classification)
        messagebox.showinfo("Success", f"Document '{new_doc.title}' created successfully")
        self.clear_create_fields()

    def clear_create_fields(self):
        self.title_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.classification_entry.delete(0, tk.END)

    def select_document_to_update(self):
        documents = self.repo.documents
        choices = [f"{doc.id}: {doc.title}" for doc in documents]
        choice = simpledialog.askstring("Select Document", "Choose a document to update:", initialvalue=choices[0] if choices else "")
 
        if choice:
            doc_id = choice.split(":")[0]
            document = self.repo.get_document_by_id(doc_id)
            if document:
                self.show_update_form(document)

    def show_update_form(self, document):
        for widget in self.update_frame.winfo_children():
            widget.destroy()

        ttk.Label(self.update_frame, text=f"Updating Document: {document.title}", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Label(self.update_frame, text="Title:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.update_title_entry = ttk.Entry(self.update_frame, width=50)
        self.update_title_entry.insert(0, document.title)
        self.update_title_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.update_frame, text="Description:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.update_description_entry = ttk.Entry(self.update_frame, width=50)
        self.update_description_entry.insert(0, document.description)
        self.update_description_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self.update_frame, text="Classification:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.update_classification_entry = ttk.Entry(self.update_frame, width=50)
        self.update_classification_entry.insert(0, document.classification)
        self.update_classification_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Button(self.update_frame, text="Update Document", command=lambda: self.update_document(document.id)).grid(row=4, column=0, columnspan=2, pady=20)

    def update_document(self, doc_id):
        title = self.update_title_entry.get()
        description = self.update_description_entry.get()
        classification = self.update_classification_entry.get()

        if self.gui_handler.update_document(doc_id, title, description, classification):
            messagebox.showinfo("Success", f"Document '{title}' updated successfully")
            self.refresh_update_list()  # Refresh the list to show updated title
        else:
            messagebox.showerror("Error", "Failed to update document")


    def refresh_delete_list(self):
        self.delete_listbox.delete(0, tk.END)
        for doc in self.repo.documents:
            self.delete_listbox.insert(tk.END, f"{doc.id}: {doc.title}")

    def delete_document(self):
        selection = self.delete_listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "Please select a document to delete")
            return

        doc_id = self.delete_listbox.get(selection[0]).split(":")[0]
        document = self.repo.get_document_by_id(doc_id)

        if messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete '{document.title}'?"):
            if self.gui_handler.delete_document(doc_id):
                self.refresh_delete_list()
                messagebox.showinfo("Success", f"Document '{document.title}' deleted successfully")
            else:
                messagebox.showerror("Error", "Failed to delete document")
#---------------------------------------------- 
    def search_documents(self):
        keyword = self.search_entry.get()
        results = self.gui_handler.search_documents(keyword)

        self.search_result.delete(1.0, tk.END)
        if results:
            for doc in results:
                self.search_result.insert(tk.END, f"ID: {doc.id}, Title: {doc.title}, Classification: {doc.classification}\n\n")
        else:
            self.search_result.insert(tk.END, "No documents found matching the keyword.")

def main():
    root = tk.Tk()
    app = DocumentManagementSystemGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
