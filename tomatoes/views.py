import json
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from tomatoes.models import Movie


def home(request):
    return render(request, 'tomatoes_base.html')


@csrf_exempt
def new_movie(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_movie = Movie.objects.create(
            title=data['title'],
            release_year=data['release_year'],
            critic_rating=data['critic_rating'],
            poster=data['poster']
        )
        movie_info = {
            'title': new_movie.title,
            'release_year': new_movie.release_year,
            'critic_rating': new_movie.critic_rating,
            'poster': new_movie.poster

        }
        return HttpResponse(json.dumps(movie_info), content_type = 'application/json')
        #this goes back into success: function (movie_response) as movie_response


@csrf_exempt
def new_movie_html(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        neww_movie = Movie.objects.create(
            title = data['title'],
            release_year= data['release_year'],
            critic_rating= data['critic_rating'],
            poster= data['poster']
        )
        movie_info = {
            'title': neww_movie.title,
            'release_year': neww_movie.release_year,
            'critic_rating': neww_movie.critic_rating,
            'poster': neww_movie.poster
        }
        return render_to_response('movie_template.html', movie_info)