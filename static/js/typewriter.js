var TypeWriter = {
  settings: {
    scrollDelayLower: 100,
    scrollDelayUpper: 200,
    defaultPeriodDelay: 2000
  },

  init: function() {
  },
};

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
  var scrollDelay = this.settings.scrollDelayUpper - Math.random() *
                    this.settings.scrollDelayLower;

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
