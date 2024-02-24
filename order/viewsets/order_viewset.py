from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import (
    BasicAuthentication,
    TokenAuthentication,
    SessionAuthentication,
)
from rest_framework.permissions import IsAuthenticated
from order.models import Order
from order.serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    authentication_classes = [
        BasicAuthentication,
        TokenAuthentication,
        SessionAuthentication,
    ]
    permission_classes = [IsAuthenticated]

    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by("id")

    """
    def get_queryset(self):
        return Order.objects.all()
    """
