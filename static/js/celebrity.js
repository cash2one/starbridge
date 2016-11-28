//$(function(){


	//红人圈
	//$(".optionbox:not(:last)").find(".redli").click(function(){
    
    // 筛选条件
    //$(".optionbox").find(".redli").click(function(){
		//$(this).parent().find(".redli").removeClass("redborder");
    //    $(this).addClass("redborder");
    //
    //    //alert($(this).attr("id"));
    //    //alert($(this).parent().find(".filter").attr("id"));
    //    //$(this).parent().find(".filter").value= $(this).attr("id")
    //    //alert($(this).attr("id"));
    //    //getAjax($(this).parent().parent().attr("id"),$(this).parent().attr("id"),$(this).attr("id"));
    //
    //
    //})
    // 是否 认证
    //$(".tablechoiceone").find(".tablechoice").click(function(){


        //alert($(this).parent().attr("id"));
        //alert($(this).parent().parent().attr("id"));
        //getAjax("","","");
	//})

    // 搜索框
    //$(".tablechoicetwo").find(".tablechoice").click(function(){

        //alert($(this).parent().attr("id"));
        //alert($(this).parent().parent().attr("id"));
        //getAjax("","","");
	//})
    
	// $(".choice").click(function(){
	// 	$(this).parent().parent().find("td:first-child").find(".draw").addClass("reddraw");
	// 	$(this).parent().find(".cancelchoice").css("display","block");
	// 	$(this).css("display","none");
     //   
	// })
	// $(".cancelchoice").click(function(){
	// 	$(this).parent().parent().find("td:first-child").find(".draw").removeClass("reddraw");
	// 	$(this).parent().find(".choice").css("display","block");
	// 	$(this).css("display","none");
     //   
	// })
        //最后一次使用的分页js代码
        	//$(function(){
        	//	//分页
    			//var totalpages=$("#totalpages").val();
             //   var currentpage=$("#currentpage").val();
             //   for (var i = totalpages;i >=1;i--) {
             //       $("#totalpages").after("<li class='pagenumbox blue'>"+i+"</li>")
             //   };
             //   $(".pagenumbox").each(function(){
             //       if($(this).text()==currentpage){
             //           $(this).addClass("darkblue")
             //       }else{
             //           $(this).removeClass("darkblue")
             //       }
             //   })
        	//})

    //分页
    //var totalpages=$("#totalpages").val();
    //            var currentpage=$("#currentpage").val();
    //            for (var i = totalpages;i >=1;i--) {
    //                $("#totalpages").after("<li class='pagenumbox blue'>"+i+"</li>")
    //            };
    //            $(".pagenumbox").each(function(){
    //                if($(this).text()==currentpage){
    //                    $(this).addClass("darkblue")
    //                }else{
    //                    $(this).removeClass("darkblue")
    //                }
    //            })
//})


// category "身份- 红人或者明星"  type "种类"   id ""
function  getAjax(category,type,id) {

    if (category  == 'celebrity'){
        $.getJSON("ajax_celebrity_data", "type="+type+"&id="+id, function(data) {
            $.each(data, function(i,item){
            // i 为索引，item为遍历值
            //    alert(i);
            //    alert(item);
            });
        });
    }
    else if (category  == 'star'){
        $.getJSON("ajax_star_data", "type="+type+"&id="+id, function(data) {});
    }
}
