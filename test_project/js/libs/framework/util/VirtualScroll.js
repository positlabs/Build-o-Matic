FJ.VirtualScroll = function(name) {

    var MULT = 2;

    var that = this;

    this.event = {

        scrollX: 0,
        scrollY: 0,

        deltaX: 0,
        deltaY: 0,

        maxDeltaX: 0,
        maxDeltaY: 0

    }

    var lastPageX = 0;
    var lastPageY = 0;
    var attached = false;
    var autoPilotMode = false, startX, startY, targetX, targetY, duration, t;

    this.dispatcher = new FJ.EventDispatcher(function(nl) {

        if (nl > 0 && !attached) {
            attach();
            attached = true;
        } else if (nl == 0 && attached) {
            detach();
            attached = false;
        }

    });

    var minX = null, maxX = null;
    var minY = null, maxY = null;

    this.limitX = function(min, max) {
        minX = min;
        maxX = max;
    }

    this.limitY = function(min, max) {
        minY = min;
        maxY = max;
    }

    this.reset = function() {
        that.setValue(0, 0);
    }

    this.setValue = function(x, y) {
        that.event.scrollX = x;
        that.event.scrollY = y;
        _dispatch();
    }
    
    this.scrollTo = function(x, y, d) {
        autoPilotMode = true;

        startX = that.event.scrollX;
        startY = that.event.scrollY;

        targetX = x;
        targetY = y;

        // 30 frames = roughyl 0.5s by default (but it could be estimated based on distance-to-travel)
        duration = d || 30;
        t = 0;


        FJ.FrameImpulse.addEventListener(autoScroll);
    }

    var autoScroll = function() {
        t++;

//        var dx = FJ.MathUtil.smoothStep(startX, targetX, startX + (targetX - startX) * (t / duration));
//        var dy = FJ.MathUtil.smoothStep(startY, targetY, startY + (targetY - startY) * (t / duration));

        var dx = FJ.MathUtil.easeQuadInOut(startX, targetX, t / duration);
        var dy = FJ.MathUtil.easeQuadInOut(startY, targetY, t / duration);

        _set(dx - that.event.scrollX, dy - that.event.scrollY);

        if (t >= duration) {
            FJ.FrameImpulse.removeEventListener(autoScroll);
            autoPilotMode = false;
        }
    }

    var _set = function(dx, dy) {
        that.event.scrollX += dx;
        that.event.scrollY += dy;

        that.event.maxDeltaX = Math.max(that.event.maxDeltaX, Math.abs(dx));
        that.event.maxDeltaY = Math.max(that.event.maxDeltaY, Math.abs(dy));

        that.event.deltaX = dx;
        that.event.deltaY = dy;

        _dispatch();
    }

    // window.addWheelListener might wrap the callback function into another one, so keep a reference to it for removing the listener later...
    var onWheelCallback;

    var _dispatch = function() {

        if (minX != null) that.event.scrollX = Math.max(that.event.scrollX, minX);
        if (maxX != null) that.event.scrollX = Math.min(that.event.scrollX, maxX);

        if (minY != null) that.event.scrollY = Math.max(that.event.scrollY, minY);
        if (maxY != null) that.event.scrollY = Math.min(that.event.scrollY, maxY);

        that.dispatcher.dispatch(that.event);
    }

    var attach = function() {
//        if (FJ.Capabilities.isTouch) {
          if (FJ.Capabilities.touch) {

		        document.addEventListener('touchstart', function(e) {
                lastPageX = 0;
                lastPageY = 0;
            }, false);

            document.addEventListener('touchmove', function(e) {
                e.preventDefault();

                if (autoPilotMode) {
                    FJ.FrameImpulse.removeEventListener(autoScroll);
                    autoPilotMode = false;
                }

                if (lastPageX != 0) {
                    _set(
                        -(e.targetTouches[0].pageX - lastPageX),
                        -(e.targetTouches[0].pageY - lastPageY)
                    );
                }

                lastPageX = e.targetTouches[0].pageX;
                lastPageY = e.targetTouches[0].pageY;

            }, false);
        } else {
            onWheelCallback = addWheelListener(document, function(e) {
                if (autoPilotMode) {
                    FJ.FrameImpulse.removeEventListener(autoScroll);
                    autoPilotMode = false;
                }

                _set(e.deltaX * MULT, e.deltaY * MULT);
            }, false);
        }
    }

    var detach = function() {
        removeWheelListener(document, onWheelCallback);
    }
};