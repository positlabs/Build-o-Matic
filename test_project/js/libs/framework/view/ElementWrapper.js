FJ.ElementWrapper = function(element) {

    var _that = this;

    if(element) _that.div = element;

    FJ.define(this, "id",
        function() {
            return _that.div.id
        },
        function(id) {
            _that.div.id = id;
        }
    );

    FJ.define(this, "class",
        function() {
            return _that.div.className
        },
        function(name) {
            _that.div.className = name;
        }
    );

    this.setDisplay = function(d) {
        _that.div.style.display = d;
    }

    this.opacity = function(o) {
        _that.div.style.opacity = o;
    }

    this.registerClick = function (f) {
        _that.div.addEventListener('click', f);
    };

    this.unRegisterClick = function (f) {
        _that.div.addEventListener('click', f);
    };

    //TODO - use a different method to compute dimensions
    // see https://github.com/jquery/jquery/blob/master/src/dimensions.js
    this.width = function() {
        return _that.div.offsetWidth;
    };
    this.height = function() {
        return _that.div.offsetHeight;
    };

    this.mouseEnabled = function(v) {
        _that.div.style['pointer-events'] = (v) ? 'auto' : 'none';
    }

}