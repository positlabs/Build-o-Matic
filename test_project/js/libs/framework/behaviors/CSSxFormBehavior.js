/*

 This behavior (optionally) extends an existing object (reverse inheritance) so it will be able to control a dom element.

 To access these methods, use controller.transform.*

 @author josh beckwith

 @param element - the DOM element to be affected
 @param controller - object used to make calls
 @return - the controller


 */

FJ.CSSxFormBehavior = function (element, controller) {
	controller = controller || {};
	controller.transform = {};
	var t = controller.transform;

	var cssTransforms = FJ.Capabilities.csstransforms;

	var vendor = FJ.Capabilities.vendor;


	var transforms = {
		translateZ:undefined,
		translateX:undefined,
		translateY:undefined,
		skewX:undefined,
		skewY:undefined,
		scaleX:undefined,
		scaleY:undefined,
		rotate:undefined,
		toString:function () {
			var props = "";
			for (var p in this) {
				if (this[p] != undefined && typeof this[p] !== "function")
					props += p + "(" + this[p] + ") ";
			}
			return props;
		}
	};

	if(FJ.Capabilities.csstransforms3d) transforms.translateZ = 0;

	var _origin = new FJ.Point("50%", "50%");
	FJ.define(t, "origin",
		function () {
			return _origin;
		},
		function (point) {
			_origin.x = point.x;
			_origin.y = point.y;
			element.style[(vendor + "transform-origin")] = _origin.x + " " + _origin.y;
		}
	);


	function setTransforms() {
		element.style[(vendor + "transform")] = transforms.toString();
	}

	if (cssTransforms) {

		t.translate = function (x, y, z) {
			transforms.translateX = x + "px";
			transforms.translateY = y + "px";
			if (z) transforms.translateZ = z + "px";
		};

		FJ.define(t, "x",
			function () {
				transforms.translateX = transforms.translateX || "0";
				return parseFloat(transforms.translateX.split("px")[0]);
			},
			function (x) {
				transforms.translateX = x + "px";
				setTransforms();
			});

		FJ.define(t, "y",
			function () {
				transforms.translateY = transforms.translateY || "0";
				return parseFloat(transforms.translateY.split("px")[0]);
			},
			function (y) {
				transforms.translateY = y + "px";
				setTransforms();
			}
		);

		FJ.define(t, "z",
			function () {
				transforms.translateZ = transforms.translateZ || "0";
				return parseFloat(transforms.translateZ.split("px")[0]);
			},
			function (z) {
				transforms.translateZ = z + "px";
				setTransforms();
			}
		);

	} else {

		t.translate = function (x, y) {
			element.style.marginLeft = x + "px";
			element.style.marginTop = y + "px";
		};

		FJ.define(t, "x",
			function () {
				return parseFloat(element.style.marginLeft.split("px")[0]);
			},
			function (x) {
				element.style.marginLeft = x + "px";
			}
		);

		FJ.define(t, "y",
			function () {
				return parseFloat(element.style.marginTop.split("px")[0]);
			},
			function (y) {
				element.style.marginTop = y + "px";
			}
		);

	}

	FJ.define(t, "rotation",
		function () {
			transforms.rotate = transforms.rotate || "0";
			return parseFloat(transforms.rotate.split("deg")[0]);
		},
		function (deg) {
			transforms.rotate = deg + "deg";
			setTransforms();
		}
	);

	t.scale = function (sx, sy) {
		transforms.scaleX = sx;
		transforms.scaleY = sy;
		setTransforms();
	};

	FJ.define(t, "scaleX",
		function () {
			transforms.scaleX = transforms.scaleX || "1";
			return parseFloat(transforms.scaleX);
		},
		function (sx) {
			transforms.scaleX = sx;
			setTransforms();
		}
	);

	FJ.define(t, "scaleY",
		function () {
			transforms.scaleY = transforms.scaleY || "1";
			return parseFloat(transforms.scaleY);
		},
		function (sy) {
			transforms.scaleY = sy;
			setTransforms();
		}
	);

	t.skew = function (x, y) {
		transforms.skewX = x + "deg";
		transforms.skewY = y + "deg";
		setTransforms();
	};

	FJ.define(t, "skewX",
		function () {
			return parseFloat(transforms.skewX.split("deg")[0]);
		},
		function (sx) {
			transforms.skewX = sx + "deg";
			setTransforms();
		});

	FJ.define(t, "skewY",
		function () {
			return parseFloat(transforms.skewY.split("deg")[0]);
		},
		function (sy) {
			transforms.skewY = sy + "deg";
			setTransforms();
		}
	);

	return controller;
};

FJ.Point = function (x, y, z) {
	this.x = x;
	this.y = y;
	this.z = z || 0;
};