$(document).ready(function(){

    var myApiKey = 'frt7hqdykbu8sj423hkqksu7';
    var searchQuery = 'The Hobbit';
    var pageLimit = 10;
    var movieInfo= {};
    $('#getMovie').on("click", function(){

        $.ajax({
            url: 'http://api.rottentomatoes.com/api/public/v1.0/' +
              'movies.json?apikey=' + myApiKey + '&q=' +
               searchQuery + '&page_limit=' + pageLimit,
            type: 'GET',
            dataType: 'jsonp',
            success: function(movie_response){
                console.log(movie_response);
                var movie = movie_response.movies[0];
                console.log(movie);
                movieInfo.title = movie.title;
                movieInfo.release_year = movie.year;
                movieInfo.critic_rating = movie.ratings.critics_score;
                movieInfo.poster = movie.posters.original;
                movieInfo.mpaa_rating = movie.mpaa_rating;
                movieInfo.runtime = movie.runtime;
                movieInfo.year = movie.year;
                movieInfo.audience_score = movie.ratings.audience_score;

            },
            error: function(error_response){
                console.log(error_response);
            }
        });
    });

    $('#saveMovie').on('click', function(){

        movieInfo = JSON.stringify(movieInfo);
        $.ajax({
            url: '/new_movie/',
            type: 'POST',
            dataType: 'json',
            data: movieInfo,
            success: function (movie_response) {
                console.log(movie_response);

            },
            error: function (error_response) {
                console.log(error_response);
            }
        });
    });

    $('#saveMovieHtml').on('click', function(){

        movieInfo = JSON.stringify(movieInfo);
        $.ajax({
            url: '/new_movie_html/',
            type: 'POST',
            dataType: 'html',
            data: movieInfo,
            success: function (movie_response) {
                console.log(movie_response);
                $('.movieInfoContainer').html(movie_response);
            },
            error: function (error_response) {
                console.log(error_response);
            }
        });
    });

    $('#searchMovie').submit(function(){


    });





});