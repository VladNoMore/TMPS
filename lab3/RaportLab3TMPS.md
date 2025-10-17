
# Laboratory Work #3 - Structural Design Patterns

**Author:** Pîslaru Vladislav  
**Group:** FAF-223  
**Course:** Design Patterns & Software Systems Design  

## Project Description
This project implements a **Library Management System** using **Structural Design Patterns**. The goal is to manage book borrowing and late fee payments efficiently while providing flexibility and maintainability through the use of design patterns.

## Design Patterns Used

### 1. Adapter Pattern
- **Purpose**: Integrates a third-party payment system for processing late fees.  
- **Usage**: Adapts the interface of the `ThirdPartyPaymentAPI` to the `PaymentService` interface used by the system.  
- **Implementation**: The `PaymentAdapter` class acts as a bridge, converting `processPayment()` calls into calls to the third-party API.  
- **Advantage**: Enables seamless integration of external libraries or services without modifying existing code.  

---

### 2. Facade Pattern
- **Purpose**: Simplifies interactions with the library system by providing a unified interface.  
- **Usage**: Combines borrowing and payment operations into a single `LibraryFacade` class for easy client interaction.  
- **Implementation**: The `LibraryFacade` class handles book lookups, borrowing, and fee payments internally, hiding the complexity from the client.  
- **Advantage**: Reduces system complexity and improves usability by encapsulating the interactions between subsystems.  

---

### 3. Decorator Pattern
- **Purpose**: Adds additional features to the book borrowing process dynamically, such as discounts or late fees.  
- **Usage**: Decorates the base `Borrowing` object with features like `MembershipDiscount` and `LateFee`.  
- **Implementation**: `MembershipDecorator` and `LateFeeDecorator` classes extend the functionality of `Borrowing` without altering the base class.  
- **Advantage**: Provides a flexible way to extend behavior without modifying existing code.

---

## Project Structure
```
library-management-system/
│
├── src/
│   ├── client/
│   │   ├── LibrarySystemClient.java
│   │   └── LibraryFacade.java
│   ├── domain/
│   │   ├── models/
│   │   │   ├── Book.java
│   │   │   └── BorrowedBook.java
│   │   ├── decorator/
│   │   │   ├── Borrowing.java
│   │   │   ├── BasicBorrowing.java
│   │   │   ├── LateFeeDecorator.java
│   │   │   └── MembershipDecorator.java
│   │   └── data/
│   │       └── LibraryDatabase.java
│   └── utilities/
│       ├── PaymentAdapter.java
│       ├── PaymentService.java
│       └── ThirdPartyPaymentAPI.java
└── README.md
```

---

## Output
### Example Interaction:
```plaintext
Searching for the book: The Great Gatsby
Borrowing book: The Great Gatsby

--- Borrowing Costs ---
Basic Borrowing Cost: $5.0
With Membership Discount: $4.0
With Late Fee: $6.0

Processing payment of $6.0 using third-party API...
Late fee paid successfully!
```

---

## Conclusions
- **Adapter Pattern**: Simplified the integration of an external payment service, making the system flexible for future upgrades.  
- **Facade Pattern**: Improved usability by abstracting the complexity of internal operations, ensuring a clean and intuitive client interaction.  
- **Decorator Pattern**: Enabled the dynamic addition of features to the borrowing system without modifying the core logic.  
- **Overall Impact**: The use of Structural Design Patterns enhanced the maintainability, scalability, and readability of the system, making it a robust solution for managing a library.  

---
