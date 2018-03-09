# Django Notes

### 2018-01-25
- preferable to write class based views vs function based views using shortcut called render
- in views, you import the associated model(s) and create a queryset
- most basic queryset is `[model name].objects.all()`
- to use templates in views, you use the `render` shortcut from `django.shortcuts`
  - `return render(request, '[template path]', {context dict})`
  - `template_path = "[app name]/[template name].html"`
- how does template path work?
  - django looks in the apps for a templates subfolder called 'templates'
  -  best practice is the structure `/[app]/templates/[app name]/[template name].html`
- context - python dictionary. key-value pairs can be called using liquid tags in html templates
- user auth - there's a user associated to the request. `print(request.user)`
```python
if request.user.is_authenticated:
  print("logged in")
else:
  print("not logged in")
```
- user auth - using a decorator
  - `from django.contrib.auth.decorators import login_required`
  ```python
  @login_required(login_url='/login') #login_url is not required. default is /account/login
  def post_model_list_view(request):
    ...
  ```
- CRU**D** - Detail views qs will pull details on one object.
- detail qs basic format `obj = [model name].objects.get(id=[id])`
- to account for objects that dont exist, use the `get_object_or_404` shortcut
  - `from django.shortcuts import get_object_or_404`
```python
  obj = get_object_or_404([model name], [query parameters - i.e., id=1])    
```
  - can also use a try block
  - can also use an if not exists clause on the filtered queryset
- create url styles
  - `<a href="/blog/{{ object.id}}">{{ object.title }}</a>`
  - `<a href='{% url "blog:detail" id=object.id %}'>{{ object.title }}</a>`
  - `<a href="{{ object.get_absolute_url }}">{{ object.title }}</a>`
- for namespace url generation, django 2.0 requires the app url.py files to have a defined `app_name`
```python
from django.urls import path, include

app_name='[app name]'

urlpatterns = [
...
]
```
- forms - using liquid tags to call form in a template
  - `{{ form.as_p }}` will wrap the form in `<p>` tags


### 2018-01-31
#### Models
- in admin.py, import model and add it to the admin  
  - `from .models import [ModelName]`
  - `admin.site.Register([ModelName])`
- each field in a model can be given a `verbose_name`. this will be the field name displayed in the admin (`verbose_name='[Field Label]'`)
- in the model Meta class, you can define `verbose_name` and `verbose_name_plural`. this will control the displayed headers in the admin for the entire model
- model field choices - how to control fields that should have a finite set of selectable choices (drop down)
  - above the model ([or in the model itself](https://docs.djangoproject.com/en/2.0/ref/models/fields/#choices)), define the choices as and array of tuples.
  - add `choices=` to the field arguments
  - first value of each tuple is what is stored in the datbase, the second is the label in the admin or form.
- Object unicode name - needed to give the model a label in the admin?
  - from within the model itself:
  ```python
  def __str__(self):
    return "Something"
    # OR
    return self.[field name] # something like title or name
  ```
- smart_text `from django.utils.encoding import smart_text`
  - helps fields render correctly if other languages or encodings are used.

### 2018-02-01
#### Models
- overwriting the save method. special actions that can be taken when records are saved.
```python
# an example of the default save method.
def save(self, *args, **kwargs):
  super(PostModel, self).save(*args, **kwargs)

# other actions can be taken on save.
def save(self, *args, **kwargs):
  print(self.title) #example of what can be printed
  #a bad idea in the save method
  self.title = "a new title" #title will always be "a new title"
  # example of practical application
  if not self.slug and self.title:
      self.slug = slugify(self.title)
  super(PostModel, self).save(*args, **kwargs)
```
- slugify `from django.utils.text import slugify`

- admin.py ModelAdmin used to display fields in the admin list
```python
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','timestamp')

admin.site.register(Contact, ContactAdmin)
```