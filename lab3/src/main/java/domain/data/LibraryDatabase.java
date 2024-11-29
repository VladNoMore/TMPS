// LibraryDatabase.java
package domain.data;

import java.util.Arrays;
import java.util.List;

public class LibraryDatabase {
    private List<String> availableBooks = Arrays.asList("The Great Gatsby", "Moby Dick", "1984", "To Kill a Mockingbird");

    public String getBook(String title) {
        // Search for the book in the database
        if (availableBooks.contains(title)) {
            return title;  // Book is available
        } else {
            return null;  // Book is not available
        }
    }
}
