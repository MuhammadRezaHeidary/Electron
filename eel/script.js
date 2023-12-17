
document.getElementById("ptn-panelize").onclick = function () {

	let BareLength = document.getElementById("ptn-bare-length").value;
	let BareHeight = document.getElementById("ptn-bare-height").value;
	let SheetLength = document.getElementById("ptn-sheet-length").value;
	let SheetHeight = document.getElementById("ptn-sheet-height").value;

	if(parseFloat(BareLength) <= parseFloat(SheetLength))
		alert("Sheet length must be smaller than PCB raw materal length!");
	else if(parseFloat(BareHeight) <= parseFloat(SheetHeight))
		alert("Sheet height must be smaller than PCB raw materal height!");
	else
		eel.plot_partitioner(parseFloat(BareLength), parseFloat(BareHeight), parseFloat(SheetLength)>=0?parseFloat(SheetLength):30, parseFloat(SheetHeight)>=0?parseFloat(SheetHeight):20);


}
