from abc import ABC, abstractmethod
from datetime import datetime
from typing import List

# Single Responsibility Principle (SRP)
# Each class has one specific responsibility

class DocumentValidator:
    """Responsible only for validating documents"""
    
    def validate_format(self, content: str) -> bool:
        """Validates if the document has correct format"""
        return len(content.strip()) > 0 and len(content) < 1000
    
    def validate_metadata(self, title: str, author: str) -> bool:
        """Validates document metadata"""
        return bool(title.strip()) and bool(author.strip())


class DocumentStorage:
    """Responsible only for storing and retrieving documents"""
    
    def __init__(self):
        self.documents = {}
    
    def save(self, doc_id: str, content: str) -> bool:
        """Saves document to storage"""
        if doc_id and content:
            self.documents[doc_id] = {
                'content': content,
                'timestamp': datetime.now()
            }
            return True
        return False
    
    def get(self, doc_id: str) -> dict:
        """Retrieves document from storage"""
        return self.documents.get(doc_id)


# Interface Segregation Principle (ISP)
# Split interfaces into smaller, specific ones that clients actually need

class Printable(ABC):
    """Interface for printable documents"""
    
    @abstractmethod
    def print_content(self) -> str:
        pass


class Exportable(ABC):
    """Interface for exportable documents"""
    
    @abstractmethod
    def export_to_file(self, filepath: str) -> bool:
        pass


class SearchableContent(ABC):
    """Interface for searchable documents"""
    
    @abstractmethod
    def search(self, keyword: str) -> List[str]:
        pass


class TextDocument(Printable, Exportable):
    """Implements only the interfaces it needs"""
    
    def __init__(self, content: str):
        self.content = content
    
    def print_content(self) -> str:
        return self.content
    
    def export_to_file(self, filepath: str) -> bool:
        try:
            with open(filepath, 'w') as f:
                f.write(self.content)
            return True
        except Exception:
            return False


class PDFDocument(Printable, Exportable, SearchableContent):
    """Implements all interfaces as it supports all functionalities"""
    
    def __init__(self, content: str):
        self.content = content
    
    def print_content(self) -> str:
        return f"PDF Content: {self.content}"
    
    def export_to_file(self, filepath: str) -> bool:
        try:
            with open(filepath, 'w') as f:
                f.write(f"PDF Format\n{self.content}")
            return True
        except Exception:
            return False
    
    def search(self, keyword: str) -> List[str]:
        results = []
        for line in self.content.split('\n'):
            if keyword.lower() in line.lower():
                results.append(line)
        return results


# Example usage
def main():
    # Using SRP
    validator = DocumentValidator()
    storage = DocumentStorage()
    
    # Validate and store a document
    content = "This is a sample document"
    if validator.validate_format(content):
        storage.save("doc1", content)
    
    # Using ISP
    text_doc = TextDocument("Simple text document")
    pdf_doc = PDFDocument("PDF document with\nmultiple lines\nfor searching")
    
    # Text document can print and export
    print(text_doc.print_content())
    text_doc.export_to_file("text_doc.txt")
    
    # PDF document can print, export, and search
    print(pdf_doc.print_content())
    pdf_doc.export_to_file("pdf_doc.txt")
    search_results = pdf_doc.search("lines")
    print(f"Search results: {search_results}")


if __name__ == "__main__":
    main()