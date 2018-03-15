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
      if (filters.clientHeight) {
        filters.style.height = 0;
      }
      else {
        var measuringWrapper = document.getElementById('measuring-wrapper');
        filters.style.height = measuringWrapper.clientHeight + 'px';
      }
    });
  }
};
