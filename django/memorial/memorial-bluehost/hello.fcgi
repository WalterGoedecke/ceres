#!/usr/bin/python2.6
from fcgi import WSGIServer
def test_app(environ, start_response):
start_response('200 OK', [('Content-Type', 'text/plain')])
yield 'Hello, world!\n'

WSGIServer(test_app).run()
