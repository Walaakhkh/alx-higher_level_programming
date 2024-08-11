/* global $ */

$(document).ready(function () {
  function fetchTranslation () {
    const languageCode = $('#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

    $.get(url, function (data) {
      $('#hello').text(data.hello);
    }).fail(function () {
      $('#hello').text('Error fetching translation');
    });
  }

  // Bind click event on button
  $('#btn_translate').click(fetchTranslation);

  // Bind enter key press event on input
  $('#language_code').keypress(function (e) {
    if (e.which === 13) { // Enter key pressed
      fetchTranslation();
    }
  });
});
