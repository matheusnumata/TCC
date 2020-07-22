function copyToClipboard(elementId) {
  /* Get the text field */
  var copyText = document.getElementById(elementId);

  /* Select the text field */
  copyText.select();
  copyText.setSelectionRange(0, 14); /*For mobile devices*/

  /* Copy the text inside the text field */
  document.execCommand("copy");
}
