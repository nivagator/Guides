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
