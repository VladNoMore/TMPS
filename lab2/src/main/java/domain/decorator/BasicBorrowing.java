package domain.decorator;

public class BasicBorrowing extends Borrowing {
    @Override
    public double getCost() {
        return 5.0; // Base borrowing cost
    }
}
