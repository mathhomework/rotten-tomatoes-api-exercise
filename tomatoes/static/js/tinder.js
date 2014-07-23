$(document).ready(function(){
    var apiKey= 'frt7hqdykbu8sj423hkqksu7';
    var movies = [];
//    $.ajax({
//        url: 'http://api.rottentomatoes.com/api/public/v1.0/movies/769959054/similar.json?apikey=88a8qpv9kwg657jxb97ma5nn&limit=3',
//        method: 'GET',
//        dataType: 'jsonp',
//        success:function(response){
//            console.log(response);
//        },
//        error:function(response){
//            console.log(response);
//        }
//    });

    $('#searchButton').on("click", function(){
        var pageLimit = 3;
        var query = $('#search').val();
        var movieID;
        $.ajax({
            url: 'http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=' +
                apiKey +'&q=' + query + '&page_limit=' + pageLimit,
            type: 'GET',
            dataType: 'jsonp',
            success:function(response) {
                console.log(response.movies[0].id);
                movieID = response.movies[0].id
            },
            error:function(response){
                console.log(response);
            }
        }).complete(function(){
            $.ajax({
                url: 'http://api.rottentomatoes.com/api/public/v1.0/movies/' +
                    movieID +
                    '/similar.json?apikey='+apiKey+'&limit=5',
                type: 'GET',
                dataType: 'jsonp',
                success: function(response){
                    console.log('Similar!');
                    console.log(response);
                    for (var i = 0; i< response.movies.length; i++){
                        var movieInfo = {};
                        movieInfo.title = response.movies[i].title;
                        movieInfo.poster= response.movies[i].posters.original;
                        movieInfo.identifier = response.movies[i].id;
                        movies.push(movieInfo);
                        $('#recommended').append("<div><p>"+response.movies[i].title+response.movies[i].id+"</p>" +
                            "<button class= 'learnMoreButton'>Learn More</button><div class='learnMore inactive'>"+ response.movies[i].year +
                            "</div><button class='favoriteButton'>Favorite</button></div>");
                    }
                    console.log(movies);


                },
                error: function(response){
                    console.log(response);
                }

            })
           });

    });



});

$(document).on('click','.favoriteButton', function(){
    $(this)// JSON.stringify
    $.ajax({
        url: "/new_favorite/",
        type: "POST",
        dataType: "json",
        success: function(data){
            console.log(data);

        },
        error: function(data){
            console.log(data);
        }

    });
});

$(document).on('click', '.learnMoreButton', function(){
    $(this).parent().find($('.learnMore')).toggleClass("active inactive");

});
