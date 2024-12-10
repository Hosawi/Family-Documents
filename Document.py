# Import necessary modules for creating a robust document class # Essential for type hinting and data class functionality
from dataclasses import dataclass, asdict  # asdict helps convert class to dictionary
from typing import List  # For type annotations


# Define the Document class using dataclass for efficient class creation # Reduces boilerplate code for initialization
@dataclass
class Document:
    # Class attributes with type hints # Provides clear structure for document metadata
    id: str            # Unique identifier for the document  # Like a library catalog number
    title: str         # Name or headline of the document  # What the document is about
    description: str   # Detailed explanation of the document  # Additional context
    classification: str  # Category or type of document  # Helps in organizing documents
    file_path: str     # Location of the actual document file  # Where to find the physical/digital document
    upload_date: str   # Timestamp of when document was added  # Tracking document entry


    # Class method to retrieve field names # Useful for introspection and dynamic processing
    @classmethod
    def get_fields(cls) -> List[str]:
        # Returns a list of all class attributes # Helps in dynamically working with document fields
        return list(cls.__annotations__.keys())  # Uses type annotations to get field names


    # Method to convert document instance to a dictionary # Facilitates easy serialization
    def to_dict(self):
        # Uses asdict to convert dataclass instance to dictionary # Converts complex object to simple key-value pairs
        return asdict(self)  # Standard way to serialize dataclass objects
