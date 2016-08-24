function popupWin() {
text = `
	<html>
		<head>
			<title>Pop Window</title>
		</head>
		<body>
			<h1>This is your alarm for {{alarm_time}}</h1>
			<audio controls autoplay>
				<source src="http://www.w3schools.com/tags/horse.ogg" type="audio/ogg">
				Your browser does not support the audio element.
			<!--<source src="horse.mp3" type="audio/mpeg"> -->
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
//  End -->