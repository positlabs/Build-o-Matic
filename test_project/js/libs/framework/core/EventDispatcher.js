/**
 * The EventDispatcher is typically used as a property of an objec t(i.e. compisition)
 * @param masterFunc this function will be invoked each time a listener is added or removed. Thanks to this the parten object can be notified if it has any listeners.
 */
FJ.EventDispatcher = function(masterFunc) {
    "use strict";

    var listeners = [];

    this.addEventListener = function(listener) {
        if (listeners.indexOf(listener) > -1) return;
        listeners.push(listener);
        if (masterFunc) masterFunc(listeners.length);
    }

    this.removeEventListener = function(listener) {
        var i = listeners.indexOf(listener);
        if (i < 0) {
            return null;
        } else {
            if (masterFunc) masterFunc(listeners.length - 1);
            return listeners.splice(i, 1);
        }

    }

    this.dispatch = function(event) {
        var nm = listeners.length;
        for (var i = 0; i < nm; i++) listeners[i](event);
    }

}