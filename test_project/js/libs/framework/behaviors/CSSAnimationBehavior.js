FJ.CSSAnimationBehavior = function(view) {

    view.animation = {};

    var a = view.animation;
    var s = view.div.style;

    var vendor = FJ.Capabilities.vendor;

    a.set = function (name, time, ease, delay, callback, fillMode) {

        delay = delay || 0;

        var t = (time + delay) * 1000;

        var ap = name + ' ' + time + 's ' + ease + ' ' + delay + 's';
        s[vendor + 'animation'] = ap;

        if (fillMode) {
            var afm = fillMode;
            s[vendor + 'animation-fill-mode'] = afm;
        }

        setTimeout(callback, t);
    };

    a.reset = function() {
        s[vendor + 'animation'] = '';
        s[vendor + 'animation-fill-mode'] = '';
    }

    return a;
}