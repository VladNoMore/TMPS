# Laboratory Work Nr.0 SOLID PRINCIPLES

**Course:** Tehnici și mecanisme de proiectare software  
**Author:** Pîslaru Vladislav  
**Group:** FAF-223

## Theory
SOLID represents five essential design principles that help create better software:
- Single responsibility principle (SRP) - a class should have only one reason to change
- Open-closed principle (OCP) - open for extension, closed for modification
- Liskov substitution principle - subtypes must be substitutable for their base types
- Interface segregation principle - clients shouldn't depend on methods they don't use
- Dependency inversion principle - depend on abstractions, not concretions

During this lab, I focused on understanding and implementing SRP and ISP in a real-world scenario.

## Objectives
- Implement 2 SOLID letters in a simple project
- Understand how these principles improve code quality
- Practice writing clean, maintainable code

## Implementation Description
For this laboratory work, I decided to create a simple document management system - something similar to what we might use for handling student assignments or course materials. I chose this because it's relatable to our university context and clearly shows how SOLID principles can improve real software.

### My Project Structure:

1. First, I created a Document Validator that only does validation (following SRP):
```python
class DocumentValidator:
    def validate_format(self, content: str) -> bool:
        # Makes sure document isn't empty and isn't too long
        return len(content.strip()) > 0 and len(content) < 1000
    
    def validate_metadata(self, title: str, author: str) -> bool:
        # Checks if we have valid title and author
        return bool(title.strip()) and bool(author.strip())
```

2. Then I made a separate Storage class for managing documents (also following SRP):
```python
class DocumentStorage:
    def __init__(self):
        self.documents = {}  # Using a simple dict for storage
    
    def save(self, doc_id: str, content: str) -> bool:
        # Stores document with timestamp
        if doc_id and content:
            self.documents[doc_id] = {
                'content': content,
                'timestamp': datetime.now()
            }
            return True
        return False
```

3. For ISP, I split document capabilities into small, focused interfaces:
```python
class Printable(ABC):
    @abstractmethod
    def print_content(self) -> str:
        pass

class Exportable(ABC):
    @abstractmethod
    def export_to_file(self, filepath: str) -> bool:
        pass

class SearchableContent(ABC):
    @abstractmethod
    def search(self, keyword: str) -> List[str]:
        pass
```

4. Finally, I created different document types that only implement what they need:
```python
class TextDocument(Printable, Exportable):
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

# PDFs need more functionality
class PDFDocument(Printable, Exportable, SearchableContent):
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
```

## Results
When I ran my implementation, here's the actual output I got:

```
Simple text document
PDF Content: PDF document with
multiple lines
for searching
Search results: ['multiple lines']
```

Let's break down what this output shows:

1. First line shows the TextDocument's print_content() working - it simply outputs the plain text
2. Next two lines show the PDFDocument's content with its special PDF formatting
3. Last line demonstrates the search functionality working in the PDFDocument, finding the line containing our search term "lines"

This output proves that:
- Both document types can successfully print their content (SRP working - printing responsibility is separate)
- The PDFDocument's search function works as intended (ISP working - only PDFs have search capability)
- Each class is doing exactly what it's supposed to do, no more and no less

When testing different features, I was pleased to see that:
- Text documents handled basic operations without any extra complexity
- PDF documents successfully implemented all their additional features
- The separation of responsibilities made it very clear what each part of the system was doing

This practical test confirms that my implementation of both SOLID principles is working as intended. The clean output and successful execution of different features for different document types shows that the separation of responsibilities (SRP) and interface segregation (ISP) are properly implemented.

## Conclusions
After completing this laboratory work, I better understand why SOLID principles are important:

1. Using SRP made my code much cleaner. Instead of one big class doing everything, I have smaller, focused classes that are easier to understand and modify. For example, when I wanted to add new validation rules, I only had to change the DocumentValidator class.

2. ISP helped me avoid bloated interfaces. My TextDocument doesn't need to implement search functionality it won't use, while PDFDocument can have all the features it needs. This makes the code more logical and prevents unnecessary complications.

The main things I learned:
- Breaking down functionality into focused classes makes code much easier to maintain
- Not every class needs every feature - it's better to have specific interfaces
- These principles really do make code more flexible and easier to change

If I were to expand this project, I could easily add new document types or features without breaking existing code - which is exactly what SOLID principles are meant to achieve.

## References
1. Class materials and lectures
2. SOLID Principles in Python: https://realpython.com/solid-principles-python/
3. Python Interface Segregation: https://www.pythontutorial.net/python-oop/python-interface-segregation-principle/
