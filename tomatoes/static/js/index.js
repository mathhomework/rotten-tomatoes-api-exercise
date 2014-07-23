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
                movieInfo.movie_id=movie.id;
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

    var searchResults = [];
    $('#searchMovies').submit(function(){
        event.preventDefault();
        searchQuery = $('.searchInput').val();

        $.ajax({
            url: 'http://api.rottentomatoes.com/api/public/v1.0/' +
              'movies.json?apikey=' + myApiKey + '&q=' +
               searchQuery + '&page_limit=' + pageLimit,
            type: 'GET',
            dataType: 'jsonp',
            success: function(movie_response){

                for(var x=0; x<movie_response.movies.length;x++) {
                    var searchInfo = {};
                    var movie = movie_response.movies[x];
                    console.log(movie.title);
                    searchInfo.title = movie.title;
                    searchInfo.movie_id=movie.id;
                    searchInfo.critic_rating = movie.ratings.critics_score;
                    searchInfo.poster = movie.posters.original;
                    searchInfo.mpaa_rating = movie.mpaa_rating;
                    searchInfo.runtime = movie.runtime;
                    searchInfo.year = movie.year;
                    searchInfo.audience_score = movie.ratings.audience_score;
                    searchResults.push(searchInfo);
                    console.log(searchResults);
//                now for post to work.


                }
                var searchObject = {};
                searchObject.searchResults = searchResults;

                searchObject = JSON.stringify(searchObject);
                    $.ajax({
                        url: '/search_movies/',
                        type: 'POST',
                        dataType: 'html',
                        data: searchObject,
                        success: function (movie_response) {
                            console.log(movie_response);
                            $('.movieInfoContainer').html(movie_response);
                        },
                        error: function (error_response) {
                            console.log(error_response);
                        }
                    });


            },
            error: function(error_response){
                console.log(error_response);
            }
        });


    });

    $(document).on("click", '.moreInfo', function(){
        $(this).text(function(i,text){
            return text === "More Info" ? "Less Info": "More Info";
        });
        $(this).parent().find($('.showHide')).toggleClass("inactive active");

    });

    var favorites = [];
    $(document).on("click", '.favorite', function(){
       $(this).parent().find()
    });





});