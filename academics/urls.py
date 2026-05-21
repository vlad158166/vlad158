from rest_framework.routers import DefaultRouter

from academics.views import (
    BidViewSet,
    BuyerViewSet,
    CategoryViewSet,
    LotViewSet,
    OperatorViewSet,
    SellerVerificationViewSet,
    SellerViewSet,
)

router = DefaultRouter()
router.register("buyers", BuyerViewSet, basename="buyer")
router.register("categories", CategoryViewSet, basename="category")
router.register("operators", OperatorViewSet, basename="operator")
router.register("sellers", SellerViewSet, basename="seller")
router.register("lots", LotViewSet, basename="lot")
router.register("bids", BidViewSet, basename="bid")
router.register("seller-verifications", SellerVerificationViewSet, basename="seller-verification")

urlpatterns = router.urls
