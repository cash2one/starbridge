$(function () {
    $(".check").click(function () {
        b = $(".choose-date").val();     //得到选择框里日期的值
        c = $(".btn-name").text();      // 得到活动名称下拉框的值
        $.getJSON("ajax__data", "choose-date=" + b +"&btn-name="+c, function (data) {
//      以拼接字符串的方式，把值传递给后端进行处理，走的方法是ajax__data              console.info(data)
            $("#dongtai tr[name=homedata]").empty()
            if (data.jsondata != "") {
            $.each(data.jsondata, function (i, b) {
                $("#dongtai").append(
                        '<tr name="homedata">'
                        + '<td>' + b.advertiser_name + '</td>'
                        + '<td>' + b.create_time.slice(0, 10) + '</td>'
                        + '<td>' + 0 + '</td>'
                        + '<td>' + 0 + '</td>'
                        + '<td>' + 0 + '</td>'
                        + '<td>' + b.budget + '</td>'
                        + '</tr>'
                )
            })
        }else{
                 $("#dongtai").append(
                    '<tr name="homedata">'
                    +'<td colspan="6">' +'无订单'+'</td>'
                    +'</tr>'
                )
            }
        })
    })
})


$(function () {
    x_label = [00,01,02,03,04,05,06,07,08,09,10,11,12,13,14,15]
    $('#container').highcharts({
        chart: {
            backgroundColor: '#FFFDEF',
            type: 'line',
        },
        title: {
            text: '',
            x: -500 //center

        },
        subtitle: {
            text: '',
            x: -20
        },
        xAxis: {
            type: 'linear',
            gridLineWidth: 1,
            categories: x_label,
            tickmarkPlacement:'on',
            tickLength:10
        },
        yAxis: {
            title: {
                //text: 'Temperature (°C)'
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        tooltip: {
            //valueSuffix: '°C'
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle',
            borderWidth: 0
        },
        series: [{
            name: '曝光数',
            data: [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6,12,15,2,3,4]
            // data: {{exposure_list | safe}}
        }, {
            name: '曝光率',
            data: [-0.2, 0.8, 5.7, 11.3, 17.0, 22.0, 24.8, 24.1, 20.1, 14.1, 8.6, 2.5,21,4,4,4,4]
        }, {
            name: '点击数',
            data: [-0.9, 0.6, 3.5, 8.4, 13.5, 17.0, 18.6, 17.9, 2,3,3,3,14.3, 9.0, 3.9, 1.0]
            // data: {{click_list | safe }}
        }, {
            name: '点击率',
            data: [3.9, 4.2, 5.7, 2,3,3,3,8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8]
            // data: {{ clickrate_list | safe }}
        }]
    });
});

$(function(){
    $(".content-list").hide();
    $(".list-mode").click(function(){
        $(".content-charts").hide();
        $(".content-list").show();
   })
    $(".pic-mode").click(function(){
        $(".content-charts").show();
        $(".content-list").hide();
   })
    $('.list-mode').click(function(){
        $('.pic-mode').removeClass('blue');
        $('.list-mode').addClass('blue');
    })
    $('.pic-mode').click(function(){
        $('.list-mode').removeClass('blue');
        $('.pic-mode').addClass('blue');
    })
        $('#container').ready(function(){
        $("#container").highcharts().reflow();
    })
    $('#toggleMenu .list').click(function () {
        $("#container").highcharts().reflow();
    });
})