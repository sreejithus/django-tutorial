from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from . models import Person
from . models import Movie


# Create your views here.
# def firstpage(request):
#          return HttpResponse('First page')

# def secondpage(request):
#          return HttpResponse('Second page')


# class First(View):
#     def get(self,request):
#           return HttpResponse('')

# class Second(View):
#     def get(self,request):
#           return HttpResponse('Second page')



class First(View):
    data=[{
          'name':"sreejith",
          'age':21,
          'place': "tvm"
    },
    {
          'name':"joyal",
          'age':22,
          'place':"ekm"
    }
    ]

    context={'data':data}
    def get(self,request):
           return render(request,'first.html',self.context)


class Second(View):
     data = Person.objects.all()
     data={'data':data}
     def get(self,request):
           return render(request,'second.html',context=self.data)


class Movie_list(View):
       def get(self,request):
             data= Movie.objects.all()
             context={'data':data}
             return render(request,'movielist.html',context)

class Add_movie(View):
       def get(self,request):
             return render(request,'addmovie.html')
       def post(self,request):
             print(request.POST)
             data= request.POST

             moviename= data['movie_name']
             Director = data['director']
             year = data['year']
             m= Movie.objects.create(movie_name=moviename,director=Director,year=year)
             m.save()
             return render(request,'addmovie.html')
      