function foundLoc(id){
	// Finds a location on the map and gives its name and coordinates
	position = document.getElementById(id).coords.split(",");
	posX = position[0];
	posY = position[1];
	alert(id + " is at: " + posX + "," + posY);
}

function trackCoords(e){
	// Gets the coordinates of the mouse pointer on a given element
	// See: https://stackoverflow.com/questions/3234256/find-mouse-position-relative-to-element
	rect = e.target.getBoundingClientRect();
	x = e.clientX - rect.left; // X coordinate within the element
	y = e.clientY - rect.top; // Y coordinate within the element
	cursor="Coordinates on Map (x,y): (" + x + "," + y + ")" ;
	document.getElementById("displayArea").innerHTML=cursor
	document.getElementById("displayArea2").innerHTML=cursor
}

function stopTracking(){
	document.getElementById("displayArea").innerHTML="Coordinates";
	document.getElementById("displayArea2").innerHTML="Coordinates";
}