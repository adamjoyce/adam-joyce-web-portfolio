/* Calculates the appropriate height for the landing-page for center placement
 * of landing content.
 */
var Recenter = {
  landingSection: document.getElementById('landing-section'),
  landingContent: document.getElementById('landing-content'),

  recenter: function() {
    var marginHeight = (this.landingSection.clientHeight * 0.5) -
                       (this.landingContent.clientHeight * 0.5);
    this.landingContent.style.marginTop = marginHeight + 'px';
  },

  updatePageHeight: function() {
    this.landingSection = document.getElementById('landing-section');
  }
}
