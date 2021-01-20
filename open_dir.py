import os
from pathlib import Path

def open_downloads():
    path = str(Path.home() / "Downloads")
    path = os.path.realpath(path)
    os.startfile(path)

def open_documents():
    path = str(Path.home() / "Documents")
    path = os.path.realpath(path)
    os.startfile(path)
    
def open_desktop():
    path = str(Path.home() / "Desktop")
    path = os.path.realpath(path)
    os.startfile(path)
