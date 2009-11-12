#!/usr/bin/env python

import wsgiref.handlers

from google.appengine.ext import webapp
from os import environ

class MainHandler(webapp.RequestHandler):

  def get(self):
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
    <script type="text/javascript">currentIp='%s'</script>
    <script src="/js/application.js" type="text/javascript"></script>
  </head>
  <body>
    <section>
      <div id="holder"></div>
    </section>
  </body>
</html>""" % (environ['REMOTE_ADDR']))


def main():
  application = webapp.WSGIApplication([('/', MainHandler)],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
