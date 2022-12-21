function trackCoords(e){
	coordinates = getCoords(e);
	cursor="Coordinates on Map (x,y): (" + coordinates[0] + "," + coordinates[1] + ")" ;
	document.getElementById("displayArea").innerHTML=cursor
	document.getElementById("displayArea2").innerHTML=cursor
}

function stopTracking(){
	document.getElementById("displayArea").innerHTML="Coordinates";
	document.getElementById("displayArea2").innerHTML="Coordinates";
}

function newLocation(e, id){
	// Get coordinates of mouse event (will be called onClick) and send to a new location form
	coordinates = getCoords(e);
	locData = {'xCoord': coordinates[0], 'yCoord': coordinates[1]};
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

function getCoords(event) {
		// Gets the coordinates of the mouse pointer on a given element
	// See: https://stackoverflow.com/questions/3234256/find-mouse-position-relative-to-element
	var rect = event.target.getBoundingClientRect();
	var coords = [(event.clientX - rect.left), (event.clientY - rect.top)];

	//Should do some validation here, like check for integer values?
	return coords;
}

	//Note: Revisit this sometime -- above function getCoords() might return floating variables if containing element
	// has decimal values. need to force intergers or otherwise validate coordinates somehow...
	// Basically, we need a way to ensure that the top-left of the map is 0,0, not o,0.25 or whatever