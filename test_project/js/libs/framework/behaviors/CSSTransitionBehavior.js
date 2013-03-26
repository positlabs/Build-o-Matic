/*
 This behavior (optionally) extends an existing object (reverse inheritance) so it will be able to control a dom element.

 To access these methods, use controller.transition.*

 @author josh beckwith

 @param element - the DOM element to be affected
 @param controller - object used to make calls
 @return - the controller
 */

FJ.CSSTransitionBehavior = function (element, controller) {
	controller = controller || {};
	controller.transition = {};
	var t = controller.transition;

	var vendor = FJ.Capabilities.vendor;
	var properties = {};

	function applyParams() {

		var strings = [];
		for (var p in properties) {
			var string = "";
			string += p + " ";
			string += properties[p].duration + "ms ";
			string += properties[p].delay + "ms ";
			string += properties[p].ease;
			strings.push(string)
		}

		element.style[(vendor + "transition")] = strings.join(",");
	}

	/*

	 @param name - name of the css property to affect.
	 @param duration - length of animation in milliseconds
	 @param delay - animation delay in milliseconds
	 @param easeFunc - name of function to be used for easing. Use FJ.ANIM constants, or FJ.ANIM.cubicBezier

	 */
	t.set = function (name, duration, delay, easeFunc) {
		properties[name] = {};
		properties[name].duration = duration || 300;
		properties[name].delay = delay || 0;
		properties[name].ease = easeFunc || FJ.ANIM.EASE;
		applyParams();
	};


	FJ.define(t, "properties",
		function () {
			return properties;
		}
	);

	return controller;
};


FJ.ANIM = {};

/*

 @params - can be 0-1
 @see http://www.roblaplaca.com/examples/bezierBuilder/

 */
FJ.ANIM.cubicBezier = function (n1, n2, n3, n4) {
	return "cubic-bezier(" + n1 + ", " + n2 + ", " + n3 + ", " + n4 + ")";
};
//TODO - convert these to cubic besier values so we can reverse them
FJ.ANIM.EASE_IN_OUT = "ease-in-out";
FJ.ANIM.EASE_OUT = "ease-out";
FJ.ANIM.EASE_IN = "ease-in";
FJ.ANIM.EASE = "ease";
FJ.ANIM.LINEAR = "linear";
