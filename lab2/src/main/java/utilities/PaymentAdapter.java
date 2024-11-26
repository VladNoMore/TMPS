// PaymentAdapter.java
package utilities;

public class PaymentAdapter implements PaymentService {
    private ThirdPartyPaymentAPI paymentAPI;

    public PaymentAdapter() {
        this.paymentAPI = new ThirdPartyPaymentAPI();
    }

    @Override
    public boolean processPayment(double amount) {
        return paymentAPI.pay(amount);
    }
}
