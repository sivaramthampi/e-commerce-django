function takedrawdata(){
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET","/home/jgetdata",true);
    xhttp.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200){
            var da = JSON.parse(this.responseText);
            drawchart(da)
        }
    }
    xhttp.send()
} 
function drawchart(da){
    const myChart = new Chart(document.getElementById('myChart'), 
    {
    type: 'line',
    data: {
    labels: labels(da),
    datasets: [{
        label: 'List of items',
        backgroundColor:'rgb(255,99,132)',
        borderColor:'rgb(255,99,132)',
        data: pricedata(da),
        borderWidth: 3
    }]
    },
    options: {
    scales: {
        y: {
        beginAtZero: true
        }
    }
    }
    });
}
function labels(da){
    let val = []
    for(x of da.convdata){
        val.push(x.name)
    }
    return val
}
function pricedata(da){
    let values = []
    for(x of da.convdata){
        values.push(x.price)
    }
    return values
}