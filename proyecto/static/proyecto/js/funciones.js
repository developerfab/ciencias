function ubicar(event){
	var canvas=document.getElementById("lienzo");
	var ctx=canvas.getContext("2d");
	x=event.pageX;
	y=event.pageY;
	document.getElementById("cordX").value=x;
	document.getElementById("cordY").value=y;
}