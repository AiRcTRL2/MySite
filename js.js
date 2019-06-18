// This function opens and closes the navigation bar
function navBar() {
  var getWidth = document.getElementById("mySidebar");
    if (getWidth.style.width === "320px") {
        document.getElementById("mySidebar").style.width = "25px";
        document.getElementById("main").style.marginLeft = "25  px";
        //document.getElementById("openbtn").style.marginLeft = "0px"; // makes button move with sidebar
        document.getElementById("main").style.marginLeft = "0px";
        $("#nonWeatherElements").fadeOut("fast");
        $("#legend").fadeOut("fast");

        // also update CSS for the info button & add listeners
        infoFilterUI.style.backgroundColor = '#fff';
        infoFilterUI.style.border = '2px solid #fff';
        infoFilterUI.style.backgroundImage = 'url(' + infoSymbol + ')';

        addListeners("info");


    } else {
        document.getElementById("mySidebar").style.width = "320px";
        //document.getElementById("openbtn").style.marginLeft = "75%";
        $("#nonWeatherElements").fadeIn("slow");
        $("#legend").fadeIn(1300);

        // also update CSS for the info button & remove listeners
        infoFilterUI.style.backgroundColor = '#464646';
        infoFilterUI.style.border = '2px solid #464646';
        infoFilterUI.style.backgroundImage = 'url(' + infoSymbolInverted + ')';

        removeListeners("info");
    }
}