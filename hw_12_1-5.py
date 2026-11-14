from abc import ABC, abstractmethod


class Payment(ABC):
    """Abstract interface of a payment."""

    @abstractmethod
    def get_amount(self) -> int:
        """Get the payment amount.

        Args:
            None.

        Returns:
            int: The payment amount in UAH.
        """

    @abstractmethod
    def get_description(self) -> str:
        """Get the payment description.

        Args:
            None.

        Returns:
            str: The text description of the payment.
        """

    @abstractmethod
    def process(self) -> str:
        """Process the payment.

        Args:
            None.

        Returns:
            str: The description of the performed operation.
        """


class BasicPayment(Payment):
    """Basic payment with a fixed amount of 1000 UAH."""

    def get_amount(self) -> int:
        """Get the payment amount.

        Args:
            None.

        Returns:
            int: The payment amount (1000 UAH).
        """
        return 1000

    def get_description(self) -> str:
        """Get the payment description.

        Args:
            None.

        Returns:
            str: The description of the basic payment.
        """
        return "Basic Payment"

    def process(self) -> str:
        """Process the basic payment.

        Args:
            None.

        Returns:
            str: The description of the performed operation.
        """
        return "Basic Payment"


class PaymentDecorator(Payment):
    """Base decorator of a payment.

    Stores a reference to the wrapped payment and delegates all calls to it.
    """

    def __init__(self, payment: Payment) -> None:
        """Create a decorator.

        Args:
            payment (Payment): The payment or decorator to wrap.

        Returns:
            None.
        """
        self._payment = payment

    def get_amount(self) -> int:
        """Get the amount from the wrapped payment.

        Args:
            None.

        Returns:
            int: The amount of the wrapped payment.
        """
        return self._payment.get_amount()

    def get_description(self) -> str:
        """Get the description from the wrapped payment.

        Args:
            None.

        Returns:
            str: The description of the wrapped payment.
        """
        return self._payment.get_description()

    def process(self) -> str:
        """Process the wrapped payment.

        Args:
            None.

        Returns:
            str: The result of processing the wrapped payment.
        """
        return self._payment.process()


class CommissionDecorator(PaymentDecorator):
    """Adds a 2% commission to the payment amount."""

    def get_amount(self) -> int:
        """Get the amount including the commission.

        Args:
            None.

        Returns:
            int: The wrapped amount increased by 2%.
        """
        return int(self._payment.get_amount() * 1.02)

    def get_description(self) -> str:
        """Get the description with the commission note.

        Args:
            None.

        Returns:
            str: The wrapped description with ", with commission" appended.
        """
        return f"{self._payment.get_description()}, with commission"

    def process(self) -> str:
        """Process the payment and add the commission info.

        Args:
            None.

        Returns:
            str: The wrapped result with ", adding commission" appended.
        """
        return f"{self._payment.process()}, adding commission"


class TaxDecorator(PaymentDecorator):
    """Adds a 5% tax to the payment amount."""

    def get_amount(self) -> int:
        """Get the amount including the tax.

        Args:
            None.

        Returns:
            int: The wrapped amount increased by 5%.
        """
        return int(self._payment.get_amount() * 1.05)

    def get_description(self) -> str:
        """Get the description with the tax note.

        Args:
            None.

        Returns:
            str: The wrapped description with ", with tax" appended.
        """
        return f"{self._payment.get_description()}, with tax"

    def process(self) -> str:
        """Process the payment and add the tax info.

        Args:
            None.

        Returns:
            str: The wrapped result with ", adding tax" appended.
        """
        return f"{self._payment.process()}, adding tax"


class InsuranceDecorator(PaymentDecorator):
    """Adds a fixed insurance cost of 20 UAH to the payment amount."""

    def get_amount(self) -> int:
        """Get the amount including the insurance.

        Args:
            None.

        Returns:
            int: The wrapped amount increased by 20 UAH.
        """
        return int(self._payment.get_amount() + 20)

    def get_description(self) -> str:
        """Get the description with the insurance note.

        Args:
            None.

        Returns:
            str: The wrapped description with ", with insurance" appended.
        """
        return f"{self._payment.get_description()}, with insurance"

    def process(self) -> str:
        """Process the payment and add the insurance info.

        Args:
            None.

        Returns:
            str: The wrapped result with ", adding insurance" appended.
        """
        return f"{self._payment.process()}, adding insurance"


class LoggingDecorator(PaymentDecorator):
    """Logs the payment processing without changing amount or description."""

    def get_amount(self) -> int:
        """Get the amount of the wrapped payment.

        Args:
            None.

        Returns:
            int: The unchanged amount of the wrapped payment.
        """
        return int(self._payment.get_amount())

    def get_description(self) -> str:
        """Get the description of the wrapped payment.

        Args:
            None.

        Returns:
            str: The unchanged description of the wrapped payment.
        """
        return self._payment.get_description()

    def process(self) -> str:
        """Process the payment and wrap the result with log messages.

        Args:
            None.

        Returns:
            str: The wrapped result surrounded by start and end log messages.
        """
        return f"Start logging, {self._payment.process()}, logging sucsesfully"


class NotificationDecorator(PaymentDecorator):
    """Simulates sending a notification without changing amount or description."""

    def get_amount(self) -> int:
        """Get the amount of the wrapped payment.

        Args:
            None.

        Returns:
            int: The unchanged amount of the wrapped payment.
        """
        return int(self._payment.get_amount())

    def get_description(self) -> str:
        """Get the description of the wrapped payment.

        Args:
            None.

        Returns:
            str: The unchanged description of the wrapped payment.
        """
        return self._payment.get_description()

    def process(self) -> str:
        """Process the payment and add the notification message.

        Args:
            None.

        Returns:
            str: The wrapped result with the success notification appended.
        """
        return f"{self._payment.process()}, Payment succsesfully done"


pay1: Payment = BasicPayment()
print(pay1.get_amount())
print(pay1.get_description())
print(pay1.process())

pay1 = CommissionDecorator(pay1)
print(pay1.get_amount())
print(pay1.get_description())
print(pay1.process())

pay1 = TaxDecorator(pay1)
print(pay1.get_amount())
print(pay1.get_description())
print(pay1.process())

pay1 = InsuranceDecorator(pay1)
print(pay1.get_amount())
print(pay1.get_description())
print(pay1.process())

pay1 = LoggingDecorator(pay1)
print(pay1.get_amount())
print(pay1.get_description())
print(pay1.process())

pay1 = NotificationDecorator(pay1)
print(pay1.get_amount())
print(pay1.get_description())
print(pay1.process())
