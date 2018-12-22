/**
 * Created by nora on 2018/3/9.
 */

$(document).ready(function(){
    $.ajax({
            type: "POST",
            url: "/trend/loadMore/",
            data:{
                "page": 0
            },
            cache: false,
            success: function(data){
                json_data = JSON.parse(data);
                if(json_data === 'end'){
                    $("#load-sent").html('end');
                    $("#load-gif").hide();
                }
                else{
                    var i = 0;
                    for(i=0;i<20;i++){
                        var p_wid = json_data['product'+i]['wid'];
                        var p_title = json_data['product'+i]['title'];
                        var p_url= json_data['product'+i]['url'];
                        var p_favour_count = json_data['product'+i]['favour_count'];
                        $("#productRow").append('<div class="col-xs-6 col-sm-4 col-md-3 product-box" id="' + p_wid + '">' +
                                    '<div class="row product-image-box">' +
                                        '<a href="' + p_url + '" target="_blank">' +
                                        '<img src="/static/img/product-img/' + p_wid + '.jpg"/></a>' +
                                    '</div>' +
                                    '<div class="row manipulateProduct">' +
                                        '<div class="col-xs-4 col-md-3 trashbin"></div>' +
                                        '<div class="col-xs-4 col-md-6"></div>' +
                                        '<div class="col-xs-4 col-md-3 feed" id="feed1">' +
                                            '<div class="heart" id="like3" rel="unlike"></div>' +
                                            '<div class="likeCount" id="likeCount3">' + p_favour_count + '</div>' +
                                        '</div>' +
                                    '</div>' +
                                    '<div class="row product-describe-box">' +
                                        '<p class="describe-p">' + p_title + '</p>' +
                                    '</div>' +
                                '</div>'
                        );
                    }
                }
            }
        });
});


$(document).delegate(".product-box","mouseover",function(){
    $(this.getElementsByClassName("manipulateProduct")).css("visibility","visible")
});
$(document).delegate(".product-box","mouseout",function(){
    $(this.getElementsByClassName("manipulateProduct")).css("visibility","hidden")
});
$(document).delegate(".trashbin","click",function(){
    $(this).parent().parent().remove();
    var dataString = -1;
    var A=$(this).parent().parent().attr("id");
    var user_obj = $("#btnUser")
    var username = user_obj.html()
    if(username === undefined){
        username = "NULL";
    }
    else{
        username = $("#btnUser").html();
    }
    $.ajax({
        type: "POST",
        url: "/trend/likeCount/",
        data: {
            'username': username,
            'productId': A,
            'likeChange': dataString
        },
        cache: false,
        success: function (data) {

        }
    })
});

$('body').on("click",'.heart',function(){
    var dataString = 1;
    var A=$(this).parent().parent().parent().attr("id");
    $(this).css("background-position","")
    var D=$(this).attr("rel");
    if(D === 'like'){
        dataString = -1;
    }
    else{
        dataString = 1;
    }
    var user_obj = $("#btnUser")
    var username = user_obj.html()
    if(username === undefined){
        username = "NULL";
    }
    else{
        username = $("#btnUser").html();
    }
    $.ajax({
      type: "POST",
      url: "/trend/likeCount/",
      data: {
          'username': username,
          'productId': A,
          'likeChange': dataString},
      cache: false,
      success: function(data) {
          $("#" + A + " div div .likeCount").html(data);
          if (D === 'unlike') {
              $("#" + A + " div div .heart").addClass("heartAnimation");
              $("#" + A + " div div .heart").attr("rel", "like"); //applying animation class
          }
          else {
              $("#" + A + " div div .heart").removeClass("heartAnimation");
              $("#" + A + " div div .heart").attr("rel", "unlike");
              $("#" + A + " div div .heart").css("background-position", "left");
          }
      }
    });//ajax end
});//heart click end


var page = 1;
$(window).scroll(function() {
    // var totalHeight= parseFloat($(window).height()) + parseFloat($(document).scrollTop());
    if($(document.body).height()-$(document).scrollTop() < 700){
        $.ajax({
            type: "POST",
            url: "/trend/loadMore/",
            data:{
                "page": page
            },
            cache: false,
            success: function(data){
                json_data = JSON.parse(data);
                if(json_data === 'end'){
                    $("#load-sent").html('end');
                    $("#load-gif").hide();
                }
                else{
                    var i = 0;
                    for(i=0;i<20;i++){
                        var p_wid = json_data['product'+i]['wid'];
                        var p_title = json_data['product'+i]['title'];
                        var p_url= json_data['product'+i]['url'];
                        var p_favour_count = json_data['product'+i]['favour_count'];
                        $("#productRow").append('<div class="col-xs-6 col-sm-4 col-md-3 product-box" id="' + p_wid + '">' +
                                    '<div class="row product-image-box">' +
                                        '<a href="' + p_url + '" target="_blank">' +
                                        '<img src="/static/img/product-img/' + p_wid + '.jpg"/></a>' +
                                    '</div>' +
                                    '<div class="row manipulateProduct">' +
                                        '<div class="col-xs-4 col-md-3 trashbin"></div>' +
                                        '<div class="col-xs-4 col-md-6"></div>' +
                                        '<div class="col-xs-4 col-md-3 feed" id="feed1">' +
                                            '<div class="heart" id="like3" rel="unlike"></div>' +
                                            '<div class="likeCount" id="likeCount3">' + p_favour_count + '</div>' +
                                        '</div>' +
                                    '</div>' +
                                    '<div class="row product-describe-box">' +
                                        '<p class="describe-p">' + p_title + '</p>' +
                                    '</div>' +
                                '</div>'
                        );
                    }
                }
            }
        });
        page++;
    }
});