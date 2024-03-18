function copyToClipboard() {
  // Get the div element
  var divElement = document.getElementById('code-to-copy');

  // Create a temporary textarea element
  var tempTextarea = document.createElement('textarea');

  // Set the value of the textarea to the HTML content of the div
  tempTextarea.value = divElement.innerHTML;

  // Append the temporary textarea to the body
  document.body.appendChild(tempTextarea);

  // Select the text in the temporary textarea
  tempTextarea.select();

  // Copy the selected text to the clipboard
  document.execCommand('copy');

  // Remove the temporary textarea from the body
  document.body.removeChild(tempTextarea);

  // Get the link element
  var linkElement = document.querySelector('.copy-link');

  // Store the original link text
  var originalText = linkElement.textContent;

  // Change the link text to "Copied"
  linkElement.textContent = 'Copied!';

  // Set a timeout to change the link text back after 3 seconds
  setTimeout(function() {
    linkElement.textContent = originalText;
  }, 1500);
}
