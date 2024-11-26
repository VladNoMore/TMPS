package domain.decorator;

public class LateFeeDecorator extends Borrowing {
    private Borrowing borrowing;

    public LateFeeDecorator(Borrowing borrowing) {
        this.borrowing = borrowing;
    }

    @Override
    public double getCost() {
        return borrowing.getCost() + 2.0; // Late fee
    }
}