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
                        movies.push(movieInfo); //this movies is different from response.movies, which is from the api GET. there's a variable above that defines this movies as an array.
                        $('#recommended').append("<div class ='"+ response.movies[i].id+"'><p>"+response.movies[i].title+response.movies[i].id+"</p>" +
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


    $(document).on('click','.favoriteButton', function(){
        var favoriteInfo;
        for (var x = 0; x< movies.length; x++){
            if (movies[x].identifier == $(this).parent().attr("class")){
                console.log(movies[x].identifier);
                favoriteInfo = JSON.stringify(movies[x]);
                console.log(favoriteInfo);
            }
        }
        console.log("Hello" + $(this).parent().attr("class"));
        //stringify usually would go here.
        $.ajax({
            url: "/new_favorite/",
            type: "POST",
            dataType: "json",
            data: favoriteInfo,
            success: function(data){
                console.log(data);

            },
            error: function(data){
                console.log(data);
            }

        });
    });

    $('#viewFavoritesButton').on("click", function(){
    $.ajax({
        url: "/all_favorites/",
        type: "GET",
        dataType: "json",
        success: function(response){
            for(var x=0; x<response.length; x++){
                console.log(response[x]);
                $('#favorites').append("<p>"+response[x].title+"</p><img src='"+response[x].poster+"'>");
            }


        },
        error: function(response){
            console.log(response);
        }

    });
});


});



$(document).on('click', '.learnMoreButton', function(){
    $(this).parent().find($('.learnMore')).toggleClass("active inactive");

});

