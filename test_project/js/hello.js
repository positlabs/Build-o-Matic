// COMPILED SCRIPTS

// Original file: _FJ.js
var FJ=FJ||{};FJ.NOTIF_EVENT="fjEvent",FJ.NOTIF_NAVIGATION="fjNavigation",FJ.MSG_NAVIGATE="fjNavigate",FJ.MSG_NAVIGATE_UNDO="fjNavigateUndo",FJ.MSG_NAVIGATE_REDO="fjNavigateRedo";
// Original file: CSSxFormBehavior.js
/*

 This behavior (optionally) extends an existing object (reverse inheritance) so it will be able to control a dom element.

 To access these methods, use controller.transform.*

 @author josh beckwith

 @param element - the DOM element to be affected
 @param controller - object used to make calls
 @return - the controller


 */FJ.CSSxFormBehavior=function(e,t){function u(){e.style[i+"transform"]=s.toString()}t=t||{},t.transform={};var n=t.transform,r=FJ.Capabilities.csstransforms,i=FJ.Capabilities.vendor,s={translateZ:undefined,translateX:undefined,translateY:undefined,skewX:undefined,skewY:undefined,scaleX:undefined,scaleY:undefined,rotate:undefined,toString:function(){var e="";for(var t in this)this[t]!=undefined&&typeof this[t]!="function"&&(e+=t+"("+this[t]+") ");return e}};FJ.Capabilities.csstransforms3d&&(s.translateZ=0);var o=new FJ.Point("50%","50%");return FJ.define(n,"origin",function(){return o},function(t){o.x=t.x,o.y=t.y,e.style[i+"transform-origin"]=o.x+" "+o.y}),r?(n.translate=function(e,t,n){s.translateX=e+"px",s.translateY=t+"px",n&&(s.translateZ=n+"px")},FJ.define(n,"x",function(){return s.translateX=s.translateX||"0",parseFloat(s.translateX.split("px")[0])},function(e){s.translateX=e+"px",u()}),FJ.define(n,"y",function(){return s.translateY=s.translateY||"0",parseFloat(s.translateY.split("px")[0])},function(e){s.translateY=e+"px",u()}),FJ.define(n,"z",function(){return s.translateZ=s.translateZ||"0",parseFloat(s.translateZ.split("px")[0])},function(e){s.translateZ=e+"px",u()})):(n.translate=function(t,n){e.style.marginLeft=t+"px",e.style.marginTop=n+"px"},FJ.define(n,"x",function(){return parseFloat(e.style.marginLeft.split("px")[0])},function(t){e.style.marginLeft=t+"px"}),FJ.define(n,"y",function(){return parseFloat(e.style.marginTop.split("px")[0])},function(t){e.style.marginTop=t+"px"})),FJ.define(n,"rotation",function(){return s.rotate=s.rotate||"0",parseFloat(s.rotate.split("deg")[0])},function(e){s.rotate=e+"deg",u()}),n.scale=function(e,t){s.scaleX=e,s.scaleY=t,u()},FJ.define(n,"scaleX",function(){return s.scaleX=s.scaleX||"1",parseFloat(s.scaleX)},function(e){s.scaleX=e,u()}),FJ.define(n,"scaleY",function(){return s.scaleY=s.scaleY||"1",parseFloat(s.scaleY)},function(e){s.scaleY=e,u()}),n.skew=function(e,t){s.skewX=e+"deg",s.skewY=t+"deg",u()},FJ.define(n,"skewX",function(){return parseFloat(s.skewX.split("deg")[0])},function(e){s.skewX=e+"deg",u()}),FJ.define(n,"skewY",function(){return parseFloat(s.skewY.split("deg")[0])},function(e){s.skewY=e+"deg",u()}),t},FJ.Point=function(e,t,n){this.x=e,this.y=t,this.z=n||0};
// Original file: Router.js
FJ.Router=new function(){"use strict";var e=this,t=" ",n=100,r=document.location.href,i=r.indexOf("#"),s=i>0?r.substring(0,i):r,o=function(){var e=r.indexOf("#"),n=r.substring(e+2);return e>0&&e!=r.length-1?n:t},u=function(e){FJ.Application.slug=e,r=s+"#/"+e,document.location.href=r};this.start=function(i){t=i,e.navigateBySlug=new FJ.Notification(FJ.MSG_NAVIGATE,FJ.NOTIF_NAVIGATION,o()),setInterval(function(){document.location.href!=r&&(r=document.location.href,e.navigateBySlug.slug=o(),FJ.Application.broadcast(e.navigateBySlug))},n)},this.init=function(){FJ.Application.createMediator("router").update=function(e){e.type==FJ.NOTIF_NAVIGATION&&u(e.slug)}}};
