package client;

import domain.models.LibrarySystem;
import domain.observer.LibraryUser;

public class LibrarySystemClient {
    public static void main(String[] args) {
        // Create library system and users
        LibrarySystem librarySystem = new LibrarySystem();
        LibraryUser alice = new LibraryUser("Alice");
        LibraryUser bob = new LibraryUser("Bob");

        // Add users as observers
        librarySystem.addObserver(alice);
        librarySystem.addObserver(bob);

        // Example actions triggering notifications
        System.out.println("Searching for the book: The Great Gatsby");
        librarySystem.setBookStatus("Searching for the book: The Great Gatsby");

        System.out.println("\nBorrowing book: The Great Gatsby");
        librarySystem.setBookStatus("The Great Gatsby has been borrowed.");

        System.out.println("\nProcessing payment via Third-Party API...");
        System.out.println("Late fee paid successfully!");

        // Example borrowing cost output
        System.out.println("\n--- Borrowing Costs ---");
        System.out.println("Basic Borrowing Cost: $5.0");
        System.out.println("With Membership Discount: $4.0");
        System.out.println("With Late Fee: $6.0");
    }
}
