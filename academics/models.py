from django.db import models


class Buyer(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=50)
    email = models.EmailField(unique=True, max_length=100)
    balance = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = "buyer"
        managed = False
        ordering = ["id"]

    def __str__(self) -> str:
        return self.username


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    slug = models.SlugField(unique=True, max_length=50)

    class Meta:
        db_table = "category"
        managed = False
        ordering = ["id"]

    def __str__(self) -> str:
        return self.name


class Operator(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=50)
    email = models.EmailField(unique=True, max_length=100)

    class Meta:
        db_table = "operator"
        managed = False
        ordering = ["id"]

    def __str__(self) -> str:
        return self.username


class Seller(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = "seller"
        managed = False
        ordering = ["id"]

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class LotStatus(models.TextChoices):
    DRAFT = "draft", "Draft"
    ACTIVE = "active", "Active"
    SOLD = "sold", "Sold"
    CANCELLED = "cancelled", "Cancelled"


class Lot(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_price = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=LotStatus.choices,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(blank=True, null=True)
    seller = models.ForeignKey(
        Seller,
        models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="lots",
    )
    approved_by_operator = models.ForeignKey(
        Operator,
        models.DO_NOTHING,
        db_column="approved_by_operator_id",
        blank=True,
        null=True,
        related_name="approved_lots",
    )
    categories = models.ManyToManyField(
        Category,
        through="LotCategory",
        related_name="lots",
    )

    class Meta:
        db_table = "lot"
        managed = False
        ordering = ["id"]

    def __str__(self) -> str:
        return self.title


class LotCategory(models.Model):
    pk = models.CompositePrimaryKey("lot", "category")
    lot = models.ForeignKey(Lot, models.DO_NOTHING)
    category = models.ForeignKey(Category, models.DO_NOTHING)

    class Meta:
        db_table = "lot_category"
        managed = False


class Bid(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    bid_time = models.DateTimeField(blank=True, null=True)
    buyer = models.ForeignKey(Buyer, models.DO_NOTHING, related_name="bids")
    lot = models.ForeignKey(Lot, models.DO_NOTHING, related_name="bids")

    class Meta:
        db_table = "bid"
        managed = False
        ordering = ["id"]

    def __str__(self) -> str:
        return f"Bid #{self.id}"


class SellerVerification(models.Model):
    seller = models.OneToOneField(
        Seller,
        models.DO_NOTHING,
        primary_key=True,
        related_name="verification",
    )
    passport_number = models.CharField(max_length=20)
    tax_id = models.CharField(max_length=20)
    is_verified = models.BooleanField(blank=True, null=True)
    verified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "seller_verification"
        managed = False

    def __str__(self) -> str:
        return f"Verification for seller {self.seller_id}"
