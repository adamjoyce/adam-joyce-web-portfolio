/* Calculates the appropriate height for the landing-page for center placement
 * of landing content.
 */
var Resize = {
  windowHeight: window.innerHeight,
  headerHeight: document.getElementById('header-container').offsetHeight +
        document.getElementsByClassName('horizontal-line')[0].style.height,
  landingSection: document.getElementById('landing-section'),

  resize: function() {
    console.log(window.innerHeight);
    console.log(this.headerHeight);
    this.setNewWindowSize();
    this.landingSection.style.minHeight = (this.windowHeight -
                                           this.headerHeight) + 'px';
  },

  setNewWindowSize: function () {
    this.windowHeight = window.innerHeight;
  }
}
