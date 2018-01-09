/* Toggles the vertical centering of elements depending on the its height
 * in comparison to the window height - i.e. if it is overlapping elements
 * above it.
 */
var VerticalCentering = {
  windowHeight: window.innerHeight,
  headerHeight: '',
  centerContent: '',

  checkForOverlap: function() {
    var overlapThreshold = this.windowHeight - this.headerHeight;
    if (this.centerContent.classList.contains('vertical-center') &&
        this.centerContent.clientHeight >= overlapThreshold) {
      // Disable centering.
      this.centerContent.classList.remove('vertical-center');
    }
    else if (!this.centerContent.classList.contains('vertical-center') &&
             this.centerContent.clientHeight < overlapThreshold) {
      //Enable centering.
      this.centerContent.classList.add('vertical-center');
    }
    console.log("thres: " + overlapThreshold);
    console.log("content: " + this.centerContent.clientHeight);
    console.log("window: " + this.windowHeight);
    console.log("header: " + this.headerHeight);
  },

  updatePageHeight: function() {
    this.windowHeight = window.innerHeight;
  }
}
