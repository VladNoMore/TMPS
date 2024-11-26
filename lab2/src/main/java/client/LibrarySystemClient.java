// LibrarySystemClient.java
package client;

import domain.decorator.*;

public class LibrarySystemClient {
    public static void main(String[] args) {
        LibraryFacade libraryFacade = new LibraryFacade();

        // Borrow a book
        libraryFacade.borrowBook("The Great Gatsby");

        // Pay a late fee
        libraryFacade.payLateFee(10.0);

        // Demonstrating Decorator
        System.out.println("\n--- Borrowing Costs ---");
        Borrowing basicBorrowing = new BasicBorrowing();
        System.out.println("Basic Borrowing Cost: $" + basicBorrowing.getCost());

        Borrowing membershipBorrowing = new MembershipDecorator(basicBorrowing);
        System.out.println("With Membership Discount: $" + membershipBorrowing.getCost());

        Borrowing lateFeeBorrowing = new LateFeeDecorator(membershipBorrowing);
        System.out.println("With Late Fee: $" + lateFeeBorrowing.getCost());
    }
}
