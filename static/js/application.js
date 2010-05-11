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
  
  (function (pos) {
    var args = arguments;
    
    if (pos==(str.length)) {
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
  
  //
  var clip = new ZeroClipboard.Client();
  clip.setText(currentIp);
  clip.setCSSEffects( true );
  clip.glue('d_clip_button');
  
};
