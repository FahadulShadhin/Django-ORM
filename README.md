# Django-ORM
Practice code while learning Django-ORM

### Accessing shell
```Shell
$ python manage.py shell
```
### Import the model
```Pyhton
>>> from <appname>.models import <modelname>
```

### Creating objects
```Python
>>> from weblog.models import Blog
>>> b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
>>> b.save()
```

### Retrieving all objects --> .all()
```Python
>>> q = Blog.objects.all()
>>> q
<QuerySet [<Blog: Beatles Blog>, <Blog: Django Blog>, <Blog: Python Blog>]>
```

### Retrieving single object based on matched attribute --> .get(attribute='value') 
```Python
>>> q = Blog.objects.get(name='Django Blog')
>>> q
<Blog: Django Blog>
>>> q = Blog.objects.get(tagline='All the latest Beatles news.')
>>> q
<Blog: Beatles Blog>
```

### Return all items from a table that match a particular attribute value --> .filter(attribute='value')

```Python
>>> q = Blog.objects.filter(name__contains='Blog')
>>> q
<QuerySet [<Blog: Beatles Blog>, <Blog: Django Blog>, <Blog: Python Blog>]>
>>> q = Blog.objects.filter(name__startswith='Python')
>>> q
<QuerySet [<Blog: Python Blog>]>

############################################################
>>> ModelName.objects.filter(attribute='value')
>>> ModelName.objects.filter(attribute__startswith='value')
>>> ModelName.objects.filter(attribute__contains='value')
>>> ModelName.objects.filter(attribute__icontains='value')
>>> ModelName.objects.filter(attribute__gt='value')
>>> ModelName.objects.filter(attribute__gte='value')
>>> ModelName.objects.filter(attribute__lt='value')
>>> ModelName.objects.filter(attribute__lte='value')
############################################################
```

### OR Query
```Python
>>> q = Blog.objects.filter(name__startswith='Python') | Blog.objects.filter(name__startswith='Django')
>>> q
<QuerySet [<Blog: Django Blog>, <Blog: Python Blog>]>
```