$(document).ready(function() {
    var socket = io.connect('http://10.10.90.78:3000'); // create connection
    socket.on('valuesReceived', function(data) {
        $('#air-quality').text(data.airQuality);
//        $('#orientation').text(data.orientation);
//        $('#vibration').text(data.vibration);
//        $('#accelerometer').text(data.accelerometer);
    });
});
