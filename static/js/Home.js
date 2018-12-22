/**
 * Created by nora on 2018/3/6.
 */

$(document).ready(function() {
    var username = "";
    var auth = "";
    var para = location.search; //获取url中"?"符后的字串
    if(para != "") {
        if(para.indexOf("usme=") != -1){
            var um_para = para.split("usme=", 2);
            username = um_para[1].split("&", 2);
        }
        if(para.indexOf("liauth=") != -1){
            var auth_para = para.split("liauth=", 2)[1];
        }
        if(auth_para === "authtp"){
            if (username[0] != "NULL" && username[0] != undefined) {
            $.ajax({
                type: "POST",
                url: "/logIn/",
                data: {
                    'username': username[0],
                    'password': 'NULL'
                },
                cache: false,
                success: function (data) {
                    var jsonData = JSON.parse(data)
                    if (jsonData[0]["user_exists"] === true) {
                        $("#btnLogin").hide();
                        $("#btnSignup").hide();
                        $("#headerBtnArea").append('<button id="btnUser" class="btn header-btn" type="button" onclick="showUserInfo()">' + username[0] + '</button>');
                    }
                }
            })
        }
        }
    }
})

var clicktime=1;
function datetimePicker(){
    $("#datetime").datetimepicker({
        format: 'YYYY-MM-DD',
        locale: moment.locale('zh-cn')
    });
}

// sign up form
function openSignupModal(){
    $("#signupCard1").show();
    $("#signupCard2").hide();
    $("#signupCard3").hide();
    $("#signupCard4").hide();
    $("#signupProgressBar").width($("#signupProgressBar").parent().width()*0.00);

    $("#img-card-2").hide();
    $("#img-card-3").hide();
    $("#img-card-4").hide();
}
function signupCardSwitch1(){
    $("#signupProgressBar").width($("#signupProgressBar").parent().width()*0.08);
}
function signupCardSwitch12(){
    // check password
    var email = $('#inputEmail').val();
    var username = $('#inputUsername-s').val();
    var password = $('#inputPassword-s').val();
    var password_check = $('#inputPassword_check').val();
    var sex = $('#radio_sex input[name="Sex"]:checked ').val();
    var birthday = $('#datetime').val();
    var job = $('div#multipicker .filter-option').html();
    var expenditure = $('#inputMonthEXPD').val();
    var reg = /^[0-9a-zA-Z]+$/;
    if(email === ""){
        $('#inputEmail').addClass("modal-input-warning");
    }
    else{
        $('#inputEmail').removeClass("modal-input-warning");
        if(username === ""){
            $('#inputUsername-s').addClass("modal-input-warning");
        }
        else if(!reg.test(username)){
            $('#inputUsername-s').addClass("modal-input-warning");
            $("#signinCondition").html("请输入只包含字母和数字的用户名");
        }
        else{
            $('#inputUsername-s').removeClass("modal-input-warning");
            $("#signinCondition").html("");
            if(password!=password_check || password==="" || password_check===""){
                $('#inputPassword-s').addClass("modal-input-warning");
                $('#inputPassword_check').addClass("modal-input-warning");
            }
            else{
                $('#inputPassword-s').removeClass("modal-input-warning");
                $('#inputPassword_check').removeClass("modal-input-warning");
                $.ajax({
                    type: "POST",
                    url: "/signIn/",
                    data: {
                        'email': email,
                        'username': username,
                        'password': password,
                        'password_check': password_check,
                        'sex': sex,
                        'birthday': birthday,
                        'job': job,
                        'expenditure': expenditure},
                    cache: false,
                    success: function (data) {
                        if(data === 'True'){
                            $('#signinCondition').html('抱歉，该用户名已存在');
                            $('#inputUsername-s').addClass("modal-input-warning");
                        }
                        else if(data === 'False'){
                            $('#signinCondition').html('');
                            $('#inputUsername-s').removeClass("modal-input-warning");
                            $("#signupCard1").hide();
                            $("#signupCard2").show();
                            $("#signupProgressBar").width($("#signupProgressBar").parent().width()*0.36);
                        }
                    }
                });
            }
        }
    }
}
function signupCardSwitch23(){
    var style_set1 = new Array();
    style_set1.push($('#inputUsername-s').val())
    $("table#chooseStyle1 tbody").find("button").each(function(){
        if($(this).css("background-color") === "rgb(255, 228, 225)"){
            style_set1.push($(this).attr("value"))
        }
    });
    $.ajax({
        type: "POST",
        url: "/insertStyle1/",
        data: {
            'style_set1': style_set1
        },
        traditional: true,
        // cache: false,
        success: function(data){
            if(data==="True"){
                $("#signupCard2").hide();
                $("#signupCard3").show();
                $("#img-card-1").show();
                $("#signupProgressBar").width($("#signupProgressBar").parent().width()*0.64);
            }
        }
    })
}
function signupCardSwitch34(){
    var style_set2 = new Array();
    style_set2.push($('#inputUsername-s').val())
    $("#chooseStyle2").find("td").each(function(){
        if($(this).css("border-left") === "10px solid rgb(255, 182, 193)"){
            style_set2.push($(this).attr("abbr"))
        }
    });
    $.ajax({
        type: "POST",
        url: "/insertStyle2/",
        data: {
            "style_set2": style_set2
        },
        traditional: true,
        success: function(data){
            if(data==="True"){
                $("#signupCard3").hide();
                $("#signupCard4").show();
                $("#signupProgressBar").width($("#signupProgressBar").parent().width()*1.00);
            }
        }
    })
}
function chooseStyleLabel(obj){
    if($(obj).css("background-color")=="#fff0" |$(obj).css("background-color")=="rgba(255, 255, 255, 0)" | $(obj).css("background-color")=="rgb(255, 182, 193)"){
        $(obj).css("background-color","#FFE4E1");
    }
    else {
        $(obj).css("background-color", "#fff0");
    }
}
function chooseStyleImage(obj){
    if($(obj).css("border-left")=="5px solid rgb(255, 182, 193)"){
        $(obj).css("border-left", "10px solid rgb(255, 182, 193)");
        $(obj).css("border-right", "10px solid rgb(255, 182, 193)");
    }
    else if($(obj).css("border-left")=="10px solid rgb(255, 182, 193)"){
        $(obj).css("border-left", "");
        $(obj).css("border-right", "");
    }
}

function imgCardSwitch(){
    if(clicktime%4 == 1){
        $("#img-card-1").hide();
        $("#img-card-2").show();
        $("#img-card-3").hide();
        $("#img-card-4").hide();
    }
    else if(clicktime%4 == 2){
        $("#img-card-1").hide();
        $("#img-card-2").hide();
        $("#img-card-3").show();
        $("#img-card-4").hide();
    }
    else if(clicktime%4==3){
        $("#img-card-1").hide();
        $("#img-card-2").hide();
        $("#img-card-3").hide();
        $("#img-card-4").show();
    }
    else if(clicktime%4==0){
        $("#img-card-1").show();
        $("#img-card-2").hide();
        $("#img-card-3").hide();
        $("#img-card-4").hide();
    }
    clicktime=clicktime+1;
}

// log in function
function checkEmpty(obj){
    var value = $(obj).val();
    if(value==null||value==""){
        $(obj).addClass("modal-input-warning")
    }
    else{
        $(obj).removeClass("modal-input-warning")
    };
}

function logIn(){
    var username = $("#inputUsername").val();
    var password = $("#inputPassword").val();
    $.ajax({
        type: "POST",
        url: "/logIn/",
        data:{
            'username': username,
            'password': password
        },
        cache: false,
        success: function(data){
            var jsonData = JSON.parse(data)
            if(jsonData[0]["user_exists"]===false){
                $("#logincondition").html("抱歉，用户不存在")
            }
            else if(jsonData[0]["user_exists"]===true && jsonData[0]["login_permit"]===false){
                $("#logincondition").html("抱歉，密码输入错误")
            }
            else if(jsonData[0]["user_exists"]===true && jsonData[0]["login_permit"]===true){
                $("#logincondition").html("")
                $("#btnLogin").hide()
                $("#btnSignup").hide()
                $('#signin').modal('toggle')
                $("#headerBtnArea").append('<button id="btnUser" class="btn header-btn" type="button" onclick="showUserInfo()">' + jsonData[0]["user_info"]["username"] +'</button>')
                $("#lbl_username").html(jsonData[0]["user_info"]["username"])
                $("#lbl_email").html(jsonData[0]["user_info"]["email"])
                $("#lbl_sex").html(jsonData[0]["user_info"]["sex"])
                $("#lbl_birthday").html(jsonData[0]["user_info"]["birthday"])
                $("#lbl_job").html(jsonData[0]["user_info"]["job"])
            }
        }
    })
}
function showUserInfo(){
    var username = $("#btnUser").html();
    $.ajax({
        type: "POST",
        url: "/getUserInfo/",
        data: {
            'username': username
        },
        cache: false,
        success: function(data){
            var jsondata = JSON.parse(data);
            $("#lbl_username").html(jsondata['username']);
            $("#lbl_email").html(jsondata['email']);
            $("#lbl_sex").html(jsondata['sex']);
            $("#lbl_birthday").html(jsondata['birthday']);
            $("#lbl_job").html(jsondata)['job'];
            $("#userInfo").modal('show');
        }
    })
}

function turnToMatch(){
    var loginUser = $("#btnUser").html();
    if(loginUser != undefined){
        loginUser = $("#btnUser").html();
    }
    else{
        loginUser = "NULL";
    }
    if($("#inputlink").val() === ""){
        $("#inputlink").addClass("modal-input-warning");
        $("#linkWarning").html("请输入服饰连接");
    }
    else{
        $("#inputlink").removeClass("modal-input-warning");
        $("#linkWarning").html("");
        $.ajax({
            type: "GET",
            url: "/startMatching/",
            data: {
                'product_link': $("#inputlink").val()
            },
            cache: false,
            success: function(data){
                if(loginUser === "NULL"){
                    var hr = "/match/?product_link=" + $("#inputlink").val();
                    hr=encodeURI(hr);
                    hr=encodeURI(hr);
                    window.location.href = hr;
                    // window.location.href="/match/?product_link=" + $("#inputlink").val();
                }
                else{
                    var hr = "/match/?product_link=" + $("#inputlink").val() + "&usme=" + loginUser + "&liauth=authtp";
                    // hr=encodeURI(hr);
                    // hr=encodeURI(hr);
                    // window.location.href = hr;
                    window.location.href="/match/?product_link=" + $("#inputlink").val() + "&usme=" + loginUser + "&liauth=authtp" ;
                }
            }
        })
    }
}

function checkIfUserLogIn(obj){
    var user_obj = $("#btnUser");
    var username = user_obj.html();
    var auth = "authfd";
    var li_href = $(obj).attr("value");
    if(username === undefined){
        username = "NULL";
        window.location.href = li_href;
    }
    else{
        username = $("#btnUser").html();
        auth = "authtp";
        window.location.href = li_href + "?usme=" + username + "&liauth=" + auth;
    }
}

function case2change_1(){
    $("#case2-1").hide();
    $("#case2-2").show();
}
function case2change_2(){
    $("#case2-2").hide();
    $("#case2-1").show();
}
function case3change_1(){
    $("#case3-1").hide();
    $("#case3-2").show();
}
function case3change_2(){
    $("#case3-2").hide();
    $("#case3-1").show();
}