/* Filter expand/collapse functionality for small screens. */
var Filters = {
  init: function() {
    Filters.bindUI();
  },

  bindUI: function() {
    // Expand/Collapse filters.
    var filters = document.getElementById('collapsible-filters');
    document.getElementById('toggle-filters').addEventListener(
      'click', function(e) {
      if (filters.clientHeight == 0) {
        filters.style.height = '100%';
        console.log('MOVING TO 100%');
      }
      else {
        filters.style.height = '0%';
        console.log('MOVING TO 0%');
      }
    });
  }
};
