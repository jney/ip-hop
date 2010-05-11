#!/usr/bin/env python

import wsgiref.handlers

from google.appengine.ext import webapp
from os import environ
import re

class MainHandler(webapp.RequestHandler):

  def get(self):
    format = self.request.get('format') or "html"
    
    if format == "html":
      if re.search('^curl.*', self.request.headers['User-Agent']):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(environ['REMOTE_ADDR'])
      else:
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write("""<!DOCTYPE html>
<?xml version="1.0" encoding="UTF-8"?>
<html>
  <head>
    <title>ip-hop</title>
    <meta name="description" content="Just know your public ip address">
    <meta name="keywords" content="ip-address ipaddress adresse address ip">
    <meta name="Robots" content="index, follow">
    <meta name="Revisit-After" content="15 days">
    <meta name="Rating" content="General">
    <meta name="Distribution" content="Global">
    <meta name="Identifier-url" content="http://www.ip-hop.com">
    <link href="/css/style.css" media="screen" rel="stylesheet" type="text/css" />
    <script src="/js/raphael-min.js" type="text/javascript"></script>
    <script src="/js/font.js" type="text/javascript"></script>
    <script src="/zeroclipboard/ZeroClipboard.js" type="text/javascript"></script>
    <script type="text/javascript">
      ZeroClipboard.setMoviePath( '/zeroclipboard/ZeroClipboard.swf' );
      var currentIp='%s';
    </script>
    <script src="/js/application.js" type="text/javascript"></script>
  </head>
  <body>
    <section>
      <div id="holder"><noscript>%s</noscript></div>
      <div id="d_clip_button">COPY</div>
    </section>
    <script type="text/javascript"> 
      var _gaq = _gaq || [];
      _gaq.push(['_setAccount', 'UA-3988705-4']);
      _gaq.push(['_trackPageview']);

      (function () {
        var ga = document.createElement('script');
        ga.src = ('https:' == document.location.protocol ?
            'https://ssl' : 'http://www') +
            '.google-analytics.com/ga.js';
        ga.setAttribute('async', 'true');
        document.documentElement.firstChild.appendChild(ga);
      })();
    </script>
  </body>
</html>""" % (environ['REMOTE_ADDR'],environ['REMOTE_ADDR']))
    elif format == "xml":
      self.response.headers['Content-Type'] = 'text/xml'
      self.response.out.write("""<?xml version='1.0' encoding="UTF-8"?>
<current-ip>%s</current-ip>
""" % (environ['REMOTE_ADDR']))
    elif format == "json":
      self.response.headers['Content-Type'] = 'text/json'
      self.response.out.write("{currentIp:'%s'}" % (environ['REMOTE_ADDR']))
    elif format == "txt":
      self.response.headers['Content-Type'] = 'text/plain'
      self.response.out.write(environ['REMOTE_ADDR'])
    else:
      self.response.headers['Content-Type'] = 'text/plain'
      self.response.out.write("Error: format '%s' is not supported" % (format))
  
def main():
  application = webapp.WSGIApplication([('/', MainHandler)],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
