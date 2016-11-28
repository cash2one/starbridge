$(function(){
    $(".changepasswordbox li.changepassword:first").addClass("item-active");
    $(".operationbox:first").show();
    $(".changepasswordbox li.changepassword").click(function(e){
        e.preventDefault();
        var targetId = $(this).attr("id");
        $(".operationbox").hide();
        $(".changepasswordbox li.changepassword").removeClass("item-active");
        $(this).addClass("item-active");
        $("#tab-"+targetId).show();
        $(".changepassword").removeClass("lightblue").addClass("blue");
        $(this).removeClass("blue").addClass("lightblue");
    })
    $('#tab-password').ready(function(){
        $('#tab-password').hide();
    })

});

//修改个人信息，用js提交表单
$(function(){
     $("#submit_data").click(function(){
         $("#submit_dataform").submit();
        alert('保存成功');
         return false;
    });

     //$("#confirm_change").click(function(){
     //    $("#sumbit_changepassword").submit()
     //       return false;
     //});
 })




//获取输入密码的值
//function clickValues(){
//        alert();
//    return false;
//}

function clickValues(){
    a = $("#oldpassword").val()   //获取原来旧密码的值
    b = $("#newpassword1").val()  //获取第一次输入新密码的值
    c = $("#newpassword2").val()  //获取第二次输入新密码的值
    var dataText = {'a':a,'b':b}
    send(a,b)

//把数据传递给后端
function send(a,b){
    if(b==c) {
        var flag =true;
        $.ajax({
            type: 'POST',
            datatype:'json',
            data: dataText,
            url: '/changepassword/',
            async: false,
            cache:false,
            success: function (data) {
            if (data.a == 'a') {
                alert('保存成功')
                //location.href="http://127.0.0.1:8000/login"
                flag = false;
            }else {
                alert('输入旧密码不对')
                flag = false;
            }
            }
        })
    }else{
        alert('两次密码输入不一致')
    }
    }
}

//防止403 forbidden
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
    var csrftoken = getCookie('csrftoken');
    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});