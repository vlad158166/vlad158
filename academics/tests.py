from django.test import SimpleTestCase

from academics.models import Bid, Buyer, Category, Lot, LotStatus, Operator, Seller, SellerVerification
from academics.serializers import BidSerializer, BuyerSerializer, CategorySerializer, LotSerializer


class ModelMappingTests(SimpleTestCase):
    def test_models_point_to_original_tables(self) -> None:
        self.assertEqual(Buyer._meta.db_table, "buyer")
        self.assertEqual(Seller._meta.db_table, "seller")
        self.assertEqual(Category._meta.db_table, "category")
        self.assertEqual(Lot._meta.db_table, "lot")
        self.assertEqual(Bid._meta.db_table, "bid")
        self.assertEqual(Operator._meta.db_table, "operator")
        self.assertEqual(SellerVerification._meta.db_table, "seller_verification")

    def test_models_are_unmanaged(self) -> None:
        self.assertFalse(Buyer._meta.managed)
        self.assertFalse(Lot._meta.managed)
        self.assertFalse(Bid._meta.managed)

    def test_lot_status_choices_match_database_enum(self) -> None:
        self.assertEqual(
            [choice for choice, _label in LotStatus.choices],
            ["draft", "active", "sold", "cancelled"],
        )


class SerializerShapeTests(SimpleTestCase):
    def test_lot_serializer_fields_match_backend_contract(self) -> None:
        serializer = LotSerializer()
        self.assertEqual(
            set(serializer.fields.keys()),
            {
                "id",
                "title",
                "description",
                "start_price",
                "status",
                "created_at",
                "seller",
                "approved_by_operator",
                "categories",
            },
        )

    def test_simple_serializers_expose_key_fields(self) -> None:
        self.assertEqual(set(BuyerSerializer().fields.keys()), {"id", "username", "email", "balance"})
        self.assertEqual(set(CategorySerializer().fields.keys()), {"id", "name", "slug"})
        self.assertEqual(set(BidSerializer().fields.keys()), {"id", "amount", "bid_time", "buyer", "lot"})
