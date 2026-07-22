"""
Q101. File Type Check

Take a filename as input (like report.pdf). Check if it ends with .pdf, .docx,
or .txt and print the file type.
"""

def check_file_type(filename):
    if filename.endswith(".pdf") or filename.endswith(".txt") or filename.endswith(".docx"):
        print("Valid file")
    else:
        print("Invalid file")
filename = "report.txt"
check_file_type(filename)