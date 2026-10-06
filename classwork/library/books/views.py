from django.shortcuts import render
from django.views import View
from . models import Book
# Create your views here.

class Home(View):
    def get(self,request):
         return render(request,'home.html')

class Add_book(View):
       def get(self,request):
            return render(request,'addbook.html')
       def post(self,request):
            data = request.POST
            Title = data['title']
            Author = data['author']
            Price = data['price']
            Language= data['language']
            Pages = data['pages']

            d = Book.objects.create(title=Title,author=Author,price=Price,language=Language,pages=Pages)
            d.save()
            return render(request,'addbook.html')
class View_book(View):
           def get(self,request):
                 data  = Book.objects.all()
                 data = {
                       'data':data
                 }

                 return render(request,'viewbooks.html',context=data)