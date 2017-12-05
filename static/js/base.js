var typeText = function(element, textPool, waitTime) {
  this.element = element;
  this.textPool = textPool;
  this.waitTime = parseInt(waitTime, 10) || 2000;
  this.text = '';
  this.count = 0;
  this.tick();
  this.isErasing = false;
};

typeText.prototype.tick = function() {
  // Pseduo-randomly select the next line to be displayed.
  var i = this.count % this.textPool.length;
  var text = this.textPool[i];

  // Adjusts the text length for writing or erasing.
  if (this.isErasing) {
    this.text = text.substring(0, this.text.length - 1);
  }
  else {
    this.text = text.substring(0, this.text.length + 1);
  }

  this.element.innerHTML = /*'<span class="wrap">' +*/ this.text /*+ '</span>'*/;

  var currentText = this;
  var scrollDelay = 200 - Math.random() * 100;

  if (this.isErasing) { scrollDelay *= 0.5; }

  if (!this.isErasing && this.text === text) {
    // Pause before erasing begins.
    scrollDelay = this.waitTime;
    this.isErasing = true;
  }
  else if (this.isErasing && this.text === '') {
    // Short pause before writing the next line.
    scrollDelay = 500;
    this.isErasing = false;
    this.count++;
  }

  setTimeout(function() { currentText.tick(); }, scrollDelay);
};

window.onload = function() {
    var elements = document.getElementsByClassName('typewrite');
    for (var i = 0; i < elements.length; i++) {
      var textPool = elements[i].getAttribute('data-text');
      var waitTime = elements[i].getAttribute('data-delay');
      if (textPool) {
        new typeText(elements[i], JSON.parse(textPool), waitTime);
      }
    }

    // Inject CSS.
    var css = document.createElement("style");
    css.type = "text/css";
    css.innerHTML = ".typewrite { border-right: 0.08em solid #ee2b47;}";
    document.body.appendChild(css);
};
