
document.getElementById("ptn-panelize").onclick = function (message) {

	let _BareLength_ = parseFloat(document.getElementById("ptn-bare-length").value);
	if(_BareLength_ <= 0 || isNaN(_BareLength_))
		alert("PCB Raw Material Lenghth must be bigger than 0cm!\rChanged to 123cm");

	let _BareHeight_ = parseFloat(document.getElementById("ptn-bare-height").value);
	if(_BareHeight_ <= 0 || isNaN(_BareHeight_))
		alert("PCB Raw Material Height must be bigger than 0cm!\rChanged to 103cm");

	let _SheetMinLength_ = parseFloat(document.getElementById("ptn-sheet-min-length").value);
	if(_SheetMinLength_ <= 0 || isNaN(_SheetMinLength_))
		alert("Sheet Minimum Length must be bigger than 0cm!\rChanged to 15cm");

	let _SheetMinHeight_ = parseFloat(document.getElementById("ptn-sheet-min-height").value);
	if(_SheetMinHeight_ <= 0 || isNaN(_SheetMinHeight_))
		alert("Sheet Minimum Height must be bigger than 0cm!\rChanged to 15cm");

	let _SheetLength_ = parseFloat(document.getElementById("ptn-sheet-length").value);
	if(_SheetLength_ <= 0 || isNaN(_SheetLength_))
		alert("Sheet Length must be bigger than 0cm!\rChanged to 30cm");

	let _SheetHeight_ = parseFloat(document.getElementById("ptn-sheet-height").value);
	if(_SheetHeight_ <= 0 || isNaN(_SheetHeight_))
		alert("Sheet Height must be bigger than 0cm!\rChanged to 20cm");

	let _SheetEdgeClearanceTop_ = parseFloat(document.getElementById("ptn-margin-top").value);
	if(_SheetEdgeClearanceTop_ < 0 || isNaN(_SheetEdgeClearanceTop_))
		alert("Sheet Edge Clearance Top must be bigger than 0cm!\rChange to 0cm");

	let _SheetEdgeClearanceLeft_ = parseFloat(document.getElementById("ptn-margin-left").value);
	if(_SheetEdgeClearanceLeft_ < 0 || isNaN(_SheetEdgeClearanceLeft_))
		alert("Sheet Edge Clearance Left must be bigger than 0cm!\rChange to 0cm");

	let _SheetEdgeClearanceRight_ = parseFloat(document.getElementById("ptn-margin-right").value);
	if(_SheetEdgeClearanceRight_ < 0 || isNaN(_SheetEdgeClearanceRight_))
		alert("Sheet Edge Clearance Right must be bigger than 0cm!\rChange to 0cm");

	let _SheetEdgeClearanceBottom_ = parseFloat(document.getElementById("ptn-margin-bot").value);
	if(_SheetEdgeClearanceBottom_ < 0 || isNaN(_SheetEdgeClearanceBottom_))
		alert("Sheet Edge Clearance Bottom must be bigger than 0cm!\rChange to 0cm");

	let BareLength = _BareLength_>=0?_BareLength_:123;
	let BareHeight = _BareHeight_>=0?_BareHeight_:103;
	let SheetMinLength = _SheetMinLength_>=0?_SheetMinLength_:15;
	let SheetMinHeight = _SheetMinHeight_>=0?_SheetMinHeight_:15;
	let SheetLength = _SheetLength_>=0?_SheetLength_:30;
	let SheetHeight = _SheetHeight_>=0?_SheetHeight_:20;
	let SheetEdgeClearanceTop = _SheetEdgeClearanceTop_>=0?_SheetEdgeClearanceTop_:0;
	let SheetEdgeClearanceLeft = _SheetEdgeClearanceLeft_>=0?_SheetEdgeClearanceLeft_:0;
	let SheetEdgeClearanceRight = _SheetEdgeClearanceRight_>=0?_SheetEdgeClearanceRight_:0;
	let SheetEdgeClearanceBottom = _SheetEdgeClearanceBottom_>=0?_SheetEdgeClearanceBottom_:0;

	let SheetTotalLength = SheetLength + SheetEdgeClearanceLeft + SheetEdgeClearanceRight;
	let SheetTotalHeight = SheetHeight + SheetEdgeClearanceTop + SheetEdgeClearanceBottom;

	if(BareLength <= SheetLength)
		alert("Sheet length must be smaller than PCB raw materal length!");
	else if(BareHeight <= SheetHeight)
		alert("Sheet height must be smaller than PCB raw materal height!");
	else if(SheetTotalLength <= SheetMinLength)
		alert("Sheet length must be bigger than " + SheetMinLength + "cm");
	else if(SheetTotalHeight <= SheetMinHeight)
		alert("Sheet height must be bigger than " + SheetMinHeight + "cm");
	else
		eel.plot_partitioner(BareLength, BareHeight, SheetTotalLength, SheetTotalHeight);


}
