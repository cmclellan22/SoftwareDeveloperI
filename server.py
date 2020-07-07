##################################################################
## Filename: server.py
## Desc:  Server script for accepting JSON requests with the appropriate keys
## Author:  McLellan, Christina
## References:  Uses a recursive function to search nested dictionaries done
##              as part of a previous project.
## Creation Date:  07/02/2020
##################################################################

from http.server import HTTPServer,BaseHTTPRequestHandler
import json

HOST_ADDRESS="127.0.0.1"

# using port 8000 - standard port many web servers are configured to listen on
HOST_PORT=8000

# This class RequestHandler is inheriting from the BaseHTTPRequestHandler
# reference: https://docs.python.org/3.8/library/http.server.html?highlight=basehttprequesthandler#module-http.server
# Three methods in the class are going to be overidden: send_response, do_GET, do_POST
class RequestHandler(BaseHTTPRequestHandler):

    def send_response(self,code,message=None):
        """ override to customize header """
        self.log_request(code)
        self.send_response_only(code)
        self.send_header('Server','python3 http.server Development Server')
        self.send_header('Date',self.date_time_string())
        self.end_headers()

    # This method accepts request to serve up files from the web server
    # The method is overidden so never actually makes it to the parent class
    def do_GET(self):
        """ response for a GET request """
        self.send_response(404)

    # This method from the parent class is being overridden so it intercepts the POST.
    # POST method is used when a client wants to send information TO a web server over http.
    # Parse the content in the form of a json object
    def do_POST(self):
        # Find out how long the content coming in is - a property of the header
        # Tells how many bytes in the payload to be read
        content_length = int(self.headers['Content-Length'])

        # Get the content (json object) and convert it to a python dictionary
        # use json.loads() function
        message = json.loads(self.rfile.read(content_length))

        # Print out the message so we can see it - for testing
        # print(message, "\n\n")

        # Create an empty list to hold 'is_malicious:true' if found from our search of the dictionary
        target_list = []

        # Call the recursive function to loop through the dictionary and find the key
        # Check if it is True and deep dive into any nested dictionaries created
        # by the json.loads() call above, representing children in a json object.
        # The function only returns key:value pairs as strings, that match the key and
        # value provided in the second and third argument

        # Lists are mutable so passing a list to a function will change the list in memory
        self.get_target_values(message, "is_malicious", "true", target_list)

        # If there is a value in the list, it would be a key:value pair where the key == 'is malicious' and
        # value == 'true', so send Forbidden response (403)
        # If the list is empty, no malicious send OK response (200)
        if target_list != []:
            self.send_response(200)
        else:
            self.send_response(403)

    # Recursive function
    # If we find any value that is true we can break - we know
    # that we will deny this request - no need to search any further.
    def get_target_values(self, payload, target_key, target_val, vals):
        for key, value in payload.items():
            if type(value) is dict:
                self.get_target_values(value, target_key, target_val, vals)
            else:
                if key == target_key and value == target_val:
                    vals.append(str(str(key) + ":" + str(value)))
                    break

# As seen on docs.python.org
def run(server_class=HTTPServer,handler_class=BaseHTTPRequestHandler):
    server_address=(HOST_ADDRESS,HOST_PORT)
    httpd=server_class(server_address,handler_class)
    httpd.serve_forever()

if __name__=='__main__':
    run(handler_class=RequestHandler)
