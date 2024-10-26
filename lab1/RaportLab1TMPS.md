# Laboratory Work #1 - Creational Design Patterns

**Author:** Pîslaru Vladislav  
**Group:** FAF-223  
**Course:** Design Patterns & Software Systems Design

## Project Description
This project is all about building a **Game Character Creation System** using Creational Design Patterns. The goal is to make it easy to create and manage game characters with various attributes and classes, using patterns that bring flexibility and clarity to the code

## Design Patterns Used

### 1. Builder Pattern
- **Purpose**: Builds complex Character objects step-by-step
- **Usage**: Allows creating characters with custom stats and attributes
- **Implementation**: `CharacterBuilder` class provides a fluent interface, making it easy to construct characters
- **Advantage**: Makes character creation process more readable and manageable

### 2. Prototype Pattern
- **Purpose**: Creates new characters by copying existing ones.
- **Usage**: Provides template characters (Warrior, Mage) that can be cloned and customized
- **Implementation**: `CharacterPrototype` abstract class with concrete implementations for each type
- **Advantage**: Efficient way to create similar characters without repeating initialization code

### 3. Singleton Pattern
- **Purpose**: Ensures a single point of access for character management
- **Usage**: Maintains a global list of all created characters
- **Implementation**: `CharacterRegistry` class with private constructor and instance control
- **Advantage**: Keeps character management consistent and avoids duplicate registries

## Project Structure
```
TMPS/
└── lab1/
    ├── character.py    # Main code
    └── RaportLab1TMPS.md       # Documentation
```

## Output
```
Created using Builder: Conan - Level 1 Warrior
Created using Prototype: Thor - Level 1 Warrior
Created using Prototype: Gandalf - Level 1 Mage

Registered characters: ['Conan', 'Thor', 'Gandalf']
Singleton check - Same characters in new instance: ['Conan', 'Thor', 'Gandalf']
```

## Conclusions
- **Builder Pattern**: Enhanced flexibility and readability, making character creation straightforward and adaptable
- **Prototype Pattern**: Made creating similar characters efficient and seamless, saving time and avoiding redundancy
- **Singleton Pattern**: Ensured consistent character management across the system by centralizing the registry
- **Overall Impact**: These patterns combined to build a system that's not only maintainable and extensible but also easy to understand and expand upon



