/* Typewriter module used for animating the pattern of typing on a keyboard
 * followed by erasing what was typed.
 */
var TypeWriter = function(element, textPool, periodDelay) {
  this.element = element;
  this.textPool = textPool;
  this.periodDelay = parseInt(periodDelay, 10) || 2000;
  this.scrollDelayLower = 100;
  this.scrollDelayUpper = 200;
  this.text = '';
  this.count = 0;
  this.isErasing = false;
}

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
  var scrollDelay = this.scrollDelayUpper - Math.random() *
                    this.scrollDelayLower;

  // Erasing is twice as fast as writing.
  if (this.isErasing) { scrollDelay *= 0.5; }

  // Calculate the delay before erasing and writing begins.
  if (!this.isErasing && this.text === text) {
    scrollDelay = this.periodDelay;
    this.isErasing = true;
  }
  else if (this.isErasing && this.text === '') {
    scrollDelay = this.periodDelay * 0.25;
    this.isErasing = false;
    this.count++;
  }

  setTimeout(function() { displayedText.tick(); }, scrollDelay);
};
