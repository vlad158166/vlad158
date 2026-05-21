from django.contrib import admin

from academics.models import Bid, Buyer, Category, Lot, Operator, Seller, SellerVerification


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "balance")
    search_fields = ("username", "email")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    search_fields = ("name", "slug")


@admin.register(Operator)
class OperatorAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email")
    search_fields = ("username", "email")


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "email", "phone")
    search_fields = ("first_name", "last_name", "email", "phone")


@admin.register(Lot)
class LotAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "status", "start_price", "seller", "approved_by_operator")
    list_filter = ("status",)
    search_fields = ("title", "description")


@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ("id", "amount", "bid_time", "buyer", "lot")


@admin.register(SellerVerification)
class SellerVerificationAdmin(admin.ModelAdmin):
    list_display = ("seller", "passport_number", "tax_id", "is_verified", "verified_at")
