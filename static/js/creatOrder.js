$(function(){
	var checkedidlength=0;
	var checkedid=[];
	var pagenextdoneslength=0;
	if($("#checkedid").val() == ""|| $("#checkedid").val() == undefined){
		checkedidlength=0;
	}else{
		checkedid=$("#checkedid").val().split(",");
		checkedidlength=checkedid.length;
	}
	if($("#pagenextdones").val() == ""|| $("#pagenextdones").val() == undefined){
		pagenextdoneslength=0;
	}else{
		pagenextdones=$("#pagenextdones").val().split(",");
		for(var i=0;i<pagenextdones.length;i++){
			if($.inArray(pagenextdones[i], checkedid) != -1){
				continue;
			}
			checkedid.push(pagenextdones[i]);
		}
	}
	checkedidlength=checkedid.length;
	$(".redtr").each(function(){
		for(var i=0;i<checkedidlength;i++){
			if($(this).attr("id")==checkedid[i]){
				$(this).find("td:last").find(".choice").css("display","none");
				$(this).find("td:last").find(".cancelchoice").css("display","inline-block");
				$(this).find("td:first").find(".headportrait").find(".draw").addClass("justjs");
			}
		}
		if($(this).find(".status").text()=="B"){
			$(this).find("td:first-child").find(".draw").addClass("reddraw");
		}
		if($(this).find(".status").text()=="A"){
			$(this).find("td:first-child").find(".draw").removeClass("reddraw");
		}
	})
	$(".redchoiced").find("b").text(checkedidlength);
	$(".optionbox").find(".redli").click(function(){
		$(this).parent().find(".redli").removeClass("redborder");
		$(this).addClass("redborder");
	})

	$(".choice").click(function(){
		$(this).parent().parent().find("td:first-child").find(".draw").addClass("justjs");
		// $(this).parent().parent().find("td:first-child").find(".draw").addClass("reddraw");
		$(this).parent().find(".cancelchoice").css("display","inline-block");
		$(this).css("display","none");
		if($(".justjs").length==$(".redtr").length){
			 $(".selectall").prev("input").prop("checked",true)
		}else{
			 $(".selectall").prev("input").prop("checked",false)
		}
		var id = $(this).parents("tr").attr("id");
 		if(checkedid != null && checkedid != ''){
			if($.inArray(id, checkedid) == -1){
				checkedid.push(id);
			}
			$("#checkedid").val(checkedid.join(","));
			checkedidlength=checkedid.length;	
		}else{
			checkedid.push(id);
			checkedidlength=checkedid.length;
		}
		$("#pagenextdones").val(checkedid);
		$("#checkedid").val(checkedid);
		$(".redchoiced").find("b").text(checkedidlength)
	})
	$(".cancelchoice").click(function(){
		$(this).parent().parent().find("td:first-child").find(".draw").removeClass("justjs");
		// $(this).parent().parent().find("td:first-child").find(".draw").removeClass("reddraw");
		$(this).parent().find(".choice").css("display","inline-block");
		$(this).css("display","none");
		if($(".justjs").length==$(".redtr").length){
			 $(".selectall").prev("input").prop("checked",true)
		}else{
			 $(".selectall").prev("input").prop("checked",false)
		}
		var id = $(this).parents("tr").attr("id");
		if(checkedid != null && checkedid != ''){
			for (var i = 0; i < checkedid.length; i++) {
				if(checkedid[i] == id){
					checkedid.splice(i,1);

				}
			};

			$("#checkedid").val(checkedid.join(","));
			checkedidlength=checkedid.length;	
		}
		$("#pagenextdones").val(checkedid);
		$("#checkedid").val(checkedid);
		$(".redchoiced").find("b").text(checkedidlength)

	})
	$(".clicknewmaterial").click(function(){
		$(".sucaixuanqu").val("从素材库选取");
		$(".blackbackground").css("display","block");
		$(".visiblebox").css("display","block");
		$(".newschedulelist").remove();
	})
    $(".closevisible").click(function(){
    	$(".visiblebox").css("display","none");
    	$(".blackbackground").css("display","none")
    })

    //链接
    $(".link").click(function(){
//    弹框span清空显示
        $(".linkpopupboxzmb").find("span").remove();
        var orderlink=$(this).attr("name");
        $(".linkpopupboxzmb").append("<span>"+orderlink+"</span>");

    	$(".linkpopupbox").css("display","block");
    	$(".linkpopupboxwarnx").click(function(){
    		$(".linkpopupbox").css("display","none");
    	})
    	$(".linkpopupboxdeletdel").click(function(){
    		$(".linkpopupbox").css("display","none");
    	})
    })
	var id="";
    $(".orderdelet").click(function(){
//    弹框span清空显示
// 		e.preventDefault();
        $(".zmb").find("span").remove();
        var orderdelet=$(this).parents(".materialltr").find("td").eq(1).text();
        $(".zmb").append("<span>"+orderdelet+"</span>");

		 id=$(this).parents(".materialltr").attr("id");
		// $(".surelinkdelet").attr("href","{% url 'creative_delete' %}?id="+$(this).parents(".materialltr").attr("id"))
    	$(".deletwarn").css("display","block");
    	$(".warnx").click(function(){
    		$(".deletwarn").css("display","none");
    	})
    })
	$(".deletdel").click(function(){
    		$(".deletwarn").css("display","none");
    	})
	$(".deletsure").click(function(){
			window.location.href="del/?id="+id;
    		$(".deletwarn").css("display","none");
    	});
    //创建订单全选效果
    $(".selectall").prev("input").click(function(){
    	var selectinput=$(".selectall").prev("input").prop("checked");
		if(selectinput==undefined||selectinput==false){
			$(".choice").css("display","inline-block");
    		$(".cancelchoice").css("display","none");
			$(".draw").each(function(){
    			$(this).removeClass("justjs")
    		})
    		$(".redtr").each(function(){
    			var id = $(this).attr("id");
				if(checkedid != null && checkedid != ''){
					for (var i = 0; i < checkedid.length; i++) {
						if(checkedid[i] == id){
							checkedid.splice(i,1);
						}
					};
					$("#checkedid").val(checkedid.join(","));
					checkedidlength=checkedid.length;	
				}
    		})
		}else{
			$(".choice").css("display","none");
    		$(".cancelchoice").css("display","inline-block");
			$(".draw").each(function(){
	    		$(this).addClass("justjs")
	    	})
	    	$(".redtr").each(function(){
				var id=$(this).attr("id");
				if(checkedid != null && checkedid != ''){
					if($.inArray(id, checkedid) == -1){
						checkedid.push(id);
					}
					$("#checkedid").val(checkedid.join(","));
					checkedidlength=checkedid.length;	
				}else{
					checkedid.push(id);
					checkedidlength=checkedid.length;
				}
			})
		}
		$(".redchoiced").find("b").text(checkedidlength);
    })
	//点击下一步效果
	 // var next="";
	$(".up").click(function(){
		if($(".redchoiced").find("b").text()==0){
			alert("请选择主播！")
			return false;
		}
		if($(".ordername").val()==""||$(".ordername").val().match(/^\s+$/g)){
			alert("请输入订单名称！")
			return false;
		}else{
			$("#ordername").val($(".ordername").val());
		}
      	$("#activityid").val($(".number").text());
      	$("#ordertimepre").val($("#txtBeginDate").val());
      	$("#ordertimenext").val($("#txtEndDate").val());
  //     	next="";
		// $(".draw").each(function(){
		// 	var checked=$(this).hasClass("justjs");
			// if(checked==true){
			// 	next+=$(this).parents(".redtr").attr("id")+",";
			// }
		// })
		$("#nextmaterialid").val(checkedid.join(","));
	})
	
	//订单保存前的素材上传
	$("#waitwork").click(function () {
		if ($("#goodsurl").val()==""){
			alert("请上传文件!")
			return false;
		}else{
			var creatid = $("#creatid").val()
			var goodsurl = ($("#goodsurl").val())
			$.ajax({
				type:"GET",
				async:false,
				url:"/activity/upload_goods_url",
				data: {"id":creatid,"goods_url":goodsurl},
				success:function (data) {
					$("#mainContent span").hide()
					if (data.creativeid!=""){
						$("#mainContent").append('<span name="remit-name" class="fontred">素材:&nbsp;'+data.creativeid+'&nbsp;,素材已上传</span><br/><br/>'+'<span class="red">注:订单必须上传完素材后才会被提交审核<span>')
					}
				},
			});
		}
	});
	// 点击查看订单素材上传
	$("#checkshow").click(function () {
		if ($("#goods_url").val()==""){
			alert("请上传文件!")
			return false;
		}else{
			var creatid = $("#creat_id").val()
			var goodsurl = ($("#goods_url").val())
			$.ajax({
				type:"GET",
				async:false,
				url:"/activity/upload_goods_url",
				data: {"id":creatid,"goods_url":goodsurl},
				success:function (data) {
					$("#checkshowContent span").hide()
					if (data.creativeid!=""){
						$("#checkshowContent").append('<span name="remit-name" class="fontred">素材:&nbsp;'+data.creativeid+'&nbsp;,素材已上传</span><br/>')
					}
				},
			});
		}
	});
	//点击确认付款改变付款状态
	$("#payment").click(function () {
		var orderid = $("#payorderid").val();
		$.ajax({
				type:"GET",
				async:false,
				url:"/activity/paysuccess",
				data: {"id":orderid},
				success:function (data) {return false},
		});
	})

	//分页
    $(".noclick").parent("li").addClass("darkblue");
    $(".pagenumbox").click(function(){
        $(".pagenumbox").removeClass("darkblue");
        $(this).addClass("darkblue");
    })

    //订单详情
    var sum=0;
    $(".orderthreeform").find(".getvalue").each(function(){
    	sum+=Number($(this).find("td:last").text());
    })
    $(".orderthreeform").find("tr:last").find("#total").text(sum);
    $(".orderdetailformula").find("#totally").text(sum);
    var maxnum=[];
    if($(".orderdetails").find(".minimum").length==0){
    	maxnum=[0]
    }else{
    	$(".orderdetails").find(".minimum").each(function(){
	    	if(maxnum.length==0){
	    		maxnum.push(parseFloat($(this).text()));
	    	}else{
	    		if(maxnum[0]<$(this).text()){
	    			maxnum=[];
	    			maxnum.push(parseFloat($(this).text()));
	    		}
	    	}
	    });
    }
    
     $(".orderdetailformula").find("#minimum").text(maxnum[0]);
     $(".orderdetailformula").find("#totalandminimum").text(maxnum[0]+sum);
     var averege=parseInt($(".orderdetails").find(".avclickchoiceredformerege").text());
     $(".payforbox").find("#actualcosts").text(maxnum[0]+sum+(maxnum[0]+sum)*averege/100);
     //平均佣金总计,平台报价总计
	 $("#asds").val(maxnum[0]+sum+(maxnum[0]+sum)*averege/100);
	 $("#asd").val(maxnum[0]);
	 // $(".payalls").click(function () {
		//  $(".payzongji").submit();
	 // })
	//订单保存提交
	$("#ordersavesumbit").click(function () {
		var hiddentotally=parseFloat($("#totally").text())+parseFloat($("#minimum").text())+parseFloat($("#totalandminimum").text())*parseFloat($(".orderdetails").find(".averege").text())/100;
		$("#hiddentotally").val(hiddentotally);
		$("#ordersavesform").submit();
		return false;

	})



	//充值汇款常规报价总计
	var balance = parseInt($(".paydetail").find("#balancemoney").text())
	var zhifu = parseInt($(".paydetail").find("#orderactualcosts").text())

	if (balance<zhifu){
		$(".paydetail").find("#balancemoney").text(balance+"，余额不足,请先充值!");
		$(".activities").find("#payment").parent("a").attr("href","javascrot:;")
		$(".activities").find("#payment").attr("disabled",true);
	}
	//点击确认付款弹出支付成功
	$("#payment").click(function () {
		$(".blackbackground").css("display","block");
		$("#paymentsuccess").css("display","block");
	})
	$("#paymentsuccess").find(".visibleboxpay").click(function(){
    	$(".blackbackground").css("display","none");
    	$("#paymentsuccess").css("display","none");
    })


    //点击查看选择的红人列表
    $(".clickchoiceredform").click(function(){
    	$(".blackbackground").css("display","block");
    	$("#clickchoiceredform").css("display","block");
    	$(".redtr").each(function(){
			if($(this).find(".status").text()=="B"){
				$(this).find("td:first-child").find(".draw").addClass("reddraw");
			}
			if($(this).find(".status").text()=="A"){
				$(this).find("td:first-child").find(".draw").removeClass("reddraw");
			}
		})
    })
    $("#clickchoiceredform .visibletitle").find(".visibleboxtwox").click(function(){
    	$(".blackbackground").css("display","none");
    	$("#clickchoiceredform").css("display","none");
    })
})
function pagelinkfrom(obj){
	status="";
        $(".draw").each(function(){
                var checked=$(this).hasClass("justjs");
                if(checked==true){
                    status+=$(this).parents(".redtr").attr("id")+",";
                }
        })
       if($("#pagenextdones").val() != null && $("#pagenextdones").val() != ''){
           if(status != ""){
               var str = $("#pagenextdones").val()+","+status.slice(0,-1);
                $("#nextmaterialidonepage").val(str);
                 $(obj).attr("href", obj+"&pagenextdone="+$("#nextmaterialidonepage").val());
            }else{
                $("#nextmaterialidonepage").val($("#pagenextdones").val());
                $(obj).attr("href", obj+"&pagenextdone="+$("#nextmaterialidonepage").val());
            }
        }else{
            $("#nextmaterialidonepage").val(status.slice(0,-1));
             $(obj).attr("href", obj+"&pagenextdone="+$("#nextmaterialidonepage").val());
        }
	 return false;
}