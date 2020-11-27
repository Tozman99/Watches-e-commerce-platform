from django.dispatch import Signal

order_creation = Signal(providing_args=["user", "order"])