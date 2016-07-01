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
import os
import jinja2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class BaseHandler(webapp2.RequestHandler):
    def render(self, html, values={}):
        template = JINJA_ENVIRONMENT.get_template(html)
        self.response.write(template.render(values))

class MainHandler(BaseHandler):
    def get(self):
        self.render("main.html")
        #self.response.write('moshimoshi, Hello world!')

class Resultpage(BaseHandler):
    def get(self):
        word1 = self.request.get('word1')
        word2 = self.request.get('word2')
        if word1 is None or word2 is None:
            self.redirect('/')
        len1=len(word1)
        len2=len(word2)
        for(a,b)in zip(word1,word2):
    #    if i<len1
            self.response.out.write(a)
            self.response.out.write(b)
    #        if j<len2
    #            self.response.out.write(word2[0])
    #            j+=1
    #            i+=1
    #        if j<len2
    #            j+=1
    #
    #    if(len(combine1)>len(combine2)):
    #        combine=combine1
    #    else:
    #        combine=combine2
    #    self.response.out.write(combine)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/result', Resultpage)
], debug=True)
