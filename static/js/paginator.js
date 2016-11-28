$(function(){
	//分页
    $(".noclick").parent("li").addClass("darkblue");
    $(".pagenumbox").click(function() {
        $(".pagenumbox").removeClass("darkblue");
        $(this).addClass("darkblue");
    })
})