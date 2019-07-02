
# Create your views here.
from django .template import loader
from django .shortcuts import render

from django.http import HttpResponse

from .models import Movie


def index(requets):

   all_movies =Movie.objects.all()

   context ={

      'all_movies': all_movies,
   }

   return render(requets,'Home/index.html',context)


'''def index(request):

   all_movies = Movie.objects.all()

   template =loader.get_template('Home/index.html')

   context ={

      'all_movies': all_movies
   }
   return HttpResponse(template.render(context,request))'''

'''for b in all_movies:
      url ='/Home/' + str(b.id) + '/'

      html = '<a href =" '+ url + ' ">' + b.actor_movie + '</a>'''





def detail(request,Home_id):

      return HttpResponse("<h1> welcome in youplus QA Team:" + str(Home_id) + "</h1>")


def page_view_count(requests,page_id):
   return HttpResponse("<h1> Page View count:"+str(page_id)+ "</h1>")


def video_view_count(requests,video_id):
   return HttpResponse("<h1> Video View count:" + str(video_id) + "</h1>")


'''def ad_impression(requests,ad_im):

   return HttpResponse("<h1> Ad_impression:" + str(ad_im) + "</h1>")'''

def ad_impression(requests,a,b):

   return HttpResponse("<h1>Addition" +str(a+b) +"</h1>")




