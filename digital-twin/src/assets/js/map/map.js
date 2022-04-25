// Define data for popup
var data = [
    {
      photo_img: "https://images-na.ssl-images-amazon.com/images/I/81UYaJFVjCL._SY450_.jpg", // Prefix "_img" is special. With it Magnific Popup finds an  element "photo" and replaces it completely with image tag.
      }
  ];
  
  
  // Initialize popup 
  $('.pulse-button').magnificPopup({
        key: 'image-popup',
        items: data,
        type: 'inline',
        inline: {
          // Define markup. Class names should match key names.
          markup: '<div class="white-popup"><div class="mfp-close"></div>'+
   '<div class="mfp-photo"></div>'+
              '</div>'
              }
          });
  
  // Define data for popup
  var data = [
    {
      photo_img: "https://s3-online.com/images/2018/10/13/ai-pic-2.jpg", // Prefix "_img" is special. With it Magnific Popup finds an  element "photo" and replaces it completely with image tag.
      }
  ];
  
  
  // Initialize popup 
  $('.pulse-button2').magnificPopup({
        key: 'image-popup',
        items: data,
        type: 'inline',
        inline: {
          // Define markup. Class names should match key names.
          markup: '<div class="white-popup"><div class="mfp-close"></div>'+
   '<div class="mfp-photo"></div>'+
              '</div>'
              }
          });