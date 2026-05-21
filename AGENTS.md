# AGENTS.md

## Project Goal

Build a small Django REST API project for working with a university database.  
The project must reproduce the logic from the provided Express/MySQL lab example, but implemented with **Python + Django + Django REST Framework** instead of Node.js.

The final project should demonstrate:

- REST API basics.
- CRUD operations through HTTP.
- Integration with a database.
- Testing endpoints through Postman or Swagger.
- Import/export workflow using DBeaver and Excel.

Do not over-engineer this project. This is a lab-style educational project, not another startup pretending to reinvent university administration because apparently tables with students were not dramatic enough.

---

## Tech Stack

Use:

- Python 3.11+
- Django
- Django REST Framework
- SQLite by default for the simplest setup
- Optional MySQL support if the user wants to connect through DBeaver/MySQL
- DBeaver for inspecting/importing/exporting data
- Postman or Swagger/OpenAPI for API testing
- VSCode as the expected IDE

Avoid:

- Node.js
- Express
- JavaScript backend implementation
- Complex authentication unless explicitly requested
- Docker unless explicitly requested
- Unnecessary frontend work

---

## Expected Django Structure

Create a Django project with a simple structure similar to:

```text
university_api/
├── manage.py
├── university_api/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── academics/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── tests.py
│   └── migrations/
└── requirements.txt
```

Use the app name:

```text
academics
```

---

## Database Models

Implement at minimum these models:

### Student

Fields:

- `student_id`: auto-generated primary key
- `first_name`: string
- `last_name`: string
- `email`: unique email field

### Course

Fields:

- `course_id`: auto-generated primary key
- `course_name`: string
- `description`: text, optional
- `credits`: positive integer, optional

The Express example only shows `courses` and `students`, so keep the Django version focused on those entities.

---

## Required API Endpoints

Implement REST endpoints equivalent to the lab example.

### Courses

#### GET all courses

```http
GET /api/courses/
```

Expected result:

```json
[
  {
    "course_id": 1,
    "course_name": "Databases",
    "description": "Introduction to relational databases",
    "credits": 4
  }
]
```

### Students

#### GET all students

```http
GET /api/students/
```

#### POST create student

```http
POST /api/students/
Content-Type: application/json
```

Example body:

```json
{
  "first_name": "Olha",
  "last_name": "Kolodchak",
  "email": "olha@example.com"
}
```

Expected result:

```json
{
  "student_id": 1,
  "first_name": "Olha",
  "last_name": "Kolodchak",
  "email": "olha@example.com"
}
```

#### PUT update student

```http
PUT /api/students/1/
Content-Type: application/json
```

Example body:

```json
{
  "first_name": "Olha",
  "last_name": "Kolodchak",
  "email": "olha.updated@example.com"
}
```

#### DELETE student

```http
DELETE /api/students/1/
```

Expected result:

```http
204 No Content
```

---

## Implementation Requirements

Use Django REST Framework properly:

- Define models in `academics/models.py`.
- Define serializers in `academics/serializers.py`.
- Define API views or viewsets in `academics/views.py`.
- Register routes in `academics/urls.py`.
- Include app URLs inside `university_api/urls.py`.

Preferred implementation:

- Use `ModelSerializer`.
- Use `ModelViewSet`.
- Use `DefaultRouter`.

This gives clean CRUD automatically, because making students manually write every route forever is apparently how civilization tests patience.

---

## API Routing Example

The final API should expose:

```text
/api/courses/
/api/courses/<id>/
/api/students/
/api/students/<id>/
```

Use trailing slashes, because Django likes them and we do not need a holy war over URL punctuation.

---

## Setup Commands

The project should be runnable with commands similar to:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install django djangorestframework
pip freeze > requirements.txt
```

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Create admin user:

```bash
python manage.py createsuperuser
```

Run server:

```bash
python manage.py runserver
```

---

## Django Admin

Register both models in `academics/admin.py`:

- Student
- Course

The admin panel should allow manual creation, editing, and deletion of students and courses.

Expected admin URL:

```text
/admin/
```

---

## Optional Swagger/OpenAPI

If Swagger is requested, use `drf-spectacular`.

Install:

```bash
pip install drf-spectacular
```

Add schema endpoints:

```text
/api/schema/
/api/docs/
```

Do not add Swagger unless explicitly requested or unless the lab requires it in the final version.

---

## DBeaver Integration

For the simplest setup, use SQLite:

```text
db.sqlite3
```

DBeaver can connect directly to this SQLite database file.

Expected workflow:

1. Open DBeaver.
2. Create a new SQLite connection.
3. Select the project `db.sqlite3` file.
4. Inspect tables generated by Django.
5. Export table data to Excel/CSV.
6. Import new student records from Excel/CSV into the `academics_student` table.

Important:

- Django table names will likely be:
  - `academics_student`
  - `academics_course`
- If importing records manually, respect field names and required values.
- Do not manually break primary keys unless the assignment specifically wants a tiny database tragedy.

---

## Import/Export Requirements

The project documentation should explain:

### Export

Export data from DBeaver:

```text
DBeaver → right-click table → Export Data → CSV/XLSX
```

Use exported files for simple data analysis.

### Import

Import new student records:

```text
DBeaver → right-click table → Import Data → select CSV/XLSX → map columns → finish
```

Example student data:

```csv
first_name,last_name,email
Olha,Kolodchak,olha@example.com
Ivan,Petrenko,ivan.petrenko@example.com
Marta,Shevchenko,marta.shevchenko@example.com
```

---

## API Testing Requirements

Prepare examples for Postman.

### Test 1: Get courses

```http
GET http://127.0.0.1:8000/api/courses/
```

### Test 2: Create student

```http
POST http://127.0.0.1:8000/api/students/
Content-Type: application/json
```

Body:

```json
{
  "first_name": "Olha",
  "last_name": "Kolodchak",
  "email": "olha@example.com"
}
```

### Test 3: Update student

```http
PUT http://127.0.0.1:8000/api/students/1/
Content-Type: application/json
```

Body:

```json
{
  "first_name": "Olha",
  "last_name": "Kolodchak",
  "email": "olha.updated@example.com"
}
```

### Test 4: Delete student

```http
DELETE http://127.0.0.1:8000/api/students/1/
```

---

## Validation Rules

Implement basic validation:

- `email` must be unique.
- `first_name` cannot be empty.
- `last_name` cannot be empty.
- `course_name` cannot be empty.
- `credits`, if present, should be positive.

Django and DRF should handle most of this automatically through model fields and serializers.

---

## README Requirements

Create or update `README.md` with:

- Project description.
- Tech stack.
- Setup instructions.
- How to run migrations.
- How to start the server.
- API endpoint list.
- Postman testing examples.
- DBeaver import/export instructions.
- Short conclusions.
- Answers to control questions.

---

## Control Questions and Expected Answers

Include these in the README or a separate `docs/control-questions.md`.

### 1. Які HTTP-методи відповідають CRUD-операціям?

- Create: `POST`
- Read: `GET`
- Update: `PUT` or `PATCH`
- Delete: `DELETE`

### 2. Що таке REST API?

REST API is an interface that allows clients to work with server resources through standard HTTP methods and structured URLs.

### 3. Для чого потрібен Postman або Swagger?

They are used to test and document API endpoints without needing a frontend.

### 4. Як інтегрувати API з MySQL або SQLite?

In Django, the database connection is configured in `settings.py`. SQLite works by default. MySQL requires installing a driver and changing the `DATABASES` configuration.

### 5. Як перевірити роботу POST-запиту?

Send a request with JSON body through Postman or Swagger, then check the API response and verify that the new record appears in the database.

### 6. Які переваги REST API у порівнянні з прямими SQL-запитами?

REST API separates client logic from database logic, improves security, validates data, and gives controlled access to database operations.

### 7. Як імпортувати Excel-дані у базу даних через DBeaver?

Use DBeaver's import tool, select the Excel/CSV file, map columns to database fields, and run the import.

---

## Acceptance Criteria

The task is complete when:

- Django project is created.
- `academics` app exists.
- Student and Course models are implemented.
- Migrations run successfully.
- Admin panel works.
- REST API supports CRUD for students.
- REST API supports listing courses.
- API can be tested through Postman.
- Database can be inspected in DBeaver.
- Import/export instructions are documented.
- README contains conclusions and answers to control questions.

---

## Suggested Development Order

1. Create virtual environment.
2. Install Django and DRF.
3. Create Django project.
4. Create `academics` app.
5. Add app and DRF to `INSTALLED_APPS`.
6. Create models.
7. Run migrations.
8. Register models in admin.
9. Create serializers.
10. Create viewsets.
11. Configure URLs.
12. Test API manually.
13. Add sample data.
14. Document Postman requests.
15. Document DBeaver import/export workflow.
16. Add control question answers.

---

## Coding Style

Keep code simple, readable, and beginner-friendly.

Use clear names:

- `Student`
- `Course`
- `StudentSerializer`
- `CourseSerializer`
- `StudentViewSet`
- `CourseViewSet`

Avoid clever abstractions. Clever code in a lab project is how simple homework mutates into a debugging swamp.

---

## Notes for Coding Agents

When editing this repository:

- Prefer small, focused changes.
- Do not introduce frontend frameworks.
- Do not replace Django REST Framework with another API framework.
- Do not add authentication unless requested.
- Do not add Docker unless requested.
- Keep SQLite as the default database unless the user asks for MySQL.
- Keep endpoints close to the lab requirements.
- Update documentation whenever behavior changes.
- Make sure the project can run from a clean clone using `requirements.txt`.

Before finishing, verify:

```bash
python manage.py makemigrations --check
python manage.py migrate
python manage.py test
python manage.py runserver
```

If tests are not implemented yet, at least manually check the endpoints through the browser, Postman, or DRF browsable API.
