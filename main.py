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
import os
import re
from string import letters

import webapp2
def page_builder(username ='',username_error='', password_error='', password_erroru='', email_error=''):
	header = """
	<!DOCTYPE html>
	<html>
		<body>
		<h2>User Signup</h2>"""
	

	body = """
	<form method='post'>

	<table>
		<tr>
			<td>Username</td>
			<td><input type='text' name='username' value='%(username)s'></td>
			<td style="color:red">%(username_error)s</td>
		</tr>
		<tr>
			<td>Password</td>
			<td><input type='password' name='password'></td>
			<td style="color:red">%(password_error)s</td>
		</tr>
		<tr>
			<td>Verify Password</td>
			<td><input type='password' name='verify'></td>
			<td style="color:red">%(password_erroru)s</td>
		</tr>
		<tr>
			<td>Email(optional)</td>
			<td><input type='text' name='email'></td>
			<td style="color:red">%(email_error)s</td>
		</tr>

	</table>
	<input type ='submit'>
	</form>
	"""
	footer ="""
	</body>
	</html>
	"""
	body = body %{"username":username,"username_error":username_error, "password_error":password_error, "password_erroru":password_erroru, "email_error":email_error}
	
	content = header+body+footer
	return content



USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return not email or EMAIL_RE.match(email)

class Signup(webapp2.RequestHandler):

    def get(self):
        content = page_builder("")
        self.response.write(content)

    def post(self):
        have_error = False
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')
        username_error=''
        password_error=''
        password_erroru=''
        email_error =''


       
        if not valid_username(username):
            username_error = "That's not a valid username."
            have_error = True

        if not valid_password(password):
            password_error = "That wasn't a valid password."
            have_error = True
        elif password != verify:
            password_erroru= "Your passwords didn't match."
            have_error = True

        if not valid_email(email):
            email_error = "That's not a valid email."
            have_error = True

        if have_error:
            self.response.write(page_builder(username,username_error,password_error,password_erroru,email_error))
        else:
            self.redirect('/welcome?username='+username)

	

class Welcome(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        content = page_builder()
        welcome= "<h2>Welcome,"+username+"!</h2>"

        if valid_username(username):
            self.response.write(welcome)
        else:
        	self.redirect('/')
   
    	

app = webapp2.WSGIApplication([
    ('/', Signup),
    ('/welcome',Welcome)
], debug=True)
