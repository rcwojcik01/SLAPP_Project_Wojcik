$(document).ready(function() {
    var socket = io.connect('localhost:3000'); // create connection
    socket.on('valuesReceived', function(data) {
        $('#air-quality').text(data.airQuality);
        $('#distance').text(data.distance);
        $('#humidity').text(data.humi);
        $('#temperature').text(data.temp);
        $('#light-sensor').text(data.lightValue);
//        $('#orientation').text(data.orientation);
//        $('#vibration').text(data.vibration);
//        $('#accelerometer').text(data.accelerometer);
    });
});
