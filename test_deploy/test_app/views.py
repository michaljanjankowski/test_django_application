from django.shortcuts import render
from django.views import View

# Create your views here.

class Hellow(View):
    def get(self,request):
        return render(request, "hellow.html")

    def post(self,request):
        pass