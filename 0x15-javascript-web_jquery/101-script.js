/* global $ */

$(document).ready(function () {
  // Click handler for adding a new item
  $('#add_item').click(function () {
    $('.my_list').append('<li>Item</li>');
  });

  // Click handler for removing the last item
  $('#remove_item').click(function () {
    $('.my_list li').last().remove();
  });

  // Click handler for clearing all items
  $('#clear_list').click(function () {
    $('.my_list').empty();
  });
});
