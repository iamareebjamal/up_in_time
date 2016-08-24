function popupWin() {
text = `
	<html>
		<head>
			<title>Pop Window</title>
		</head>
		<body>
			<audio controls autoplay loop>
				{% load staticfiles %}
				<source src="/static/alarm/Argon.ogg" type="audio/ogg">
				Your browser does not support the audio element.
			</audio>
			<center>
			<br>
				Tring!!! Tring!!!!!!!!!!.
			</center>
		</body>
	</html>`;
	setTimeout('windowProp(text)', 10); 		// delay 10 milliseconds before opening
}
function windowProp(text) {
	newWindow = window.open('','newWin','width=300,height=400');
	newWindow.document.write(text);
	setTimeout('closeWin(newWindow)', 5 * 60 * 1000);	// delay 5 minutes before closing
}
function closeWin(newWindow) {
	newWindow.close();				// close small window and depart
}