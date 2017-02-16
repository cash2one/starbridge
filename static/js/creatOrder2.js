$(function(){
	$("#newordersubmit").click(function(){
		if($(".activematerial").length==0){
			alert("请添加新素材");
			return false;
		}
		/*if($(".fansbox").length==0){
			alert("请填写新条件");
			return false;
		}*/

	 	//素材数据
	 	var resultArr = new Array();
	 	var activematerialObjs = $(".direct .activematerial");
	 	activematerialObjs.each(function(){
	 		var obj = $(this);
	 		var result = new Object();
	 		var sucaiObj = new Object();
	 		var paiqiArr = new Array();
	 		sucaiObj['id'] = obj.find(".directcontent .hiddenid").val();
	 		sucaiObj['name'] = obj.find(".directcontent .fontgrey>.span_title").text();
	 		sucaiObj['link'] =  obj.find(".directcontent .hiddenlinkcon").val();
	 		var paiqi = obj.find(".activityscheduling");
	 		paiqi.each(function(){
	 			var paiqiObj = new Object();
	 			paiqiObj['data'] = $(this).find(".directcontent .dataone").text()+"|"+$(this).find(".directcontent .datatwo").text()
	 			paiqiObj['time'] = $(this).find(".directcontent .timeone").text()+":"+$(this).find(".directcontent .timetwo").text()+"-"+
	 					$(this).find(".directcontent .timethree").text()+":"+$(this).find(".directcontent .timefour").text();
	 			paiqiObj['pingtai'] = $(this).find(".directcontent .pingtaizhi").text();
	 			paiqiArr.push(paiqiObj);
	 		});
			sucaiObj['paiqi'] = paiqiArr;
	 		result['sucai_content'] = sucaiObj;
	 		resultArr.push(result);
	 	});	
		var jsonData = JSON.stringify(resultArr);
		$("#sucai").val(jsonData);
		//额外佣金奖励
		if($(".cps").val()==""||$(".cps").val().match(/^\s+$/g)){
			$("#cps").val("0");
		}else{
			$("#cps").val($(".cps").val());
		}
		var fansbox="";
		if($(".fansbox").length==0){
			$("#fansnum").val("0-0-0")
		}else{
			$(".fansbox").each(function(){
				fansbox+=$(this).find(".firstfansnum").text()+"-"+$(this).find(".secondfansnum").text()+"-"+$(this).find(".thirdfansnum").text()+","
			})
			$("#fansnum").val(fansbox.slice(0,-1));
		}
	    $("#flightingform2").submit();
	    return false;
	})
	//额外佣金奖励效果
	$(".clicknewcondition").click(function(){
		$(".firstfansnum").val("");
		$(".secondfansnum").val("");
		$(".thirdfansnum").val("");
		$(".fansinput").css("display","block");
		return false;
	})
	$(".fanssure").click(function(){
		if($(".fansinput .firstfansnum").val()=="" || $(".fansinput .secondfansnum").val()=="" || $(".fansinput .thirdfansnum").val()=="" || $(".fansinput .firstfansnum").val().match(/^\s+$/g) || $(".fansinput .secondfansnum").val().match(/^\s+$/g) || $(".fansinput .thirdfansnum").val().match(/^\s+$/g)){
			alert("请输入相关数值！")
		}else if($(".fansinput .firstfansnum").val().match(/^\d+$/g) && $(".fansinput .secondfansnum").val().match(/^\d+$/g) && $(".fansinput .thirdfansnum").val().match(/^\d+$/g)){
			$(".fansinput").before("<div class='directcontent fontgrey fansbox'>粉丝量为&nbsp;<span class='firstfansnum'></span>万&nbsp;至&nbsp;<span class='secondfansnum'></span>万&nbsp;，保底佣金为&nbsp;<span class='thirdfansnum'>2000</span>&nbsp;<span class='fontblue lookdetails fontbtn fansdelet'>删除</span></div>");
			var i = $(".fansbox").length-1;
			$(".fansbox").eq(i).find(".firstfansnum").text($(".fansinput .firstfansnum").val());
			$(".fansbox").eq(i).find(".secondfansnum").text($(".fansinput .secondfansnum").val());
			$(".fansbox").eq(i).find(".thirdfansnum").text($(".fansinput .thirdfansnum").val());
			$(".fansinput").css("display","none");
		}else{
			alert("请输入正确格式的数值！");
		}
		return false;
	})
	$(document).on("click",".fansdelet",function(){
		$(this).parent(".fansbox").remove();
	})
	
	//添加素材效果
	$("#updisabled").click(function(){
		if($(this).prop("checked")==true){
			$(".sucaixuanqu").click(function(){
				$(".visibleboxtwo").css("display","none");
			})
			$(".updisabledone").attr("disabled","disabled");
		}else{
			$(".updisabledone").attr("disabled",false);
			$(".sucaixuanqu").click(function(){
				$(".visibleboxtwo").css("display","block");
			})
		}
	})
	//关闭素材
	$(".visibleboxtwox").click(function(){
		$(".visibleboxtwo").css("display","none");
	})
	$("#addnewschedule").click(function(){
		if($(".newschedulelist").length==0){
			$(".visiblecontent hr").eq(0).after("<div class='newschedulelist'><div class='newsclose fontgrey'>×</div><div class='visibleconbox'><span class='fontgrey spanbox'>投放日期：</span><input type='text' name='' placeholder='请选择日期区间' class='div-date bigheighttext' readonly/><span class='fontgrey'>&nbsp;至&nbsp;&nbsp;</span><input type='text' name='' placeholder='请选择日期区间' class='div-date bigheighttext' readonly/></div><div class='visibleconbox' style='position:absolute;'><span class='fontgrey spanbox'>自定义时间：</span><span class='hours'><input type='text' class='square' readonly><ul></ul></span><span>:</span>&nbsp;&nbsp;<span class='minutes'><input type='text' class='square' readonly><ul></ul></span><span>-&nbsp;&nbsp;</span><span class='hours'><input type='text' class='square' readonly><ul></ul></span><span>:</span>&nbsp;&nbsp;<span class='minutes'><input type='text' class='square' readonly><ul></ul></span></div><div class='visibleconbox' style='margin-top:90px;overflow:hidden'><span class='fontgrey spanbox' style='float:left'>投放平台：</span><span style='display:inline-block;width:500px;float:left' class='justforinput'></span></div></div><hr>");
			$(".suibianla").each(function(){
				$(".justforinput").eq(0).append("<input type='checkbox'><span class='visibleconboxword fontgrey'>"+$(this).text()+"</span>")
			})
		}else{
			var bigheighttext=$(".newschedulelist").eq(0).find(".bigheighttext");
			if(bigheighttext.eq(0).val()==""||bigheighttext.eq(0).val().match(/^\s+$/g)||bigheighttext.eq(1).val()==""||bigheighttext.eq(1).val().match(/^\s+$/g)){
				alert("请选择投放日期！");
			}else{
				if(bigheighttext.eq(0).val()>bigheighttext.eq(1).val()){
						alert("请选择大于前者的日期！");
						return false;
				}
				var square=$(".newschedulelist").eq(0).find(".square");
				if(square.eq(0).val()==""||square.eq(0).val().match(/^\s+$/g)||square.eq(1).val()==""||square.eq(1).val().match(/^\s+$/g)||square.eq(2).val()==""||square.eq(2).val().match(/^\s+$/g)||square.eq(3).val()==""||square.eq(3).val().match(/^\s+$/g)){
					alert("请自定义时间段！")
				}else{
					/*if(square.eq(0).val()==square.eq(2).val()){
						if(square.eq(1).val()>square.eq(3).val()){
							alert("请选择大于前者的时间！");
							return false;
						}
					}else{
						if(square.eq(0).val()>square.eq(2).val()){
							alert("请选择大于前者的时间！");
							return false;
						}
					}*/
					var justforinputlength=$(".newschedulelist").eq(0).find(".justforinput").find("input:checked").length;
					if(justforinputlength==0){
						alert("请选择投放平台！")
					}else{
						$(".visiblecontent hr").eq(0).after("<div class='newschedulelist'><div class='newsclose fontgrey'>×</div><div class='visibleconbox'><span class='fontgrey spanbox'>投放日期：</span><input type='text' name='' placeholder='请选择日期区间' class='div-date bigheighttext' readonly/><span class='fontgrey'>&nbsp;至&nbsp;&nbsp;</span><input type='text' name='' placeholder='请选择日期区间' class='div-date bigheighttext' readonly/></div><div class='visibleconbox' style='position:absolute;'><span class='fontgrey spanbox'>自定义时间：</span><span class='hours'><input type='text' class='square' readonly><ul></ul></span><span>:</span>&nbsp;&nbsp;<span class='minutes'><input type='text' class='square' readonly><ul></ul></span><span>-&nbsp;&nbsp;</span><span class='hours'><input type='text' class='square' readonly><ul></ul></span><span>:</span>&nbsp;&nbsp;<span class='minutes'><input type='text' class='square' readonly><ul></ul></span></div><div class='visibleconbox' style='margin-top:90px;overflow:hidden'><span class='fontgrey spanbox' style='float:left'>投放平台：</span><span style='display:inline-block;width:500px;float:left' class='justforinput'></span></div></div><hr>")
						$(".suibianla").each(function(){
							$(".justforinput").eq(0).append("<input type='checkbox'><span class='visibleconboxword fontgrey'>"+$(this).text()+"</span>")
						})
						$(".newschedulelist:gt(0)").find(".bigheighttext").attr("disabled","disabled");
						$(".newschedulelist:gt(0)").find(".bigheighttext").css("color","#9c9698");
						$(".newschedulelist:gt(0)").find(".square").attr("disabled","disabled");
						$(".newschedulelist:gt(0)").find(".square").css("color","#9c9698");
						$(".newschedulelist:gt(0)").find(".justforinput").find("input").attr("disabled","disabled");
					}
				}
			}
		}
		$(".newschedulelist:last").next("hr").remove();
		$(".div-date").on("focus",function () {
 　　	 	$(this).daterangepicker({
                    "singleDatePicker": true,
                    "locale": {
                            "format": "YYYY-MM-DD"}
                });
    	});
    	$(".hours").each(function(){
		$(this).find("input").focus(function(){
			$(this).next().css("display","inline-block")
		})
		for(var i=0;i<=23;i++){
			if(i<10){
				$(this).find("ul").append("<li>0"+i+"</li>")
			}else{
				$(this).find("ul").append("<li>"+i+"</li>")
			}
		}
		})
	$(".minutes").each(function(){
		$(this).find("input").focus(function(){
			$(this).next().css("display","inline-block")
		})
		for(var i=0;i<=59;i++){
			if(i<10){
				$(this).find("ul").append("<li>0"+i+"</li>")
			}else{
				$(this).find("ul").append("<li>"+i+"</li>")
			}
		}
		
	})
	$(document).on("click",".hours ul li",function(){
		$(this).parent().prev().val($(this).text());
		$(this).parent().css("display","none");
	})
	$(document).on("click",".minutes ul li",function(){
		$(this).parent().prev().val($(this).text());
		$(this).parent().css("display","none");
	})
		return false;
	})
	$(document).on("click",".newsclose",function(){
		if($(".visiblecontent hr").length>1){
			$(this).parent(".newschedulelist").prev("hr").remove();
		}
		$(this).parent(".newschedulelist").remove();
	})
	//点击确认按钮之后
	$("#flightingsubmit").click(function(){
		$("#zhiboid").val($(".sucaixuanqu").attr("id"));
		$("#outsidelink").val($(".updisabledone").val());
		if($(".newschedulelist").length==0){
			alert("您还未添加新排期！");
			return false;
		}else{
			var bigheighttext=$(".newschedulelist").eq(0).find(".bigheighttext");
			if(bigheighttext.eq(0).val()==""||bigheighttext.eq(0).val().match(/^\s+$/g)||bigheighttext.eq(1).val()==""||bigheighttext.eq(1).val().match(/^\s+$/g)){
				alert("请选择投放日期！");
			}else{
				if(bigheighttext.eq(0).val()>bigheighttext.eq(1).val()){
						alert("请选择大于前者的日期！");
						return false;
				}
				var square=$(".newschedulelist").eq(0).find(".square");
				if(square.eq(0).val()==""||square.eq(0).val().match(/^\s+$/g)||square.eq(1).val()==""||square.eq(1).val().match(/^\s+$/g)||square.eq(2).val()==""||square.eq(2).val().match(/^\s+$/g)||square.eq(3).val()==""||square.eq(3).val().match(/^\s+$/g)){
					alert("请自定义时间段！")
				}else{
					/*if(square.eq(0).val()==square.eq(2).val()){
						if(square.eq(1).val()>square.eq(3).val()){
							alert("请选择大于前者的时间！");
							return false;
						}
					}else{
						if(square.eq(0).val()>square.eq(2).val()){
							alert("请选择大于前者的时间！");
							return false;
						}
					}*/
					var justforinputlength=$(".newschedulelist").eq(0).find(".justforinput").find("input:checked").length;
					if(justforinputlength==0){
						alert("请选择投放平台！")
					}else{
						$("#platformfont").before("<div style='margin-left:55px;' class='activematerial'><div class='directcontent'><span class='fontgrey'>素材<span>"+($(".activematerial").length+1)+"</span>：<span class='span_title'>"+$(".sucaixuanqu").val()+"</span></span><span class='fontblue lookdetails fontbtn orfixed' style='margin-left:20px;'>修改</span><input type='hidden' class='hiddenid' value='"+$("#zhiboid").val()+"'><span class='fontblue lookdetails orderdelet fontbtn' style='color:#ff0000;'>删除</span><input type='hidden' value='"+$("#outsidelink").val()+"' class='hiddenlinkcon'><div class='deletwarn'><div class='visibletitle blue warntitle'><span>警告</span><div class='warnx' style='float:right;font-size: 30px;'>×</div></div><div class='directcontent textcenter'><span>确定删除该素材吗？</span></div><div class='directcontent textcenter'><button class='blue sure'>确定</button><button class='blue deletdel'>取消</button></div></div></div></div>");
						for (var j = $(".newschedulelist").length - 1; j >= 0; j--) {
							var checked="";
							$(".newschedulelist").eq(j).find(".justforinput").find("input:checked").each(function(){
								checked+=$(this).next().text()+"，"
							})
							$(".activematerial").eq($(".activematerial").length-1).append("<div class='activityscheduling'><div class='directcontent'><span class='fontgrey'></span><span class='fontgrey'>日期：</span><span class='fontgrey dataone'>"+$(".newschedulelist").eq(j).find(".bigheighttext").eq(0).val()+"</span><span class='fontgrey'>&nbsp;至&nbsp;</span><span class='fontgrey datatwo'>"+$(".newschedulelist").eq(j).find(".bigheighttext").eq(1).val()+"</span></div><div class='directcontent marginleft'><span class='fontgrey'>时段：</span><span class='fontgrey timeone'>"+$(".newschedulelist").eq(j).find(".square").eq(0).val()+"</span><span class='fontgrey'>:</span><span class='fontgrey timetwo'>"+$(".newschedulelist").eq(j).find(".square").eq(1).val()+"</span><span class='fontgrey'>&nbsp;-&nbsp;</span><span class='fontgrey timethree'>"+$(".newschedulelist").eq(j).find(".square").eq(2).val()+"</span><span class='fontgrey'>:</span><span class='fontgrey timefour'>"+$(".newschedulelist").eq(j).find(".square").eq(3).val()+"</span></div><div class='directcontent marginleft'><span class='fontgrey'>投放平台：</span><span class='fontgrey pingtaizhi'>"+checked.slice(0,-1)+"</span></div></div>")
						};
							
						$(".blackbackground").css("display","none");
						$(".visiblebox").css("display","none");
					}
				}
			}
		}
		return false;
	})
	//自定义时间效果
	var flagmouse=true;
	$(document).on("blur",".square",function(){
		if(flagmouse==true){
		 	$(this).next().css("display","none");
		}
	})
	$(document).on("mouseover",".hours ul,.minutes ul",function(){
			flagmouse=false;
			$(this).css("display","inline-block");
		})
	$(document).on("mouseout",".hours ul,.minutes ul",function(){
			flagmouse=true;
		})
    //删除效果
    $(document).on("click",".orderdelet",function(){
    	$(".blackbackground").css("display","block");
    	$(this).next().next().css("display","block");
    	$(this).next().next().find(".warnx").click(function(){
    		$(".blackbackground").css("display","none");
    		$(".deletwarn").css("display","none");
    	})
    	$(this).next().next().find(".deletdel").click(function(){
    		$(".blackbackground").css("display","none");
    		$(".deletwarn").css("display","none");
    	})
    	$(this).next().next().find(".sure").click(function(){
    		$(this).parents(".activematerial").remove();
    	})
    })
    //修改效果
    $(document).on("click",".orfixed",function(){
    	$(".blackbackground").css("display","block");
    	$(this).parent(".directcontent").after("<div class='visiblebox orfixedvisiblebox'><div class='visibletitle blue'><span>直播平台活动排期及素材选取</span><img src='/static/img/del.png' class='closevisible' style='width:17px;float:right;cursor:pointer;margin-top:15px'></div><div class='visiblecontent'><div class='visibleconbox'><input type='checkbox' id='updisabled'>&nbsp;&nbsp;&nbsp;<span class='fontgrey fontsize'>素材稍后上传</span></div><div class='visibleconbox'><span class='fontgrey visiblewordbox'>素材：</span><input class='blue cpsbox lookdetails sucaixuanqu' type='button' value='"+$(this).prev().find(".span_title").text()+"' id='"+$(this).next().val()+"'></div><div class='visibleconbox'><span class='fontgrey visiblewordbox'>外部链接</span><input type='text' class='fontgrey cpsbox inputcpsbux updisabledone' value='"+$(this).siblings(".hiddenlinkcon").val()+"'></div><hr><div class='visibleconbox'><input class='blue cpsbox lookdetails' id='addnewscheduleone' type='button' value='添加新的排期'></div><div class='visibleconbox'><button class='blue search visiblesure' id='flightingsubmitone'>确认</button></div></div></div>");
    	$(this).parent(".directcontent").siblings(".activityscheduling").each(function(){
    		$(".orfixedvisiblebox .visiblecontent hr").eq(0).after("<div class='newschedulelist'><div class='newsclose fontgrey'>×</div><div class='visibleconbox'><span class='fontgrey spanbox'>投放日期：</span><input type='text' name='' placeholder='请选择日期区间' readonly class='div-date bigheighttext' value='"+$(this).find(".dataone").text()+"'/><span class='fontgrey'>&nbsp;至&nbsp;&nbsp;</span><input type='text' name='' placeholder='请选择日期区间' readonly class='div-date bigheighttext' value='"+$(this).find(".datatwo").text()+"'/></div><div class='visibleconbox' style='position:absolute;'><span class='fontgrey spanbox'>自定义时间：</span><span class='hours'><input type='text' class='square' readonly value='"+$(this).find(".timeone").text()+"'><ul></ul></span><span>:</span>&nbsp;&nbsp;<span class='minutes'><input type='text' readonly class='square' value='"+$(this).find(".timetwo").text()+"'><ul></ul></span><span>-&nbsp;&nbsp;</span><span class='hours'><input type='text' class='square' readonly value='"+$(this).find(".timethree").text()+"'><ul></ul></span><span class='fontgrey'>:</span>&nbsp;&nbsp;<span class='minutes'><input type='text' class='square' readonly value='"+$(this).find(".timefour").text()+"'><ul></ul></span></div><div class='visibleconbox' style='overflow:hidden;margin-top:90px;'><span class='fontgrey spanbox' style='float:left'>投放平台：</span><span style='display:inline-block;width:500px;float:left' class='justforinput'></span></div></div><hr>");
    		$(".suibianla").each(function(){
				$(".justforinput").eq(0).append("<input type='checkbox'><span class='visibleconboxword fontgrey'>"+$(this).text()+"</span>")
			})
    		var wenzilength=$(this).find(".pingtaizhi").text().split("，");
    		$(".orfixedvisiblebox .visibleconboxword").each(function(){
    			var thistext=$(this).text();
    			for(var i=0;i<wenzilength.length;i++){
    				if(thistext==wenzilength[i]){
    					$(this).prev().prop("checked",true);
    				}
    			}
    		})	
    	});

//添加效果
		$(".orfixedvisiblebox #addnewscheduleone").click(function(){
			if($(".orfixedvisiblebox .newschedulelist").length==0){
				$(".orfixedvisiblebox .visiblecontent hr").eq(0).after("<div class='newschedulelist'><div class='newsclose fontgrey'>×</div><div class='visibleconbox'><span class='fontgrey spanbox'>投放日期：</span><input type='text' name='' placeholder='请选择日期区间' class='div-date bigheighttext' readonly/><span class='fontgrey'>&nbsp;至&nbsp;&nbsp;</span><input type='text' name='' placeholder='请选择日期区间' class='div-date bigheighttext' readonly/></div><div class='visibleconbox' style='position:absolute;'><span class='fontgrey spanbox'>自定义时间：</span><span class='hours'><input type='text' class='square' readonly><ul></ul></span><span>:</span>&nbsp;&nbsp;<span class='minutes'><input type='text' class='square' readonly><ul></ul></span><span>-&nbsp;&nbsp;</span><span class='hours'><input type='text' class='square' readonly><ul></ul></span><span>:</span>&nbsp;&nbsp;<span class='minutes'><input type='text' class='square' readonly><ul></ul></span></div><div class='visibleconbox' style='margin-top:90px;overflow:hidden'><span class='fontgrey spanbox' style='float:left'>投放平台：</span><span style='display:inline-block;width:500px;float:left' class='justforinput'></span></div></div><hr>")
				$(".suibianla").each(function(){
					$(".justforinput").eq(0).append("<input type='checkbox'><span class='visibleconboxword fontgrey'>"+$(this).text()+"</span>")
				})
			}else{
				var bigheighttext=$(".orfixedvisiblebox .newschedulelist").eq(0).find(".bigheighttext");
				if(bigheighttext.eq(0).val()==""||bigheighttext.eq(0).val().match(/^\s+$/g)||bigheighttext.eq(1).val()==""||bigheighttext.eq(1).val().match(/^\s+$/g)){
					alert("请选择投放日期！");
				}else{
					if(bigheighttext.eq(0).val()>bigheighttext.eq(1).val()){
						alert("请选择大于前者的日期！");
						return false;
					}
					var square=$(".orfixedvisiblebox .newschedulelist").eq(0).find(".square");
					if(square.eq(0).val()==""||square.eq(0).val().match(/^\s+$/g)||square.eq(1).val()==""||square.eq(1).val().match(/^\s+$/g)||square.eq(2).val()==""||square.eq(2).val().match(/^\s+$/g)||square.eq(3).val()==""||square.eq(3).val().match(/^\s+$/g)){
						alert("请自定义时间段！")
					}else{
						/*if(square.eq(0).val()==square.eq(2).val()){
							if(square.eq(1).val()>square.eq(3).val()){
								alert("请选择大于前者的时间！");
								return false;
							}
						}else{
							if(square.eq(0).val()>square.eq(2).val()){
								alert("请选择大于前者的时间！");
								return false;
							}
						}*/
						var justforinputlength=$(".orfixedvisiblebox .newschedulelist").eq(0).find(".justforinput").find("input:checked").length;
						if(justforinputlength==0){
							alert("请选择投放平台！")
						}else{
							$(".orfixedvisiblebox .visiblecontent hr").eq(0).after("<div class='newschedulelist'><div class='newsclose fontgrey'>×</div><div class='visibleconbox'><span class='fontgrey spanbox'>投放日期：</span><input type='text' name='' placeholder='请选择日期区间' class='div-date bigheighttext' readonly/><span class='fontgrey'>&nbsp;至&nbsp;&nbsp;</span><input type='text' name='' placeholder='请选择日期区间' class='div-date bigheighttext' readonly/></div><div class='visibleconbox' style='position:absolute;'><span class='fontgrey spanbox'>自定义时间：</span><span class='hours'><input type='text' class='square' readonly><ul></ul></span><span>:</span>&nbsp;&nbsp;<span class='minutes'><input type='text' class='square' readonly><ul></ul></span><span>-&nbsp;&nbsp;</span><span class='hours'><input type='text' class='square' readonly><ul></ul></span><span>:</span>&nbsp;&nbsp;<span class='minutes'><input type='text' class='square' readonly><ul></ul></span></div><div class='visibleconbox' style='margin-top:90px;overflow:hidden'><span class='fontgrey spanbox' style='float:left'>投放平台：</span><span style='display:inline-block;width:500px;float:left' class='justforinput'></span></div></div><hr>")
							$(".suibianla").each(function(){
								$(".justforinput").eq(0).append("<input type='checkbox'><span class='visibleconboxword fontgrey'>"+$(this).text()+"</span>")
							})
						}
					}
				}
			}
			$(".newschedulelist:last").next("hr").remove();
			$(".orfixedvisiblebox .div-date").on("focus",function () {
	
	 　　	 	$(this).daterangepicker({
	                    "singleDatePicker": true,
	                    "locale": {
	                            "format": "YYYY-MM-DD"}
	                });
	    	});
	    	$(".orfixedvisiblebox .hours").each(function(){
				$(this).find("input").focus(function(){
					$(this).next().css("display","inline-block")
				})
				for(var i=0;i<=23;i++){
					if(i<10){
						$(this).find("ul").append("<li>0"+i+"</li>")
					}else{
						$(this).find("ul").append("<li>"+i+"</li>")
					}
				}
			})
			$(".orfixedvisiblebox .minutes").each(function(){
				$(this).find("input").focus(function(){
					$(this).next().css("display","inline-block")
				})
				for(var i=0;i<=59;i++){
					if(i<10){
						$(this).find("ul").append("<li>0"+i+"</li>")
					}else{
						$(this).find("ul").append("<li>"+i+"</li>")
					}
				}
				
			})
			$(document).on("click",".orfixedvisiblebox .hours ul li",function(){
				$(this).parent().prev().val($(this).text());
				$(this).parent().css("display","none");
			})
			$(document).on("click",".orfixedvisiblebox .minutes ul li",function(){
				$(this).parent().prev().val($(this).text());
				$(this).parent().css("display","none");
			})
			return false;
		})
		$(".orfixedvisiblebox .div-date").on("focus",function () {
 　　	 	$(this).daterangepicker({
                    "singleDatePicker": true,
                    "locale": {
                            "format": "YYYY-MM-DD"}
                });
    	});
    	$(".orfixedvisiblebox .hours").each(function(){
			$(this).find("input").focus(function(){
				$(this).next().css("display","inline-block")
			})
			for(var i=0;i<=23;i++){
				if(i<10){
					$(this).find("ul").append("<li>0"+i+"</li>")
				}else{
					$(this).find("ul").append("<li>"+i+"</li>")
				}
			}
		})
		$(".orfixedvisiblebox .minutes").each(function(){
			$(this).find("input").focus(function(){
				$(this).next().css("display","inline-block")
			})
			for(var i=0;i<=59;i++){
				if(i<10){
					$(this).find("ul").append("<li>0"+i+"</li>")
				}else{
					$(this).find("ul").append("<li>"+i+"</li>")
				}
			}
			
		})
		$(document).on("click",".orfixedvisiblebox .hours ul li",function(){
			$(this).parent().prev().val($(this).text());
			$(this).parent().css("display","none");
		})
		$(document).on("click",".orfixedvisiblebox .minutes ul li",function(){
			$(this).parent().prev().val($(this).text());
			$(this).parent().css("display","none");
		})
         //素材选取
         $(document).on("click",".orfixedvisiblebox .sucaixuanqu",function(){
		$(".visibleboxtwo").css("display","block");
		$(".visibleboxtwo").find("tr:not(:first)").click(function(){
			$(".sucaixuanqu").val("");
			$(".sucaixuanqu").val($(this).find("td").eq(0).text());
			$(".sucaixuanqu").attr("id","");
			$(".sucaixuanqu").attr("id",$(this).find("input").val());
			$(".visibleboxtwo").css("display","none");
		})
		return false;
	})
         //修改页面素材弹窗关闭
         $(document).on("click",".orfixedvisiblebox .sucaixuanqu .visibleboxtwox",function(){
         	$(".visibleboxtwo").css("display","none");
         })



			//点击确认按钮之后
	$(".orfixedvisiblebox #flightingsubmitone").click(function(){
		$("#zhiboid").val($(".sucaixuanqu").attr("id"));
		$("#outsidelink").val($(".updisabledone").val());
		if($(".newschedulelist").length==0){
			alert("您还未添加新排期！");
			return false;
		}else{
			var bigheighttext=$(".newschedulelist").eq(0).find(".bigheighttext");
			if(bigheighttext.eq(0).val()==""||bigheighttext.eq(0).val().match(/^\s+$/g)||bigheighttext.eq(1).val()==""||bigheighttext.eq(1).val().match(/^\s+$/g)){
				alert("请选择投放日期！");
			}else{
				if(bigheighttext.eq(0).val()>bigheighttext.eq(1).val()){
						alert("请选择大于前者的日期！");
						return false;
				}
				var square=$(".newschedulelist").eq(0).find(".square");
				if(square.eq(0).val()==""||square.eq(0).val().match(/^\s+$/g)||square.eq(1).val()==""||square.eq(1).val().match(/^\s+$/g)||square.eq(2).val()==""||square.eq(2).val().match(/^\s+$/g)||square.eq(3).val()==""||square.eq(3).val().match(/^\s+$/g)){
					alert("请自定义时间段！")
				}else{
					/*if(square.eq(0).val()==square.eq(2).val()){
						if(square.eq(1).val()>square.eq(3).val()){
							alert("请选择大于前者的时间！");
							return false;
						}
					}else{
						if(square.eq(0).val()>square.eq(2).val()){
							alert("请选择大于前者的时间！");
							return false;
						}
					}*/
					var justforinputlength=$(".orfixedvisiblebox .newschedulelist").eq(0).find(".justforinput").find("input:checked").length;
					if(justforinputlength==0){
						alert("请选择投放平台！")
					}else{
						$(this).parents(".activematerial").find(".activityscheduling").remove();
						for (var j = $(".orfixedvisiblebox .newschedulelist").length - 1; j >= 0; j--) {
							var checked="";
							$(".orfixedvisiblebox .newschedulelist").eq(j).find(".justforinput").find("input:checked").each(function(){
								checked+=$(this).next().text()+"，"
							})
							
							$(this).parents(".activematerial").append("<div class='activityscheduling'><div class='directcontent'><span class='fontgrey'>—</span><span class='fontgrey'>日期：</span><span class='fontgrey dataone'>"+$(".newschedulelist").eq(j).find(".bigheighttext").eq(0).val()+"</span><span class='fontgrey'>&nbsp;至&nbsp;</span><span class='fontgrey datatwo'>"+$(".newschedulelist").eq(j).find(".bigheighttext").eq(1).val()+"</span></div><div class='directcontent marginleft'><span class='fontgrey'>时段：</span><span class='fontgrey timeone'>"+$(".newschedulelist").eq(j).find(".square").eq(0).val()+"</span><span class='fontgrey'>:</span><span class='fontgrey timetwo'>"+$(".newschedulelist").eq(j).find(".square").eq(1).val()+"</span><span class='fontgrey'>&nbsp;-&nbsp;</span><span class='fontgrey timethree'>"+$(".newschedulelist").eq(j).find(".square").eq(2).val()+"</span><span class='fontgrey'>:</span><span class='fontgrey timefour'>"+$(".newschedulelist").eq(j).find(".square").eq(3).val()+"</span></div><div class='directcontent marginleft'><span class='fontgrey'>投放平台：</span><span class='fontgrey pingtaizhi'>"+checked.slice(0,-1)+"</span></div></div>")
						};
							
						$(".blackbackground").css("display","none");
						$(".orfixedvisiblebox").remove();
					}
				}
			}
		}
		return false;
	})


    	$(".orfixedvisiblebox").css("display","block");
    	$(".orfixedvisiblebox #updisabled").click(function(){
			if($(this).prop("checked")==true){
				$(".orfixedvisiblebox .sucaixuanqu").click(function(){
					$(".orfixedvisiblebox .visibleboxtwo").css("display","none")
				})
				$(".orfixedvisiblebox .updisabledone").attr("disabled","disabled");
			}else{
				$(".orfixedvisiblebox .updisabledone").attr("disabled",false);
				$(".orfixedvisiblebox .sucaixuanqu").click(function(){
					$(".orfixedvisiblebox .visibleboxtwo").css("display","block");
				})
			}
		})
		$(".orfixedvisiblebox .closevisible").click(function(){
			$(".blackbackground").css("display","none");
	    	$(".orfixedvisiblebox").remove();
	    })
    });
//素材选取弹窗
	$(".sucaixuanqu").click(function(){
		$(".visibleboxtwo").css("display","block");
		$(".visibleboxtwo").find("tr:not(:first)").click(function(){
			$(".sucaixuanqu").val("");
			$(".sucaixuanqu").val($(this).find("td").eq(0).text());
			$(".sucaixuanqu").attr("id","");
			$(".sucaixuanqu").attr("id",$(this).find("input").val());
			$(".visibleboxtwo").css("display","none");
		})
		return false;
	})
})
