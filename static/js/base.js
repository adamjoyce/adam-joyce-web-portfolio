/* Typewriter. */
var TypeWriter = function(element, textPool, waitTime) {
  this.element = element;
  this.textPool = textPool;
  this.waitTime = parseInt(waitTime, 10) || 2000;
  this.text = '';
  this.count = 0;
  this.tick();
  this.isErasing = false;
};

var scrollDelayUpper = 200;
var scrollDelayLower = 100;
TypeWriter.prototype.tick = function() {
  // this.count tracks the current index for the textPool.
  var index = this.count % this.textPool.length;
  var text = this.textPool[index];

  // Adjusts the text length for writing or erasing.
  if (this.isErasing) {
    this.text = text.substring(0, this.text.length - 1);
  }
  else {
    this.text = text.substring(0, this.text.length + 1);
  }

  // Record a copy of this tick's element HTML content to recursively call
  // tick.
  this.element.innerHTML = this.text;
  var displayedText = this;

  // How long the pause is before the next tick when writing or erasing.
  // Simulates variance in typing speed.
  var scrollDelay = scrollDelayUpper - Math.random() * scrollDelayLower;

  // Erasing is twice as fast as writing.
  if (this.isErasing) { scrollDelay *= 0.5; }

  // Calculate the delay before erasing and writing begins.
  if (!this.isErasing && this.text === text) {
    scrollDelay = this.waitTime;
    this.isErasing = true;
  }
  else if (this.isErasing && this.text === '') {
    scrollDelay = this.waitTime * 0.25;
    this.isErasing = false;
    this.count++;
  }

  setTimeout(function() { displayedText.tick(); }, scrollDelay);
};
/* End of TypeWriter. */

// Executes once the window has loaded.
window.onload = function() {
  // TypeWriter.
  var elements = document.getElementsByClassName('typewrite');
  for (var i = 0; i < elements.length; i++) {
    var textPool = elements[i].getAttribute('data-text');
    var waitTime = elements[i].getAttribute('data-delay');
    if (textPool) {
      new TypeWriter(elements[i], JSON.parse(textPool), waitTime);
    }
  }
};
