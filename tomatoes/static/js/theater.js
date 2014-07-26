$(document).ready(function(){
    var apiKey = 'frt7hqdykbu8sj423hkqksu7';
    var playingNow = [];
    $('#playingNowButton').on("click",function(){
        var playingNowObject = {};
        $.ajax({
            url: "http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters.json?apikey=" + apiKey,
            type: "GET",
            dataType: "jsonp",
            success: function(response){
                for (var x = 0; x< response.movies.length; x++){
//                    playingNowObject = {
//                        'title':response.movies[x].title,
//                        'poster':response.movies[x].posters.original,
//                        'identifier': response.movies[x].id
//                    };
//                    playingNow.push(playingNowObject);
                    $('#playingNow').append("<p>"+response.movies[x].id+"</p>");
                }

                console.log(response);
            },
            error: function(response){
                console.log(response);
            }
        });

    });
    $('#upcomingMovies').on("click", function(){
        $.ajax({
            url: "http://api.rottentomatoes.com/api/public/v1.0/lists/movies/upcoming.json?apikey=" + apiKey,
            type: "GET",
            dataType: "jsonp",
            success: function(response){
                console.log(response);
            },
            error: function(response){
                console.log(response);
            }

        })
    })

});