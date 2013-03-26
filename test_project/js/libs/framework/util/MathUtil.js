FJ.MathUtil = {

    step: function(e, t) {
        return (t >= e) ? 1 : 0;
    },

    clamp: function(s, e, t) {
        if (t < s) return s;
        if (t > e) return e;
        return t;
    },

    smoothStep: function(e0, e1, t) {
        if (t <= e0) return e0;
        if (t >= e1) return e1;

        t = (t - e0) / (e1 - e0);

        return e0 + (e1 - e0) * (3 * t * t - 2 * t * t * t);
    },

    easeQuadInOut: function(e0, e1, t) {
        if (( t *= 2 ) < 1) return e0 + (e1 - e0) * 0.5 * t * t;
        return e0 + (e1 - e0) * (- 0.5 * ( --t * ( t - 2 ) - 1 ));
    }

}