function prokeysearch(){
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET","/home/contain/" + document.getElementById('sb').value,true);
    xhttp.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200){
            var data = JSON.parse(this.responseText);
            str = '<div style="color:gray;border-color:purple;width:500px;font-size:20px"><b>'
            for(x of data.fd){
                    str = str + x.name + ' - '
                    str = str + '₹'+x.price + '<br>'
            }
            str = str + '</b></div>'
            document.getElementById('data').innerHTML = str
        }
     }
     xhttp.send();
}