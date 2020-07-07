##################################################################
## Filename: tester.py
## Desc:  Test script for server.py with variations of payload to 
##        test the consistency of correct responses and confirms
##        at least ten requests can be processed in one second.
## Author:  McLellan, Christina
## References:  Uses a recursive function to search nested dictionaries done
##              as part of a previous project.
## Creation Date:  07/02/2020
##################################################################
import requests
import json
import time

def main ():

    # URL for the post request
    url = 'http://127.0.0.1:8000'

    # Create  test payloads as Python Dictionaries
    # to be converted into JSON strings later.

    # Positive test case
    payload1 = {"sender": "Company X",
                 "is_malicious":"true",
                 "receiver": "Company Y"}

    # Negative test case
    payload2 = {"sender": "Company X",
                 "is_malicious":"false",
                 "receiver": "Company Y"}

    # Positive nested test case
    payload3 = {"sender": "Company X",
                 "is_malicious":"false",
                 "receiver": "Company Y",
                 "hidden":
                     { "is_malicious":"true"}
                 }

    # Negative null test case
    payload4 = {"sender": "Company X",
              "data": "null",
              "receiver": "Company Y"}

    # Negative test case
    payload5 = {"sender": "Company X",
              "data": "true",
              "receiver": "Company Y"}

    # Set the headers for the request
    headers = {'Content-type': 'application/json'}

    # Create a list to easily cycle through the test cases
    d_list = [payload1, payload2, payload3, payload4, payload5,
              payload1,payload2,payload3,payload4,payload5]

    # Validation test list
    answer_key = ['Forbidden,', 'OK,', 'Forbidden,', 'OK,', 'OK,', 'Forbidden,', 'OK,', 'Forbidden,', 'OK,', 'OK']

    # Using time.perf_counter to time 10 requests
    # Test should finish in less that 1 second.
    tic = time.perf_counter()

    # Cycle through all 10 test cases
    for d in d_list:
        # send the request to the server, using json.dumps() to dump the
        # dictionary to a json format.
        r = requests.post(url, json.dumps(d), headers=headers)
        # print out the response from the web server.  Should be OK or 200 for
        # cases that are False (non-malicious) and 403 for cases that are True
        #(malicious)
        print(r.status_code)

    # Stop the time
    toc = time.perf_counter()

    # Check the results against the correct responses
    print("Correct Responses: ", *answer_key)
    print(f"Requests x10 time: {toc - tic:0.4f} seconds")

if __name__ == '__main__':
    main()
