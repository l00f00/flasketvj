
// implement methods for mapper via jquery post request
$(document).ready(function () {
  // $('.navbar-primary').addClass('collapsed');
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
    $('#monitor').html("Config mode");
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
  $('.add_circle').click(function () {
    $.post('/mapper/add_circle/');
    $('#monitor').html("Add circle surface");
  });
  $('.duplicate').click(function () {
    $.post('/mapper/duplicate/');
    $('#monitor').html("Duplicated x 2");
  });
  $('.scale_up').click(function () {
    $.post('/mapper/scale_up/');
    $('#monitor').html("Scaled surface up +");
  });
  $('.scale_down').click(function () {
    $.post('/mapper/scale_down/');
    $('#monitor').html("Scale surface down -");
  });
  $('.remove_columns').click(function () {
    $.post('/mapper/remove_columns/');
    $('#monitor').html("removed column from grid surface");
  });
  $('.add_columns').click(function () {
    $.post('/mapper/add_columns/');
    $('#monitor').html("add columns to grid surface");
  });
  $('.remove_rows').click(function () {
    $.post('/mapper/remove_rows/');
    $('#monitor').html("remove rows from grid surface");
  });
  $('.add_rows').click(function () {
    $.post('/mapper/add_rows/');
    $('#monitor').html("add rows to grid surface");
  });
  $('.next_surface').click(function () {
    $.post('/mapper/next_surface/');
    $('#monitor').html("select next surface");
  });
  $('.previous_surface').click(function () {
    $.post('/mapper/previous_surface/');
    $('#monitor').html("select previous surface");
  });
  $('.previous_vertex').click(function () {
    $.post('/mapper/previous_vertex/');
    $('#monitor').html("select previous vertex");
  });
  $('.next_vertex').click(function () {
    $.post('/mapper/next_vertex/');
    $('#monitor').html("select next vertex");
  });
  $('.layer_up').click(function () {
    $.post('/mapper/layer_up/');
    $('#monitor').html("Move selected surface one layer up");
  });
  $('.layer_down').click(function () {
    $.post('/mapper/layer_down/');
    $('#monitor').html("Move selected surface one layer down");
  });
  $('.mapper_save').click(function () {
    $.post('/mapper/mapper_save/');
    $('#monitor').html("Save! Often! Save!");
  });
  $('.layer_panel').click(function () {
    $.post('/mapper/layer_panel/');
    $('#monitor').html("Hide/show layer panel");
  });
  $('.undo').click(function () {
    $.post('/mapper/undo/');
    $('#monitor').html("CTRL + Z");
  });
  $('.newcomp').click(function () {
    $.post('/mapper/newcomp/');
    $('#monitor').html("Clear composition,Yes is all gone!");
  });
  $('.delete').click(function () {
    $.post('/mapper/delete/');
    $('#monitor').html("Delete surface");
  });
  $('.pause').click(function () {
    $.post('/mapper/pause/');
    $('#monitor').html("Videos are Paused");
  });
  $('.next_source').click(function () {
    $.post('/mapper/next_source/');
    $('#monitor').html("Select next source <br/> (no need to use the source selection interface)");
  });
  $('.arrow_up').click(function () {
    $.post('/mapper/arrow_up/');
    $('#monitor').html("arrow up");
  }); $('.arrow_down').click(function () {
    $.post('/mapper/arrow_down/');
    $('#monitor').html("arrow_down");
  });
  $('.arrow_left').click(function () {
    $.post('/mapper/arrow_left/');
    $('#monitor').html("arrow left");
  });
  $('.arrow_right').click(function () {
    $.post('/mapper/arrow_right/');
    $('#monitor').html("arrow right");
  });
  $('.accuracy').click(function () {
    $.post('/mapper/accuracy/');
    $('#monitor').html("Toggle 1px/10px steps for keyboard moves on Raspberry Pi");
  });
});
