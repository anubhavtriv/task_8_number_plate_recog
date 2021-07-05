function getInfo() {
    var i = document.getElementById("id1").value;
    var xhr = new XMLHttpRequest();

    xhr.open("GET", "http://192.168.0.104/cgi-bin/app.py?x=" + i, true);
    xhr.send();
    xhr.onload = function() {
        var i = document.getElementById("id1").value;
        var output = xhr.responseText;
        document.getElementById("info").innerHTML = output;
    }
}