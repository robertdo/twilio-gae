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

# Import the webapp2 framework, the Mail API, and Twilio Rest Client
import webapp2
from google.appengine.api import mail
from twilio.rest import TwilioRestClient

account = "ACXXXXXXXXXXXXXXXXX"
token = "YYYYYYYYYYYYYYYYYY"
client = TwilioRestClient(account, token)

# This is the handler that gets called when your app is visited
class SendEmail(webapp2.RequestHandler):
  def get(self):
    # Get the recipient from the text message.
    # The recipient is the body of the text message.
    recipient = self.request.get('Body')
    # Create the email and assign its attributes
    message = mail.EmailMessage()
    # Identify the sender or the From address of the email
    # You should change this to the email you created this app with
    message.sender="Your Name <youremail@gmail.com>"
    message.subject="This email was sent by Twilio"
    message.to = recipient
    message.body = """
    This is an email that is being sent to you from the sample app.
    """
    # Send the email
    message.send()
    # Send the SMS confirmation
    # Get the number of the SMS sender
    sms_sender = self.request.get('From')
    sms = client.sms.messages.create(to=sms_sender, from_="+5555555555",
                                     body="Your email has been sent to %s" % recipient)

app = webapp2.WSGIApplication([
  ('/', SendEmail)
], debug=True)
