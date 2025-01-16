# PDF Keyword Search Tool

A Python-based desktop application that allows users to search for multiple keywords across PDF files in a specified directory. The tool features a simple graphical user interface and supports both "any" and "all" keyword matching modes.

## Features

- Search through multiple PDF files in a directory and its subdirectories
- Support for multiple comma-separated keywords
- Two search modes:
  - "Any keywords" - matches PDFs containing any of the specified keywords
  - "All keywords" - matches PDFs containing all specified keywords
- Results display with file path and page number
- Click-to-open functionality for matched PDF files
- Real-time search status indication
- Scrollable results view
- Multi-threaded search to maintain GUI responsiveness

## Prerequisites

To run this application, you'll need:

- Python 3.6 or higher
- PyMuPDF (fitz)
- tkinter (usually comes with Python)

## Installation

1. Clone this repository:
```bash
git clone [your-repository-url]
cd [repository-name]
```

2. Install the required dependencies:
```bash
pip install PyMuPDF
```

## Usage

1. Run the application:
```bash
python search2.py
```

2. In the application window:
   - Enter the folder path to search (default is "C:\root\archive")
   - Enter keywords separated by commas (e.g., "keyword1, keyword2, keyword3")
   - Select search mode ("Any keywords" or "All keywords")
   - Click "Search" to begin

3. Results will appear in the scrollable list:
   - Each result shows the file path and page number where matches were found
   - Click any result to open the PDF in your default PDF viewer

## Error Handling

The application includes error handling for:
- Invalid folder paths
- Empty keyword inputs
- PDF file access issues
- File opening errors

## Performance Considerations

- The search is performed in a separate thread to prevent GUI freezing
- Progress updates are shown through a status label
- Large directories with many PDFs may take longer to process

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

None

## Acknowledgments

This tool uses the following open-source packages:
- [PyMuPDF](https://github.com/pymupdf/PyMuPDF) for PDF processing
- Python's built-in tkinter for the GUI


---

<p align="center">
  <img src="https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif" alt="Code is Life" width="120">
</p>

<p align="center">
  <b>⌨️ with 💻 by Raj Reddy</b><br>
  <code>// Reach out if you find bugs in the matrix</code><br>
  <a href="https://github.com/neuralnet19" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-000000?style=flat-square&logo=github&logoColor=white" alt="GitHub">
  </a>
  <a href="mailto:neuralnet19@hotmail.com" target="_blank">
    <img src="https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white" alt="Email">
  </a>
</p>

<p align="center">
  <code>// "Hello, World!" is just the beginning 🚀</code>
</p>

---
