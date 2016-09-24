

var graph_values = [];

    function drawBasic() {

    google.charts.load('current', {packages: ['corechart', 'bar']});
    google.charts.setOnLoadCallback(drawBasic);

      var data = google.visualization.arrayToDataTable([
        ['City', '2010 Population',],
        ['New York City, NY', 8175000],
        ['Los Angeles, CA', 3792000],
        ['Chicago, IL', 2695000],
        ['Houston, TX', 2099000],
        ['Philadelphia, PA', 1526000]
      ]);

      var options = {
        title: 'Premimum of the person',
        chartArea: {width: '50%'},
        hAxis: {
          title: 'horizontal axis',
          minValue: 0
        },
        vAxis: {
          title: 'vertical axis '
        }
      };

      var chart = new google.visualization.BarChart(document.getElementById('graph'));

    }

$(document).ready(function() {
    graph_values = $.parseJSON($('#insurance').val());
    console.log(graph_values);
    console.log(graph_values);
    drawBasic() ;
});

