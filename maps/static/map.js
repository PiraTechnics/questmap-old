function trackCoords(e){
	// Gets the coordinates of the mouse pointer on a given element
	// See: https://stackoverflow.com/questions/3234256/find-mouse-position-relative-to-element
	var coords = getMapCoords(e);
	cursor="Coordinates on Map (x,y): (" + coords[0] + "," + coords[1] + ")" ;
	document.getElementById("displayArea").innerHTML=cursor
	document.getElementById("displayArea2").innerHTML=cursor
}

function stopTracking(){
	document.getElementById("displayArea").innerHTML="Coordinates";
	document.getElementById("displayArea2").innerHTML="Coordinates";
}

function newLocation(e, id){
	// Get coordinates of mouse event (will be called onClick) and send to a new location form
	var coords = getMapCoords(e);
	locData = {'xCoord': coords[0], 'yCoord': coords[1]};
	queryParam = encodeQuery(locData);
	url = "/maps/" + id + "/new_location";
	url += queryParam;
	document.location.href = url;
}

function encodeQuery(data) {
	let query = "?";
	for (let d in data)
		query += encodeURIComponent(d) + '=' 
			+ encodeURIComponent(data[d]) + '&';
	return query.slice(0, -1);
}

function getMapCoords(event) {
	var rect = event.target.getBoundingClientRect();
	var xCoord = event.clientX - rect.left; // X coordinate within the element
	var yCoord = event.clientY - rect.top; // Y coordinate within the element

	// Return an array containing both coordinates
	return [xCoord, yCoord];
}