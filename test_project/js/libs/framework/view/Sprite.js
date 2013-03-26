FJ.View = function(container, tag) {
    "use strict";

    if(tag) console.log("WARNING. Calling FJ.View with possibly deprecated argument: " + tag);

    var _that = this;

    var _container = container;// || document.body;
    this.div = document.createElement(tag || 'div');

    FJ.ElementWrapper.call(this);

    this.show = function() {
        if (!_that.visible) _container.appendChild(_that.div);
        _that.visible = true;
    };

    this.hide = function() {
        if (_that.visible) _container.removeChild(_that.div);
        _that.visible = false;
    };

    this.add = function() {
        for (var i = 0; i < arguments.length; i++) {
            var d = arguments[i];
            d.visible = true;
            if (!this.contains(d)) this.div.appendChild(d.div);
        }
    }

    this.contains = function(d) {
        return d.div.parentNode == this.div;
    }

    this.remove = function() {
        for (var i = 0; i < arguments.length; i++) {
            var d = arguments[i];
            d.visible = false;
            if (this.contains(d)) this.div.removeChild(d.div);
        }
    }



    // implementing css transform and transition methods
    new FJ.CSSxFormBehavior(this.div, this);
    new FJ.CSSTransitionBehavior(this.div, this);

    // To implement
    // update function?

};

FJ.View.prototype = new FJ.ElementWrapper();
FJ.View.prototype.constructor = FJ.ElementWrapper;
