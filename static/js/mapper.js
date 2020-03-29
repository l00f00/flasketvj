
// implement methods for mapper via jquery post request
$(document).ready(function () {
  $('.btn-expand-collapse').click(function (e) {
    $('.navbar-primary').toggleClass('collapsed');
  });
  $('#turn_on').click(function () {
    $.post('/mapper/turn_on/');
    $('#monitor').html("Mapper Running")
  });
  $('#turn_off').click(function () {
    $.post('/mapper/turn_off/');
    $('#monitor').html("Mapper Killed")
  });
  $('#clearconsole').click(function () {
    $.post('/mapper/clearconsole/');
    $('#monitor').html("Console Cleared")
  });
  $('#ext').click(function () {
    $.post('/mapper/ext/');
    $('#monitor').html("Mapper Exit 2 Cli")
  });
  $('#reboot').click(function () {
    $.post('/mapper/reboot/');
    $('#monitor').html("Reboooting Please Wait")
  });
  $('#shudown').click(function () {
    $.post('/mapper/shutdown/');
    $('#monitor').html("Shutting Down Raspberry")
  });
  $('#presentation').click(function () {
    $.post('/mapper/present_mode/');
    $('#monitor').html("Presentation mode")
  });
  $('#mapping').click(function () {
    $.post('/mapper/mapping_mode/');
    $('#monitor').html("Projection mapping mode")
  });
  $('#texture').click(function () {
    $.post('/mapper/texture_mode/');
    $('#monitor').html("Texture Editing Mode")
  });
  $('#source').click(function () {
    $.post('/mapper/source_selection_mode/');
    $('#monitor').html("Source selection mode")
  });
});
