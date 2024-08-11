/* global $ */

$(document).ready(function () {
  $('#btn_translate').click(function () {
    // Get the value entered in the input field
    const languageCode = $('#language_code').val();

    // Construct the API URL
    const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

    // Perform the GET request
    $.get(url, function (data) {
      // Update the div with the translation
      $('#hello').text(data.hello);
    }).fail(function () {
      // Handle errors by displaying an error message
      $('#hello').text('Error fetching translation');
    });
  });
});
