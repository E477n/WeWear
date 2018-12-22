/**
 * Created by nora on 2018/3/9.
 */
$(document).ready(function() {
    var link = "";
    var para = location.search; //获取url中"?"符后的字串
    para = decodeURI(para);
    para = decodeURI(para);
    if(para != ""){
        if(para.indexOf("product_link") != -1){// 存在url
            var spe1 = para.split("product_link=", 2);
            if(spe1[1].indexOf("&usme=") != -1){//存在用户登录
                var spe2 = String(spe1[1]).split("&usme=", 2);
                $("#pdclink").attr("value", spe2[0]);
            }
            else{
                $("#pdclink").attr("value", spe1[1]);
            }
            $("#chooseCategory").modal('show');
        }
    }
    $("#btnstartMatching").hide();
    $("#loadingDiv").hide();
});

var cate1 = ['外套', '上装', '内衬', '内搭', '连体套装', '连衣套装', '西装套装', '裤装', '裙装', '鞋子', '配饰'];
var cate2 = new Array();
cate2[0] = ['夹克', '棉服', '棉衣', '毛呢外套', '风衣', '羽绒服', '马甲', '西服', '皮草', '毛衣外套', '斗篷', '大衣', '皮衣', '卫衣外套', '牛仔外套'];
cate2[1] = ['衬衫', '套头毛衣', '圆领卫衣', '连帽卫衣', 'T恤', '套头针织衫'];
cate2[2] = ['打底衫', '内衬'];
cate2[3] = ['文胸', '内裤', '抹胸', '吊带', '背心'];
cate2[4] = ['吊带裙', '背心裙'];
cate2[5] = ['连衣裙', '碎花裙', '衬衫裙', '连体裤', '比基尼', '毛衣裙', '套装'];
cate2[6] = ['西装套装'];
cate2[7] = ['休闲裤', '牛仔裤', '运动裤', '西裤', '背带裤', '灯笼裤', '紧身裤', '打底裤', '直筒裤', '哈伦裤', '铅笔裤', '短裤', '阔腿裤'];
cate2[8] = ['斜裙', '百褶裙', '鱼尾裙', '西服裙', '旗袍裙', '短裙', '筒裙', 'A字裙', '包臀裙', '半身裙'];
cate2[9] = ['运动鞋', '帆布鞋' , '小白鞋', '板鞋', '高帮鞋' , '短靴', '马丁靴', '长筒靴' , '高跟鞋', '皮鞋', '凉鞋'];
cate2[10] = ['针织帽', '棒球帽', '鸭舌帽', '贝雷帽', '其它帽子', '双肩包', '单肩包', '挎包', '手提包', '手表', '围巾', '项链', '耳饰', '手镯', '戒指', '领带'];
function loadCate2(){
    var i = 0;
    var cate1 = '';
    cate1 = $("#modal-select-cate1 option:selected").attr("id");
    $("#modal-select-cate2").html("");
    for(i=0;i<cate2[parseInt(cate1)].length;i++){
        $("#modal-select-cate2").append('<option id="' + i + '">' + cate2[parseInt(cate1)][i] + '</option>');
    }
}
function loadCategories(){
    var selected_cate1 = '';
    var selected_cate2 = '';
    if($("#modal-select-cate2").val()==null){
        $("#modal-select-cate2").addClass("modal-input-warning");
    }
    else{
        $("#modal-select-cate2").removeClass("modal-input-warning");
        selected_cate1 = $("#modal-select-cate1 option:selected").attr("id");
        selected_cate2 = $("#modal-select-cate2 option:selected").attr("id");
        loadCate1page();
        $("#select-cate1").val(cate1[parseInt(selected_cate1)]);
        loadCate2page();
        $("#select-cate2").val(cate2[parseInt(selected_cate1)][parseInt(selected_cate2)])
        $("#btnstartMatching").show();
        $("#chooseCategory").modal('hide');
    }
}
function loadCate1page(){
    var i = 0;
    if($("#pdclink").val() != ""){
        $("#div-selectCate1").html("");
        $("#div-selectCate2").html("");
        $("#div-selectCate1").append('<label class="margin-left--15">类别1</label>');
        $("#div-selectCate1").append('<select id="select-cate1" class="form-control match-cate-modal margin-left--15" onchange="loadCate2page()"></select>');
        for(i=0;i<cate1.length;i++){
            $("#select-cate1").append('<option id="' + i + '">' + cate1[i] + '</option>')
        }
    }
}
function loadCate2page(){
    var i = 0;
    var cate1_selected = '';
    cate1_selected = $("#select-cate1 option:selected").attr("id");
    $("#div-selectCate2").html("");
    $("#div-selectCate2").append('<label class="margin-left-15">类别2</label>');
    $("#div-selectCate2").append('<select id="select-cate2" class="form-control match-cate-modal margin-left-15" onchange="loadButton()"></select>');
    for(i=0;i<cate2[parseInt(cate1_selected)].length;i++){
        $("#select-cate2").append("<option>" + cate2[parseInt(cate1_selected)][i] + "</option>");
    }
}
function loadButton(){
    $("#btnstartMatching").show();
}

function callMatching(){
    $("#thumb-down").removeClass("fa-thumbs-down");
    $("#thumb-down").addClass("fa-thumbs-o-down");
    $("#thumb-up").removeClass("fa-thumbs-up");
    $("#thumb-up").addClass("fa-thumbs-o-up");
    $("#feedback-line").hide();
    var product_link = $("#pdclink").val();
    var category1 = $("#select-cate1").val();
    var category2 = $("#select-cate2").val();
    var username = $("#btnUser").html();
    var clothesArray = [];
    // var colorThief = new ColorThief();
    if(username === undefined){
        username = "NULL";
    }
    else{
        username = $("#btnUser").html();
    }
    $("#loadingDiv").show();
    $(".match-table-img-style").find("td").each(function(){
        $(this).html("");
    });
    $.ajax({
        type: "POST",
        url: "/matching/",
        data:{
            'username': username,
            'url': product_link,
            'category1': category1,
            'category2': category2
        },
        cache: false,
        success: function(data){
            $("#loadingDiv").hide();
            var jsonData = JSON.parse(data);
            // alert(String(jsonData));
            $("#matchBox2").html("");
            $("#matchBox2").append('<img id="product-img" src="/static/downloaded-img/' + jsonData["userdetail"]["image"] + '.jpg" class="input-img-style"/>');

            // for(var i in jsonData["matchset"]){
            //     if(isEmptyObject(jsonData["matchset"][i])){
            //         continue;
            //     }
            //     else{
                    for(var j in jsonData["matchset"]["matchset7"]){
                        clothesArray.push(j);
                    }
                    var n_key = 0;
                    var cloth_len = clothesArray.length;
                    $(".match-table-img-style").find("td").each(function(){
                        if(n_key<cloth_len){
                            $(this).append('<a class="img-result-a" href="' +
                                jsonData["matchset"]["matchset7"][clothesArray[n_key]]["url"] +
                                '" target="_blank"><img class="img-responsive result-img" src="/static/img/product-img/' +
                                jsonData["matchset"]["matchset7"][clothesArray[n_key]]['wid'] +
                                '.jpg" class="input-img-style" onmouseout="hoverHiddendiv(this)" onmouseover="hoverShowDiv(this)"/>' +
                                '<div id="hover-info" class="hover-info-style">' +
                                ' <label>Brand: ' + jsonData["matchset"]["matchset7"][clothesArray[n_key]]["brand"] + '</label></br>' +
                                ' <label>Title: ' + jsonData["matchset"]["matchset7"][clothesArray[n_key]]["title"] + '</label></br>' +
                                ' <label>Price: ' + jsonData["matchset"]["matchset7"][clothesArray[n_key]]["price"] + 'RMB</label></br>' +
                                ' <label>Composition: ' + jsonData["matchset"]["matchset7"][clothesArray[n_key]]["composition"] + '</label></br>' +
                                '</div></a>')
                        }
                        n_key++;
                    });
                // }
            // }
            $("#feedback-line").show();
            // var pdc_img = document.getElementById("product-img");
            // var color_palette = colorThief.getPalette(pdc_img, 8);
            // $("#matchPalette").html(color_palette);
        }
    });
}
function isEmptyObject(obj){
    if (JSON.stringify(obj) == '{}') {
        return true;
    } else {
        return false;
    }
}

function hoverShowDiv(obj){
    var position_x = obj.getBoundingClientRect().left+document.body.scrollLeft+135;
    var position_y = obj.getBoundingClientRect().top+document.body.scrollTop-110;
    $(obj).next().css("left", position_x);
    $(obj).next().css("top", position_y);
    $(obj).next().css("display", "block");
}
function hoverHiddendiv(obj){
    $(obj).next().css("display", "none");
}

function feedback(obj){
    if($(obj).attr("id") == "thumb-down"){
        if($(obj).hasClass("fa-thumbs-o-down")){
            $(obj).removeClass("fa-thumbs-o-down");
            $(obj).addClass("fa-thumbs-down");
            if($("#thumb-up").hasClass("fa-thumbs-up")){
                $("#thumb-up").removeClass("fa-thumbs-up");
                $("#thumb-up").addClass("fa-thumbs-o-up");
            }
        }
        else{
            $(obj).removeClass("fa-thumbs-down");
            $(obj).addClass("fa-thumbs-o-down");
        }
    }
    else if($(obj).attr("id") == "thumb-up"){
        if($(obj).hasClass("fa-thumbs-o-up")){
            $(obj).removeClass("fa-thumbs-o-up");
            $(obj).addClass("fa-thumbs-up");
            if($("#thumb-down").hasClass("fa-thumbs-down")){
                $("#thumb-down").removeClass("fa-thumbs-down");
                $("#thumb-down").addClass("fa-thumbs-o-down");
            }
        }
        else{
            $(obj).removeClass("fa-thumbs-up");
            $(obj).addClass("fa-thumbs-o-up");
        }
    }
}