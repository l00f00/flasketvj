
// implement methods for mapper via jquery post request
$(document).ready(function () {
  $('#turn_on').click(function () {
    $.post('/mapper/turn_on/');
  });
  $('#turn_off').click(function () {
    $.post('/mapper/turn_off/');
  });
  $('#clearconsole').click(function () {
    $.post('/mapper/clearconsole/');
  });
  $('#ext').click(function () {
    $.post('/mapper/ext/');
  });
  $('#reboot').click(function () {
    $.post('/mapper/reboot/');
  });
  $('#shudown').click(function () {
    $.post('/mapper/shudown/');
  });
});
