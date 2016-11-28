$(function(){
    $(".son_ul li").click(function(){
        $(".type_text").val($(this).val())
    })
})

function textinput(){
    var activity=$(".type_text").val()
    var gjz=$(".key_text").val()
    var dateTime=$("input[name=time]").val()
    $("#ep").find("span").click(function(){
        window.location.href="datainput?activity="+activity+"&gjz="+gjz+"&dateTime="+dateTime
    })
}