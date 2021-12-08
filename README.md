# Django-ORM
Practice code while learning Django-ORM

### Accessing shell
```Shell
$ python manage.py shell
```
### Creating objects
```Python
>>> from weblog.models import Blog
>>> b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
>>> b.save()
```