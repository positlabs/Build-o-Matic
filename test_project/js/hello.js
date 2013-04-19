// COMPILED SCRIPTS

// Original file: Notification.js
FJ.Notification=function(e,t,n){if(!e)throw"NOTIFICATION ERROR. Message cannot be null";if(t==FJ.NOTIF_NAVIGATION&&!n)throw"NOTIFICATION ERROR. Navigation type notifications require a slug";this.message=e,this.vars=null,this.type=t||FJ.NOTIF_EVENT,this.slug=n||"",this.action=null,this.postAction=null;var r=this;this.send=function(){FJ.Application.broadcast(r)}};
// Original file: Mediator.js
FJ.Mediator=function(e){this.name=e,this.notify=function(e){this.update&&this.update(e)}};
// Original file: Router.js
FJ.Router=new function(){"use strict";var e=this,t=" ",n=100,r=document.location.href,i=r.indexOf("#"),s=i>0?r.substring(0,i):r,o=function(){var e=r.indexOf("#"),n=r.substring(e+2);return e>0&&e!=r.length-1?n:t},u=function(e){FJ.Application.slug=e,r=s+"#/"+e,document.location.href=r};this.start=function(i){t=i,e.navigateBySlug=new FJ.Notification(FJ.MSG_NAVIGATE,FJ.NOTIF_NAVIGATION,o()),setInterval(function(){document.location.href!=r&&(r=document.location.href,e.navigateBySlug.slug=o(),FJ.Application.broadcast(e.navigateBySlug))},n)},this.init=function(){FJ.Application.createMediator("router").update=function(e){e.type==FJ.NOTIF_NAVIGATION&&u(e.slug)}}};
