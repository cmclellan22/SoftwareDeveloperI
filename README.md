# SoftwareDeveloperI - README.md

Author: McLellan, Christina

# ThreatX Coding Challenge

Scripted based on ThreatX-owned Repository: engineering-homework / software-developer-i /

# Summary:
The server.py script is a simple HTTP service written in Python hosted on the address 127.0.0.1 and port number 8000 that accepts requests and returns either 200 OK or 403 Forbidden, acting in some ways like a simple web application firewall. There is an assumption that malicious requests will announce their intent in the body of the request. The tester.py script was written as a means to test the correctness of responses, as well as response time to ensure at least ten requests could be handled per second.

Host Port:
The server is on the host port number 8000 because it is a rather standard port which servers are configured to listen on.

Libraries:
The script server.py includes imports from http.server, which are the HTTPServer library and the BASEHTTPRequestHandler library. The json library is also used, as we assume requests are received in json format. 

# Test Script:
The tester.py script contains five different Python dictionaries (payload1, payload2, payload3, payload4, payload5) which include different variations of test cases. They include a positive test case (malicious), a negative test case (non-malicious), a positive nested test case (malicious, but hidden), a null test case (non-malicious), and another negative test case (non-malicious). 

Each of the dictionaries are cycled through the server twice in order to track how many seconds the server takes to process ten requests. 

From the time library, the method perf_counter() is used to capture the time the test script starts and ends. The total time is then calculated and converted into seconds, rather than nanoseconds. (Tester.py has been ran over twenty-five times, and the total response time has not met or exceeded 0.1 second)

Libraries:
The script tester.py includes an import of the requests library, the json library, and the time library. 

# Potential Additions:
In order to monitor and troubleshoot the server if need be, I would recommend the addition of a process control system, specifically Supervisor. 
