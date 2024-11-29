// src/main/java/domain/observer/LibraryUser.java
package domain.observer;

public class LibraryUser implements Observer {
    private String name;

    public LibraryUser(String name) {
        this.name = name;
    }

    @Override
    public void update(String message) {
        System.out.println(name + " received update: " + message);
    }
}
