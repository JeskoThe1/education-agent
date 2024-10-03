import os
import sys

# Add the backend directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from backend.src.data_processing.preprocessor import Preprocessor

preprocessor = Preprocessor()

def process_file_by_path(file_path):
    file_extension = os.path.splitext(file_path)[1].lower()
    
    if file_extension == '.pdf':
        return preprocessor.process_pdf(file_path)
    elif file_extension in ['.doc', '.docx']:
        return preprocessor.process_doc(file_path)
    elif file_extension == '.txt':
        return preprocessor.process_txt(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_extension}")