// CHART
function drawGraph(data, id, plottype) {
	var ctx = document.getElementById(id).getContext('2d');

	var chartOptions = {
		responsive							: true,
		maintainAspectRatio     : false,
		datasetFill             : false,
		tooltips: {
			mode: 'index',
			intersect: true
			},
		}

	var chart = new Chart(ctx, {
		// The type of chart we want to create
    type: plottype,
    // The data for our dataset
    data: {
				labels: data.labels,
				datasets: [{
				label: data.chartLabel,
				backgroundColor: data.backgroundColor,
				borderColor: data.linecolor,
				data: data.chartdata,
				fill: data.fill,
			}]
		},
    options: chartOptions
  });
}
