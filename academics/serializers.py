from rest_framework import serializers

from academics.models import Bid, Buyer, Category, Lot, Operator, Seller, SellerVerification


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = ("id", "username", "email", "balance")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "slug")


class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operator
        fields = ("id", "username", "email")


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ("id", "first_name", "last_name", "email", "phone")


class SellerVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerVerification
        fields = ("seller", "passport_number", "tax_id", "is_verified", "verified_at")


class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = ("id", "amount", "bid_time", "buyer", "lot")


class LotSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Lot
        fields = (
            "id",
            "title",
            "description",
            "start_price",
            "status",
            "created_at",
            "seller",
            "approved_by_operator",
            "categories",
        )
