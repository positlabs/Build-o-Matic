/*

 FJ.Capabilities extends Modernizr.

 */


FJ.Capabilities = (function () {

	var c = {};

	if (Modernizr == undefined) throw Error("Modernizr is required");
//    for (var p in Modernizr) c[p] = Modernizr[p];

	c = Modernizr;

	var _vendor = "";
	var prefixes = ["o", "webkit", "moz", "ms"];
	var pfx = Modernizr.prefixed("transform").toLowerCase();
	for (var i = 0; i < prefixes.length; i++) {
		if (pfx.split("transform")[0] == prefixes[i]) _vendor = "-" + prefixes[i] + "-";
	}

	c.vendor = _vendor;

	return c;

})();
