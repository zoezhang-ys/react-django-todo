
- create db
    - `python manage.py makemigrations test`
	- `python manage.py migrate`
- create admin (TODO: integrate with LDAP)
    - `python manage.py createsuperuser`
- start test server
    - `python manage.py runserver 8000`
- Visit `localhost:8000/admin/` 