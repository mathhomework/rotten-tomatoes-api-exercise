from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'tomatoes.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'new_movie/$', 'tomatoes.views.new_movie', name = 'new_movie'),
    url(r'new_movie_html/$', 'tomatoes.views.new_movie_html', name = 'new_movie_html'),
    url(r'search_movies/$', 'tomatoes.views.search_movies', name= 'search_movies'),
    url(r'tinder/$', 'tomatoes.views.tinder', name='tinder'),
    url(r'new_favorite/$', 'tomatoes.views.new_favorite', name='new_favorite'),
    url(r'all_favorites/$', 'tomatoes.views.all_favorites', name='all_favorites'),
    url(r'theater/$', 'tomatoes.views.theater', name='theater'),

)
