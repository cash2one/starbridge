$(document).ready(function () {
        $(function () {
            $('.sortable-accordion div').show();
            $('.sortable-accordion div').slideToggle('slow');
            $('.sortable-accordion h3').click(function () {
                $(this).toggleClass('current');
            });
        });
        $('.options').click(function () {
            var childpos = $(this).offset();
            var parentpos = $(this).parent().offset();
            var posLeft = childpos.left - parentpos.left;
            $('#submenu').css({
                'top': childpos.top - 10 + 'px',
                'left': posLeft + 420 + 'px'
            }).fadeIn(200);
            $('#submenu').mouseleave(function () {
                $(this).fadeOut(200);
            });
        });
        $('#sidebar-menu').ready(function(){
            $('#sidebar-menu').addClass('animate');
            $('#sidebar-menu li span').animate({
                    'opacity': 1,
                    'margin-left': '0'
                });
                 $('#pagecontent').css({
                    'margin-left':'180px'
                });
        });
        var i=0;
        $('#toggleMenu .list').click(function () {
            i++;
            if(i%2==0){
                $('#sidebar-menu li span').css({
                    'opacity': 0,
                    'margin-left': '9px'
                });
                $('#pagecontent').css({
                    'margin-left':'50px'
                })
                $('#sidebar-menu').removeClass('animate');
                $('.content_button').css('left','-126px');
            }else{
                $('#sidebar-menu li span').animate({
                    'opacity': 1,
                    'margin-left': '0px'
                });
                 $('#pagecontent').css({
                    'margin-left':'180px'
                })
                 $('#sidebar-menu').addClass('animate');
                 $('.content_button').css('left','-115px');
            }
        });
        $('#sidebar-menu li').click(function () {
            $('#sidebar-menu li').not(this).removeClass('selected');
            $(this).toggleClass('selected');
        });

        //.choose-date为双向选择日历
        //.div-date为单项选择日历
            $(".div-date").daterangepicker({
                "singleDatePicker": true,
                "locale": {
                        "format": "YYYY-MM-DD"}
            });
        $(".daterangepicker_input input").text(moment().format('YYYY-MM-DD'));

            $('.choose-date').daterangepicker({
                "locale": {
                    "format": "YYYY-MM-DD"
                }
            });
        $(".date_detail").click(function(){
            var id = $(this).attr("id");
            if(id=="today"){
                $('.choose-date').val([moment().format('YYYY-MM-DD')+" - "+moment().format('YYYY-MM-DD')]);
            }else if(id=="yesterday"){
                $('.choose-date').val([moment().subtract(1, 'days').format('YYYY-MM-DD')+" - "+moment().format('YYYY-MM-DD')]);
            }else if(id=="last7"){
                $('.choose-date').val([moment().subtract(6, 'days').format('YYYY-MM-DD')+" - "+moment().format('YYYY-MM-DD')]);
            }else if(id=="last30"){
                $('.choose-date').val([moment().subtract(29, 'days').format('YYYY-MM-DD')+" - "+moment().format('YYYY-MM-DD')]);
            }
        });
});
   //下拉菜单
$(document).ready(function(){
    $('.son_ul').hide(); //初始ul隐藏
    $('.select_box span').click(function(){ //鼠标移动函数
        $(this).parent().find('ul.son_ul').slideDown();  //找到ul.son_ul显示
        $(this).parent().find('li').hover(function(){$(this).addClass('hover')},function(){$(this).removeClass('hover')}); //li的hover效果
        $(this).parent().hover(function(){},
        function(){
            $(this).parent().find("ul.son_ul").slideUp();
        });
    });
    $('ul.son_ul li').click(function(){
        $(this).parents('li').find('span').html($(this).html());
        $(this).parents('li').find('ul').slideUp();
    });
    //头部-用户
    $('.setting').hide();
    $('.admin').click(function(){
        $('.setting').slideToggle('fast');
    });
    $('.setting').mouseleave(function(){
        $('.setting').slideUp();
    });
});

