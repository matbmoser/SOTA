async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
function closeWindow() {
  
  // Open the new window 
  // with the URL replacing the
  // current page using the
  // _self value
  let new_window =
      open(location, '_self');

  // Close this window
  new_window.close();

  return false;
}