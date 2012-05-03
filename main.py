#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('Hello world!')

class Guestbook(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('<html><body>You wrote:<pre>')
        self.response.out.write(self.request)
        self.response.out.write('\n\n')
        self.response.out.write(dir(self.request))
        self.response.out.write('\n\n')
        self.response.out.write(str(self.request.params))
        self.response.out.write('\n\n')
        for key, value in self.request.params.items():
	        self.response.out.write(cgi.escape('%s=%s\n' % (key, value)))
        self.response.out.write('</pre></body></html>')

URI_LIST = [
	('/',		MainHandler),
	('/sign',	Guestbook),
]

app = webapp2.WSGIApplication(URI_LIST, debug=True)
