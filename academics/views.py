from rest_framework import viewsets

from academics.models import Bid, Buyer, Category, Lot, Operator, Seller, SellerVerification
from academics.serializers import (
    BidSerializer,
    BuyerSerializer,
    CategorySerializer,
    LotSerializer,
    OperatorSerializer,
    SellerSerializer,
    SellerVerificationSerializer,
)


class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class OperatorViewSet(viewsets.ModelViewSet):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer


class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class LotViewSet(viewsets.ModelViewSet):
    queryset = Lot.objects.all().prefetch_related("categories")
    serializer_class = LotSerializer


class BidViewSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer


class SellerVerificationViewSet(viewsets.ModelViewSet):
    queryset = SellerVerification.objects.select_related("seller").all()
    serializer_class = SellerVerificationSerializer
