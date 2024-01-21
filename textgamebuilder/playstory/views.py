from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    context = {}
    return render(request, "home.html", context)