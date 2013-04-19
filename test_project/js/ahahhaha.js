// COMPILED SCRIPTS

// Original file: Notification.js
FJ.Notification=function(e,t,n){if(!e)throw"NOTIFICATION ERROR. Message cannot be null";if(t==FJ.NOTIF_NAVIGATION&&!n)throw"NOTIFICATION ERROR. Navigation type notifications require a slug";this.message=e,this.vars=null,this.type=t||FJ.NOTIF_EVENT,this.slug=n||"",this.action=null,this.postAction=null;var r=this;this.send=function(){FJ.Application.broadcast(r)}};
// Original file: Define.js
FJ.define=function(e,t,n,r){e[t]=function(e){if(e==undefined)return n();r&&r(e)}};
