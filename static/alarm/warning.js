// Code wrapped in IIFE to avoid polluting global namespace.
//(function() {
//  var isLinkClicked = false;
//  window.addEventListener("beforeunload", function(event) {
//    var confirmationText = "Are you sure?";
//    if (!isLinkClicked) {
//      event.returnValue = confirmationText; // Gecko, Trident, Chrome 34+
//      return confirmationText;              // Gecko, WebKit, Chrome <34
//    } else {
//      // Set flag back to false, just in case
      // user stops loading page after clicking a link.
//      isLinkClicked = false; 
//    }
//  });
//}()
//)

//var hook = true;
  //    window.onbeforeunload = function() {
    //    if (hook) {
      //    return "Wait! Have you claimed Your FREE CD Yet?"
//        }
  //    }
    //  function unhook() {
      //  hook=false;
     // }

