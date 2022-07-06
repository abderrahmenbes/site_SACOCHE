from django.shortcuts import render

from main.models import Order

# Create your views here.
def index(request):
    context = {
        'ord' : Order.objects.all(),
        'x': 1
    }
    return render(request,'page/index.html',context)