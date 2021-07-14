from decimal import Decimal

from django.conf import settings
from tienda.models import Producto

class Carro:

    def __init__(self, request):
        self.session = request.session
        carro = self.session.get(settings.CART_SESSION_ID)
        if settings.CART_SESSION_ID not in request.session:
            carro = self.session[settings.CART_SESSION_ID] = {}
        self.carro = carro
    
    def __len__(self):
        """
        Get the basket data and count the qty of items
        """
        return sum(item["quantity"] for item in self.carro.values())

    def get_subtotal_price(self):
        return sum(Decimal(item["price"]) * item["quantity"] for item in self.carro.values())