package domain.models;

import domain.observer.LibraryUser;
import java.util.ArrayList;
import java.util.List;

public class LibrarySystem {
    private List<LibraryUser> observers = new ArrayList<>();

    public void addObserver(LibraryUser user) {
        observers.add(user);
    }

    public void removeObserver(LibraryUser user) {
        observers.remove(user);
    }

    public void setBookStatus(String status) {
        notifyObservers(status);
    }

    private void notifyObservers(String status) {
        for (LibraryUser observer : observers) {
            observer.update(status);
        }
    }
}
