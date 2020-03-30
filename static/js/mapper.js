
// implement methods for mapper via jquery post request
$(document).ready(function () {
  // hide all pads by default
  $('.pad').hide();

  $('.btn-expand-collapse').click(function (e) {
    $('.navbar-primary').toggleClass('collapsed');
  });
  $('.btn-expand-collapse').click(function (e) {
    $('.arrow').toggleClass('glyphicon-menu-left');
    $('.arrow').toggleClass('glyphicon-menu-right');
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
    $('#monitor').html("Presentation mode");
    $('.pad').toggle(false);
    $('.present_mode').toggle(true);
  });
  $('#mapping').click(function () {
    $.post('/mapper/mapping_mode/');
    $('#monitor').html("Projection mapping mode");
    $('.pad').toggle(false);
    $('.mapping_mode').toggle(true);
  });
  $('#texture').click(function () {
    $.post('/mapper/texture_mode/');
    $('#monitor').html("Texture Editing Mode")
    $('.pad').toggle(false);
    $('.texture_mode').toggle(true);
  });
  $('#source').click(function () {
    $.post('/mapper/source_selection_mode/');
    $('#monitor').html("Source selection mode");
    $('.pad').toggle(false);
    $('.source_selection_mode').toggle(true);
  });
  //TODO:config
  $('#config_mode').click(function () {
    $.post('/mapper/config_mode/');
    $('#monitor').html("Source selection mode");
    $('.pad').toggle(false);
    $('.config_mode').toggle(true);
  });
  //INFO:mappingmode_controls
  $('.add_triangle').click(function () {
    $.post('/mapper/add_triangle/');
    $('#monitor').html("Addeded Triangle");
  });
  $('.add_quad').click(function () {
    $.post('/mapper/add_quad/');
    $('#monitor').html("Addeded Quad");
  });
  $('.add_grid').click(function () {
    $.post('/mapper/add_grid/');
    $('#monitor').html("Addeded Grid Warp");
  });
});
