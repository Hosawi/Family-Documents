# Family Document Management System (FDMS)

## Overview

The Family Document Management System (FDMS) is a desktop application designed to help families efficiently store, organize, and retrieve important documents. This application solves the common challenge of scattered document storage by providing a centralized, user-friendly solution for managing family documents.

## Key Features

- **Document Creation**: Easily add new documents with details like title, description, and classification
- **Document Update**: Modify existing document metadata
- **Document Deletion**: Remove documents from the system
- **Advanced Search**: Find documents using keywords across all document fields
- **Automatic ID Generation**: Unique identifiers assigned to each document
- **Automatic Date Tracking**: Upload dates are automatically recorded

## Supported Document Categories

- Education
- Health
- Financial
- Government and Private Services
- Self-Development
- Family Photos

## System Requirements

- Python 3.x
- Tkinter (included in standard Python distribution)

## Installation

1. Ensure Python 3.x is installed on your system
2. Clone the repository
3. Install required dependencies (if any)

## Getting Started

### Launching the Application

Run the following command:
```bash
python GUI.py
```

### User Interface

The application features a tabbed interface with four main sections:

1. **Create Document**
   - Enter document title
   - Add description
   - Select classification
   - Click "Create Document"

2. **Update Document**
   - Select a document from the list
   - Modify document details
   - Click "Update Document"

3. **Delete Document**
   - Select a document from the list
   - Click "Delete Selected Document"
   - Confirm deletion

4. **Search Documents**
   - Enter a keyword
   - View search results

## Data Storage

- Documents are stored in `data/document.csv`
- Individual document details are saved as text files
- Metadata includes:
  - Unique auto ID
  - Title
  - Description

  
  

## Error Handling

- Invalid inputs are prevented
- Helpful error messages guide user actions
- Problematic data rows are skipped during loading

## Future Roadmap

- Enhanced GUI design
- More robust error handling
- Additional document management features

## Contributing

Contributions are welcome! Please submit pull requests or open issues on the project repository.

## License
https://github.com/Hosawi/Family-Documents/blob/main/LICENSE  
 

## Contact

Abduljaleel Hosawi

## Acknowledgments

Special thanks to Dr. Chris for guidance during the project development.
