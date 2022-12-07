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

function newLocation(e, id){
	// Get coordinates of mouse event (will be called onClick) and send to a new location form
	rect = e.target.getBoundingClientRect();
	xCoord = e.clientX - rect.left; // X coordinate within the element
	yCoord = e.clientY - rect.top; // Y coordinate within the element
	locData = {'xCoord': xCoord, 'yCoord': yCoord};
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