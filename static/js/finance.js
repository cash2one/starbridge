//查看消费记录明细
function getValues(){
        $(".choose-date").val();
    $.getJSON("ajax__data", "type=" + a, function (data) {
        $("#table-remit tr[name=remit-name]").empty()
        $("#table-refund tr[name=refund-name]").empty()
        if(data.throw_data!=""){
            $.each(data.throw_data, function (i, a) {
            var name="充值汇款"
            $("#table-remit").append(
                '<tr name="remit-name">'
                +'<td>' +a.time.slice(0,10)+'</td>'
                +'<td>'+a.order_id +'</td>'
                +'<td>'+ a.number +'</td>'
                +'<td>'+ name+'</td>'
                +'<td>'+ a.amount+'</td>'
                +'<td>'+ a.Balance+'</td>'
                +'</tr>'
            )
        });
        }else{
             $("#table-remit").append(
                '<tr name="remit-name">'
                +'<td colspan="6">' +'无订单'+'</td>'
                +'</tr>'
            )
        }
        if(data.prepaid_data!=""){
             $.each(data.prepaid_data, function (i, a) {
            var name="投放信息"
            $("#table-refund").append(
                '<tr name="refund-name">'
                +'<td>' +a.time.slice(0,10) +'</td>'
                +'<td>'+a.order_id +'</td>'
                +'<td>'+ a.number +'</td>'
                +'<td>'+ name+'</td>'
                +'<td>'+ a.amount+'</td>'
                +'<td>'+ a.Balance+'</td>'
                +'</tr>'
            )
        });
        }else{
             $("#table-refund").append(
                '<tr name="refund-name">'
                +'<td colspan="6">' +'无订单'+'</td>'
                +'</tr>'
            )
        }

    });
    }

$(function(){
    var href = window.location.href;
    //如果有/length后面-1
    var param = href.substring(href.indexOf("finance/")+8, href.length);
    //param里面''的值为页面finance/后面的内容
    if(param == "?type=2"){
        $(".financetitlebox li.financetitle:eq(2)").addClass("item-active");
        $(".operationbox:eq(2)").show();
        $("#remit").addClass("lightblue");
        $("#moneymanagement").removeClass("lightblue");
        $("#moneymanagement").addClass("blue");
        $("#tab-moneymanagement").ready(function(){
           $("#tab-moneymanagement").css("display","none");
        })
    }else{
        $(".operationbox li.financetitle:first").addClass("item-active");
        $(".operationbox:first").show();
    }
    
    /*消费记录明细*/
    $(".financetitle").click(function(){
        $(".financetitle").removeClass("lightblue");
        $(".financetitle").addClass("blue");
        $(this).toggleClass("lightblue");
        a = $(".choose-date").val();
        getValues();
        clickValues();
    })
    /*查询*/
    $(".financetitlebox li.financetitle:first").addClass("item-active");
    $(".operationbox:first").show();
    $(".financetitlebox li.financetitle").click(function(e){
        e.preventDefault();
        var targetId = $(this).attr("id");
        $(".operationbox").hide();
        $(".financetitlebox li.financetitle").removeClass("item-active");
        $(this).addClass("item-active");
        $("#tab-"+targetId).show();
    })
    
    $('#password').click(function(){
        $('#tab-information').hide();
        $('#tab-password').show();
    })
    //消费记录明细下拉框选择
    $("#table-remit").ready(function(){
        $("#table-remit").show();
    })

    $("#table-refund").ready(function(){
        $("#table-refund").hide();
    })

    $(".type-remint").click(function(){
        $("#table-refund").hide();
        $("#table-remit").show();

    })
    $(".type-refund").click(function(){
        $("#table-refund").show();
        $("#table-remit").hide();
    })
    
    //查看消费明细
    $("#pag-moneylist").click(function(){
       $("#tab-moneymanagement").hide();
       $("#tab-moneylist").show();
       $("#moneylist").addClass("lightblue");
       $("#moneymanagement").removeClass("lightblue");
       $("#moneymanagement").addClass("blue");
    })

    //查看汇款记录
    $("#pag-remit").click(function(){
       $("#remit").addClass("lightblue");
       $("#moneymanagement").removeClass("lightblue");
       $("#moneymanagement").addClass("blue");
       $("#tab-moneymanagement").hide();
       $("#tab-remit").show();
    })

    //查看充值汇款
    $("#query_chongzhi").click(function(){
        $(".blackbackground").css("display","block");
        $(".linkpopupbox").show()
        $("#form-remit").hide()

    })
    //退款查询事件中，把dataText挪出去
        var dataText = ""
         $("#task-son-ul li").click(function(){
             dataText =  $(this).val()
        });
    //退款查询事件
     $(".chaxun").click(function () {
         $("#context-refund tr[name='refund-name']").empty()
        if (dataText == null || dataText == "") {
            dataText = 0
        }else{
            dataText = 1
        }

       var  b = $(".select-date").val();
        send(b,dataText)
    })


    //查看退款记录
       $("#pag-refund").click(function(){
       $("#refund").addClass("lightblue");
       $("#moneymanagement").removeClass("lightblue");
       $("#moneymanagement").addClass("blue");
       $("#tab-moneymanagement").hide();
       $("#tab-refund").show();
    })

    //申请退款
    $("#turn-refund").click(function(){
        $("#page-a").hide();
        $("#page-b").show();
    })
    $("#page-b").ready(function(){
        $("#page-b").hide();
    })
    //查看汇款明细调整
  $(".choice").click(function(){
        $(this).parent().parent().find("td:first-child").find(".draw").addClass("reddraw");
        $(this).parent().find(".cancelchoice").css("display","block");
        $(this).css("display","none");
        
    })
    $(".cancelchoice").click(function(){
        $(this).parent().parent().find("td:first-child").find(".draw").removeClass("reddraw");
        $(this).parent().find(".choice").css("display","block");
        $(this).css("display","none");
        
    })
    //账户充值跳转
    $('.recharge').click(function(){
        $('#moneymanagement').removeClass('lightblue');
        $('#moneymanagement').addClass('blue');
        $('#remit').addClass('lightblue');
        $('#remit').removeClass('blue');
        $('#tab-moneymanagement').hide();
        $('#tab-remit').show();
    })
    //充值汇款中，把退款方式的value值传给后端
    $("#form-remit .deways .son_ul li").click(function(){
        var selectValue=$(this).attr("name")
        $("#recharge_box").attr("value",selectValue)
    })
    //申请退款中，把退款方式的value值传给后端，保存数据库中
    $(".refund_select li").click(function(){
        var selectValue=$(this).attr("name")
        $("#refund_box").attr("value",selectValue)
    })
 

    //分页
    $(".noclick").parent("li").addClass("darkblue");
    $(".pagenumbox").click(function(){
        $(".pagenumbox").removeClass("darkblue");
        $(this).addClass("darkblue");
    })

    $("#put_on").click(function(){
        a = $("#refund_money").val()
        b = $("#account_name").val()
        c = $("#bank_name").val()
        d = $("#bank_info").val()
        if (a != ""  || b != "" || c !== "" ||　ｄ!= "") {
            alert('提交成功');

        //}else{
        ////    alert('不成功')
        //    return false;
        }


    })


    })
function clickValues() {
    var dataText = ""
    $("#context-refund tr[name='refund-name']").empty()
    $("#task-son-ul li").click(function () {
        dataText = $(this).val()
    })
     b = $(".select-date").val();
    dataText = 0
    send(b,dataText)
}


//退款记录发送请求
function send(b,dataText){
      //$.getJSON("ajax__chaxun", "" + b + "&caozuo=" + dataText, function (data) {
          $.ajax({
              type:"GET",
              data:"chaxun-date="+b+ "&caozuo=" + dataText,
              url:"ajax__chaxun",
              async:false,
              success:function(data){
                  if (data.refund_data !="") {
                        $.each(data.refund_data, function (i, a) {
                            var yang = "";
                            if (a.type == 'A') {
                                yang = "汇款转账"
                            } else {
                                yang = "支付宝"
                            }
                            $("#context-refund").first().append(
                                '<tr name="refund-name">'
                                + '<td>' + a.time.slice(0, 10) + '</td>'
                                + '<td>' + a.amount + '</td>'
                                + '<td>' + yang + '</td>'
                                + '<td>' + '测试' + '</td>'
                                + '</tr>'
                            )
                        })
                    }else{
                      $("#context-refund tr[name=context-refund]").empty()
                      $("#context-refund").append(
                          '<tr name="refund-name">'
                          +'<td colspan="4">' +'无订单'+'</td>'
                          +'</tr>'
                      )
                  }
        }
        })
}
