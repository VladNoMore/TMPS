// LibraryFacade.java
package client;

import domain.data.LibraryDatabase;
import utilities.PaymentAdapter;

public class LibraryFacade {
    private LibraryDatabase libraryDatabase;
    private PaymentAdapter paymentAdapter;

    public LibraryFacade() {
        this.libraryDatabase = new LibraryDatabase();
        this.paymentAdapter = new PaymentAdapter();
    }

    public void borrowBook(String title) {
        System.out.println("Searching for the book: " + title);
        String book = libraryDatabase.getBook(title);
        if (book != null) {
            System.out.println("Borrowing book: " + book);
        } else {
            System.out.println("Book not available.");
        }
    }

    public void payLateFee(double fee) {
        if (paymentAdapter.processPayment(fee)) {
            System.out.println("Late fee paid successfully!");
        }
    }
}
