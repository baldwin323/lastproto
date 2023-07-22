```python
from django.shortcuts import render
from .models import MyModel

def index(request):
    data = MyModel.objects.all()
    return render(request, 'app/index.html', {'data': data})
```