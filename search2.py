import os
import fitz  # PyMuPDF
import tkinter as tk
from tkinter import messagebox
import webbrowser
import threading

def open_pdf(file_path):
    """Open PDF in the default PDF viewer."""
    try:
        webbrowser.open_new(file_path)
    except Exception as e:
        messagebox.showerror("Error", f"Could not open file: {e}")

def search_keyword_in_pdfs(folder_path, keywords, search_type, results_listbox, loading_label, canvas):
    """Search for keywords in all PDFs in the specified folder based on search type."""
    # Clear previous results
    results_listbox.delete(0, tk.END)
    loading_label.config(text="Searching...")
    loading_label.update()  # Update the loading label immediately
    
    files_checked = 0
    matches_found = 0
    
    # Prepare keywords for search
    keyword_list = [kw.strip().lower() for kw in keywords.split(",") if kw.strip()]
    
    # Loop through each file in the folder
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            if file_name.lower().endswith('.pdf'):  # Only process PDF files
                file_path = os.path.join(root, file_name)
                files_checked += 1
                try:
                    with fitz.open(file_path) as pdf_document:
                        # Iterate through each page in the PDF
                        for page_num in range(pdf_document.page_count):
                            page = pdf_document[page_num]
                            text = page.get_text().lower()  # Extract text and make it lowercase
                            
                            # Check based on search type: 'any' or 'all'
                            if (search_type == "any" and any(keyword in text for keyword in keyword_list)) or \
                               (search_type == "all" and all(keyword in text for keyword in keyword_list)):
                                results_listbox.insert(
                                    tk.END, f"{file_path} (page {page_num + 1}) - Match found"
                                )
                                matches_found += 1
                                break  # Stop checking this file if match criteria is met
                except Exception as e:
                    print(f"Could not read file {file_path}: {e}")
    
    # Show summary in listbox if no matches found
    if matches_found == 0:
        results_listbox.insert(tk.END, f"No matches found for keywords: {', '.join(keyword_list)} in {files_checked} PDF files.")
    
    # Update the scroll region of the canvas to match the listbox content
    canvas.config(scrollregion=canvas.bbox("all"))
    
    # Hide the loading indicator
    loading_label.config(text="Search Complete")

def on_listbox_select(event):
    """Handle clicking an item in the results listbox."""
    selected_item = event.widget.get(event.widget.curselection())
    file_path = selected_item.split(" (page")[0]  # Get the file path from the item
    open_pdf(file_path)

def start_search_thread(folder_path, keywords, search_type, results_listbox, loading_label, canvas):
    """Start the search in a separate thread to keep the GUI responsive."""
    search_thread = threading.Thread(target=search_keyword_in_pdfs, args=(folder_path, keywords, search_type, results_listbox, loading_label, canvas))
    search_thread.start()

def main():
    # Create the main window
    root = tk.Tk()
    root.title("PDF Multi-Keyword Search")
    
    # Set the window size
    root.geometry("600x450")
    
    # Input fields and button
    tk.Label(root, text="Folder Path:").pack()
    folder_entry = tk.Entry(root, width=50)
    folder_entry.pack()
    folder_entry.insert(0, r"C:\root\archive")  # Pre-fill with the default path
    
    tk.Label(root, text="Keywords (comma-separated):").pack()
    keyword_entry = tk.Entry(root, width=50)
    keyword_entry.pack()
    
    # Add radio buttons for search type
    search_type = tk.StringVar(value="any")  # Default to "any"
    tk.Label(root, text="Search Type:").pack()
    tk.Radiobutton(root, text="Any keywords", variable=search_type, value="any").pack()
    tk.Radiobutton(root, text="All keywords", variable=search_type, value="all").pack()
    
    # Create a canvas and scrollbar for the listbox
    canvas = tk.Canvas(root)
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    
    # Create a frame inside the canvas for the listbox
    results_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=results_frame, anchor="nw")
    
    # Create the listbox inside the frame
    results_listbox = tk.Listbox(results_frame, width=160, height=40)
    results_listbox.pack()
    results_listbox.bind("<<ListboxSelect>>", on_listbox_select)
    
    # Pack the canvas and scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    # Loading label
    loading_label = tk.Label(root, text="Ready to Search", fg="blue")
    loading_label.pack()

    def start_search():
        folder_path = folder_entry.get()
        keywords = keyword_entry.get()
        if not os.path.isdir(folder_path):
            messagebox.showerror("Error", "Please enter a valid folder path.")
            return
        if not keywords:
            messagebox.showerror("Error", "Please enter at least one keyword.")
            return
        
        # Start the search in a separate thread with the selected search type
        start_search_thread(folder_path, keywords, search_type.get(), results_listbox, loading_label, canvas)
    
    # Search button
    search_button = tk.Button(root, text="Search", command=start_search)
    search_button.pack()
    
    # Run the GUI loop
    root.mainloop()

if __name__ == "__main__":
    main()
