# Conference-Room-Reservation-App
a Django Conference room manager

- add SECRET_KEY in to your local_settings.py file. Use this command to generate one:
```
python manage.py shell -c 'from django.core.management import utils; print(utils.get_random_secret_key())'
```