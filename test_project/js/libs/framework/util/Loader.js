var FJ = FJ || {};
FJ.Loader = FJ || {};

//TODO - error handling

FJ.Loader.loadJSON = function (path, onLoadedFunc) {

	var request = new XMLHttpRequest();
	request.open("GET", path);

	request.onreadystatechange = function () {
		if (request.readyState == 4) {
			onLoadedFunc(JSON.parse(request.responseText));
		}
	};

	request.send();
};

window.__loadCount = 0;
FJ.Loader.loadJSONP = function (url, callback) {

	var script = document.createElement("script");

	if(callback != undefined) url += "&callback=__loaded" + window.__loadCount;
	script.src = url;

	document.body.appendChild(script);

	if (callback != undefined) {
		window["__loaded" + window.__loadCount] = function (response) {
			callback(response);
		};
		window.__loadCount++;
	}

};

FJ.Loader.loadPlainText = function (path, onLoadedFunc) {

	var request = new XMLHttpRequest();
	request.open("GET", path);

	request.onreadystatechange = function () {
		if (request.readyState == 4) {
			onLoadedFunc(request.responseText);
		}
	};

	request.send();
};

FJ.Loader.loadScript = function (path, callback) {
	var sc = document.createElement("script");
	sc.onload = callback;
	sc.src = path;
	document.getElementsByTagName("head")[0].appendChild(sc);
};

FJ.Loader.loadLink = function(url, callback) {
	var fileref = document.createElement("link");
	fileref.setAttribute("rel", "stylesheet");
	fileref.setAttribute("type", "text/" + url.split(".")[1]);
	fileref.setAttribute("href", url);
	fileref.onload = callback;
	document.getElementsByTagName("head")[0].appendChild(fileref);
};

/*
 Loads all of the framework scripts. only use for dev purposes.
 @param root - base path of the framework
 */
FJ.Loader.loadFramework = function (root, callback) {

	// all of the framework scripts. omitting Loader.js for obvious reasons.
	var scripts = [
		"behaviors/CSSTransitionBehavior.js",
		"behaviors/CSSxFormBehavior.js",
		"core/Application.js",
		"core/EventDispatcher.js",
		"core/Mediator.js",
		"core/Notification.js",
		"core/Router.js",
		"util/display/DisplayUtil.js",
		"util/viewport/ViewportUtil.js",
		"util/Capabilities.js",
		"util/Extensions.js",
		"util/ImageDataUtil.js",
		"util/Slug.js",
		"util/modernizr.js",
		"util/VirtualScroll.js",
		"util/Define.js",
		"view/Sprite.js",
		"view/Template.js"
	];

	// have to load FJ.js first
	FJ.Loader.loadScript(root + "_FJ.js", function () {

		var toLoad = scripts.length;
		for (var i = 0; i < scripts.length; i++) {
			FJ.Loader.loadScript(root + scripts[i], function () {
				toLoad--;
				if (toLoad == 0) callback();
			});
		}
	});

};