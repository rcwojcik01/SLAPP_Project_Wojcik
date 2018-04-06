$(document).ready(function() {
    var socket = io.connect('http://10.10.90.110:3000'); // create connection
    socket.on('valuesReceived', function(data) {
        $('#air-quality').text("Rangefinder Value: " + data.airQuality);
    });
});
