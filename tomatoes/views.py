import json
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from tomatoes.models import Movie, Favorite


def home(request):
    return render(request, 'tomatoes_base.html')


@csrf_exempt
def new_movie(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_movie = Movie.objects.create(
            title = data['title'],
            movie_id = data['movie_id'],
            critic_rating= data['critic_rating'],
            poster= data['poster'],
            mpaa_rating= data['mpaa_rating'],
            runtime= data['runtime'],
            year= data['year'],
            # audience_score =data['audience_score']
        )
        movie_info = { #this is for making json objects and we use json dumps instead of serialize for formatting issues.
            'title': new_movie.title,
            'movie_id': new_movie.movie_id,
            'critic_rating': new_movie.critic_rating,
            'poster': new_movie.poster,
            'mpaa_rating': new_movie.mpaa_rating,
            'runtime': new_movie.runtime,
            'year': new_movie.year,
            # 'audience_score': new_movie.audience_score

        }
        return HttpResponse(json.dumps(movie_info), content_type = 'application/json')
        #this goes back into success: function (movie_response) as movie_response


@csrf_exempt
def new_movie_html(request):
    if request.method == 'POST':
        data = json.loads(request.body) #data is equivalent to data:movieInfo
        new_movie = Movie.objects.create(
            title = data['title'],
            movie_id = data['movie_id'],
            critic_rating= data['critic_rating'],
            poster= data['poster'],
            mpaa_rating= data['mpaa_rating'],
            runtime= data['runtime'],
            year= data['year'],
            # audience_score =data['audience_score']

        )
        movie_info = {
            'title': new_movie.title,
            'movie_id': new_movie.movie_id,
            'critic_rating': new_movie.critic_rating,
            'poster': new_movie.poster,
            'mpaa_rating': new_movie.mpaa_rating,
            'runtime': new_movie.runtime,
            'year': new_movie.year,
            # 'audience_score': new_movie.audience_score,
            }
        return render_to_response('movie_template.html', movie_info)


@csrf_exempt
def search_movies(request):
    if request.method == "POST":
        movie_info_list = []

        data = json.loads(request.body)
        for x in data['searchResults']:
            new_movie = Movie.objects.create(
                title = x['title'],
                movie_id = x['movie_id'],
                critic_rating= x['critic_rating'],
                poster= x['poster'],
                mpaa_rating= x['mpaa_rating'],
                runtime= x['runtime'],
                year= x['year'],
                # audience_score =x['audience_score']
            )
            movie_info = {
                'title': new_movie.title,
                'movie_id': new_movie.movie_id,
                'critic_rating': new_movie.critic_rating,
                'poster': new_movie.poster,
                'mpaa_rating': new_movie.mpaa_rating,
                'runtime': new_movie.runtime,
                'year': new_movie.year,
                # 'audience_score': new_movie.audience_score,

            }
            movie_info_list.append(movie_info)
        return render_to_response('movie_template_search.html', {'movie_info_list': movie_info_list})


def tinder(request):
    return render(request, 'tinder.html')

@csrf_exempt
def new_favorite(request):
    if request.method == "POST":
        data = json.loads(request.body)
        new_favorite = Favorite.objects.create(
            title = data['title'],
            poster = data['poster'],
            identifier = data['identifier']
        )
        favorite_info = {
            'title': new_favorite.title,
            'poster': new_favorite.poster,
            'identifier': new_favorite.identifier,
        }

        return HttpResponse(json.dumps(favorite_info), content_type='application/json')

@csrf_exempt
def all_favorites(request):
    all_favs = Favorite.objects.all()
    favorites_list = []
    for fav in all_favs:
        favorites_list.append({
            'title': fav.title,
            'poster': fav.poster,
            'identifier': fav.identifier,
        })

    #return render_to_response("all_favorites.html", favorites_info)
    #^that's if you wanted to directly send to html instead of making json objects.
    #you would also have to make a favorites_info dictionary? for the template to have stuff to render. maybe stash stuff in an array?idk.
    return HttpResponse(json.dumps(favorites_list), content_type='application/json')


def theater(request):
    return render(request, "theater.html")
