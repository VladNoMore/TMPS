package domain.decorator;

public class MembershipDecorator extends Borrowing {
    private Borrowing borrowing;

    public MembershipDecorator(Borrowing borrowing) {
        this.borrowing = borrowing;
    }

    @Override
    public double getCost() {
        return borrowing.getCost() - 1.0; // Membership discount
    }
}