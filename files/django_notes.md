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
### 2018-02-05
#### Models - Signals
- post_save and pre_save signals are built into django. 
- error_messages can be called as an argument of dictionary values in a model field that override the default error messages on form/model validation.
- help_text for a field will describe conditions required for a valid field
- verbose_name for a model field will change field label. 
```python
title = models.CharField(max_length=240, unique=True, error_messages={"unique":"this field must be unique"}, verbose_name="Post Title", help_text="Must be a unique value")
```
#### Models - Timestamp and DateTimeField
- `auto_now=True` is updated every time save is called.
- `auto_now_add=True` is when it was added to the database. once created, it does not get updated.

#### Models - ModelAdmin
- can be used to override the default admin display
- also in the ModelAdmin: you can run functions and display them even if they are not stored in the database. see `new_content` below
```python
# admin.py
class PostModelAdmin(admin.ModelAdmin):
  fields=[
    'title',
    'slug',
    'content',
    'publish',
    'publish_date',
    'active',
    'updated',
    'timestamp',
    'new_content',
  ]
  readonly_fields=[
    'updated',
    'timestamp',
    'new_content',
  ]
  
  def new_content(self, obj, *args, **kwargs):
    return str(obj.title)
  
  class Meta:
    model = PostModel

admin.site.register(PostModel, PostModelAdmin)
```
#### Models - Instance methods and properties.
- similar to the `new_content` above, you can create functions in the Model class and call them in to the admin.
- by adding `@Property` just before the method definition, you can use it as a dot object. `return str(instance.age)` vs `return str(instance.age())`
#### Model Managers
- can alter model defaults such as the objects call. 
- defined outside of the Model class but connected inside the model class through `objects = PostModelManager()`
#### Model QuerySet Methods
- can change the default queryset calls such as all()
- you can define your own qs defaults for frequently used calls.
- important for class based views since they use default query set calls
