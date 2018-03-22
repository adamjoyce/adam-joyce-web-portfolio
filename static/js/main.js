window.onload = function() {
  // Resize the landing page if applicable.
  if (document.getElementById('landing-section') !== null) {
    // Determine the header height including margins.
    var header = document.getElementById('header-container');
    var headerStyle = window.getComputedStyle(header);
    var lineStyle = window.getComputedStyle(
                      document.getElementsByClassName('horizontal-line')[0]
                    );
    var headerHeight = header.offsetHeight +
                       (parseInt(headerStyle.marginTop) || 0) +
                       (parseInt(headerStyle.marginBottom) || 0) +
                       (parseInt(lineStyle.height) || 0);
    VerticalCentering.headerHeight = headerHeight;

    VerticalCentering.centerContent = document.getElementById('landing-section');
    VerticalCentering.checkForOverlap();
  }

  // Typewriter setup.
  var typedElements = document.getElementsByClassName('typewrite');
  for (var i = 0; i < typedElements.length; ++i) {
    var textPool = typedElements[i].getAttribute('data-text');
    var periodDelay = typedElements[i].getAttribute('data-delay');
    if (textPool) {
      var typeWriter = new TypeWriter(typedElements[i], JSON.parse(textPool),
                                      periodDelay);
      typeWriter.tick();
    }
  }

  // Overlay setup.
  Overlay.init();

  // Filters for project pages.
  if (document.getElementById('collapsible-filters') !== null) {
    Filters.init();
  }
};

window.onresize = function () {
  if (document.getElementById('landing-section') !== null) {
    VerticalCentering.updatePageHeight();
    VerticalCentering.checkForOverlap();
  }
};
