window.onload = function() {
  // Resize the landing page if applicable.
  if (document.getElementById('landing-section') !== null) {
    Resize.resize();
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
};

window.onresize = function () {
  Resize.resize();
}
