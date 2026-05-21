TEST


# Auction Backend

Django REST Framework backend mapped onto the original PostgreSQL `auction` database. The ORM now reflects the real existing tables instead of the earlier lab placeholder models.

## Database target

The project connects through `.env` and now targets:

```env
URL = jdbc:postgresql://localhost:5432/auction
user = postgres
Password = your_password_here
Port = 5432
```

The backend reads this JDBC-style format directly from `settings.py`.

## Original database schema

The mapped PostgreSQL tables are:

- `buyer`
- `seller`
- `operator`
- `category`
- `lot`
- `bid`
- `lot_category`
- `seller_verification`

These models are intentionally `managed = False` so Django works with the original tables instead of trying to recreate or overwrite them.

## API endpoints

- `GET/POST /api/buyers/`
- `GET/PUT/PATCH/DELETE /api/buyers/<id>/`
- `GET/POST /api/sellers/`
- `GET/PUT/PATCH/DELETE /api/sellers/<id>/`
- `GET/POST /api/operators/`
- `GET/PUT/PATCH/DELETE /api/operators/<id>/`
- `GET/POST /api/categories/`
- `GET/PUT/PATCH/DELETE /api/categories/<id>/`
- `GET/POST /api/lots/`
- `GET/PUT/PATCH/DELETE /api/lots/<id>/`
- `GET/POST /api/bids/`
- `GET/PUT/PATCH/DELETE /api/bids/<id>/`
- `GET/POST /api/seller-verifications/`
- `GET/PUT/PATCH/DELETE /api/seller-verifications/<seller_id>/`

## ORM mapping notes

- `Lot.status` matches the existing PostgreSQL enum values:
  - `draft`
  - `active`
  - `sold`
  - `cancelled`
- `Lot.seller` maps to `seller_id`
- `Lot.approved_by_operator` maps to `approved_by_operator_id`
- `SellerVerification` is a one-to-one extension of `Seller`
- `Lot.categories` is backed by the existing `lot_category` join table

## Running the backend

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py check
python manage.py runserver
```

Use `/admin/` for Django admin and `/api/` for the REST API.

## Verification

The project was verified with:

```bash
python manage.py check
python manage.py test
```

The database inspection also confirmed that the populated data lives in the `auction` database, not in the default `postgres` database.
