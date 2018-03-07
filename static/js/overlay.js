/* Overlay navigation functionality for small screens. */
var Overlay = {
  init: function() {
    Overlay.bindUI();
  },

  bindUI: function() {
    // Open overlay.
    var overlay = document.getElementById('nav-overlay');
    document.getElementById('nav-icon').addEventListener('click', function(e) {
      overlay.style.height = '100%';
    });

    // Close Overlay.
    document.getElementById('close-overlay').addEventListener(
      'click', function(e) {
      overlay.style.height = '0%';
    });
  }
};
