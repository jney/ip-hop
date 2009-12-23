window.onload = function () {
  
  var centerX = function(e){
    return (400 - (e.getBBox().width/2)); 
  }
  
  var r = Raphael("holder", 800, 300),
    str = r.
      print(0, 100, currentIp, r.getFont("C39HrP24DhTt"), 100).
      attr({fill: "#000", opacity:.25, scale: ".1,.1" });
    str.translate(centerX(str), 0);

  var odd = true;
  
  (function(pos){
    var args = arguments;
    
    if(pos==(str.length)){
      odd = !odd;
      pos = 0;
    }
    
    if (odd) {
      str[pos].animate({opacity:1}, 200, function(){
        var that = this;
        setTimeout(function(){that.animate({opacity:.5}, 200)}, 0);
        args.callee(pos+1);
      });
    } else {
      str[pos].animate({opacity:1}, 200, function(){
        var that = this;
        setTimeout(function(){that.animate({opacity:.25}, 200)}, 0);
        args.callee(pos+1);
      });
    }
  })(0);
    
  // var mouseOut = function(){
  //   button.attr({fill: "#eee"});
  //   buttonLabel.attr({fill: "#555"});
  //   button.node.style.cursor = "pointer";
  //   buttonLabel.node.style.cursor = "pointer";
  // }
  // 
  // var mouseOn = function(){
  //   button.attr({fill: "#ccc"});
  //   buttonLabel.attr({fill: "#000"});
  // }
  // 
  // var click = function(){
  //   var text = currentIp;
  //   
  //   if(window.clipboardData) {  
  //     window.clipboardData.setData('text', text);  
  //   } else {
  //     var clipboarddiv = document.getElementById('divclipboardswf');  
  //     if(clipboarddiv == null) {
  //       clipboarddiv = document.createElement('div');  
  //       clipboarddiv.setAttribute("name", "divclipboardswf");  
  //       clipboarddiv.setAttribute("id", "divclipboardswf");  
  //       document.body.appendChild(clipboarddiv);
  //     }
  //     clipboarddiv.innerHTML =
  //       '<embed src="/swf/clipboard.swf" FlashVars="clipboard=' +
  //       encodeURIComponent(text) +
  //       '" width="0" height="0" type="application/x-shockwave-flash"></embed>';
  //   }
  //   
  //   return false;
  // }
  // 
  // var button = r.rect(350, 200, 100, 40, 10).
  //   attr({fill: "#eee", "stroke-width":0}).
  //   hover(mouseOn, mouseOut);
  // 
  // var buttonLabel = r.
  //   text(400, 220, "copy to clipboard").
  //   attr({fill: "#888"}).
  //   toFront().
  //   hover(mouseOn, mouseOut);
  //   
  // button.node.onclick = click;  
  // buttonLabel.node.onclick = click;
};
