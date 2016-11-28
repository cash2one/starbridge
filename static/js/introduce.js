  $(function () {
        x_label = [00,01,02,03,04,05,06,07,08,09,10,11,12,13,14,15]
        //直播平台折线图
        $('#container_online').highcharts({
        chart: {
            backgroundColor: '#FFFDEF',
            type: 'line',
        },
            title: {
                text: '近7天的直播平台浏览',
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
                name: 'PV',
                data: [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6,12,15,2,3,4]
            }, {
                name: 'UV',
                data: [-0.2, 0.8, 5.7, 11.3, 17.0, 22.0, 24.8, 24.1, 20.1, 14.1, 8.6, 2.5,21,4,4,4,4]
            }]
        });
//直播平台柱状图
        $('#container_online_colomn').highcharts({
            chart: {
                 backgroundColor: '#FFFDEF',
                 type: 'column'
            },
            title: {
                text: '近7天的微信送爱心数'
            },
            xAxis: {
                type: 'category',
                labels: {
                    rotation: -45,
                    style: {
                        fontSize: '13px',
                        fontFamily: 'Verdana, sans-serif'
                    }
                }
            },
            yAxis: {
                min: 0,
                title: {
                    text: 'Population (millions)'
                }
            },
            legend: {
                enabled: false
            },
            tooltip: {
                pointFormat: 'Population in 2008: <b>{point.y:.1f} millions</b>'
            },
            series: [{
                name: 'Population',
                data: [
                    ['送爱心数', 1000]


                ],
                dataLabels: {
                    enabled: true,
                    rotation: -90,
                    color: '#FFFFFF',
                    align: 'right',
                    format: '{point.y:.1f}', // one decimal
                    y: 10, // 10 pixels down from the top
                    style: {
                        fontSize: '13px',
                        fontFamily: 'Verdana, sans-serif'
                    }
                }
            }]
        });
    });
  $(function(){
        $('#container_online').ready(function(){
            $("#container_online").highcharts().reflow();
            $("#container_online_colomn").highcharts().reflow();
        })
        $('#toggleMenu .list').click(function () {
            $("#container_online").highcharts().reflow();
            $("#container_online_colomn").highcharts().reflow();
        });
  });