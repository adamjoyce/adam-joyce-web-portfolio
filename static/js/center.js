/* Calculates the appropriate height for the landing-page for center placement
 * of landing content.
 */
var Center = {
  windowHeight: window.innerHeight,
  headerHeight: document.getElementById('header-container').offsetHeight +
    document.getElementsByClassName('horizontal-line')[0].style.height,
  contentToCenter: '',

  centerContent: function() {
    var marginHeight = ((this.windowHeight * 0.5) - this.headerHeight -
                       (this.contentToCenter.clientHeight * 0.5)) * 0.5;

    if (marginHeight < 0) {
      marginHeight = 0;
    }
    this.contentToCenter.style.marginTop = marginHeight + 'px';
  },

  updatePageHeight: function() {
    this.windowHeight = window.innerHeight;
  }
}
