$(document).ready(function() {
    var socket = io.connect('http://10.10.90.78:3000'); // create connection
    socket.on('valuesReceived', function(data) {
        $('#air-quality').text("Air Quality Value: " + data.airQuality);
    });
});
