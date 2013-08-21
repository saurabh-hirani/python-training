python-training
===============

As a part of the Python month celebration for Pycon India 2013, I had conducted a Python training at CIT, Gubbi, Bangalore. 

Following is a brief summary of the training:

As it was an introductory session, I had planned accordingly and was doing 2 things - using http://anandology.com/python-practice-book/ (very good material for referring to while teaching) and using sample programs to teach the students. I covered upto Chapter 3 in the book and observed that it was better to go to the right depth rather than painting the picture broadly. 

The sample programs build upon each other - I have used a simple command line calculator as the base. The idea was to increase complexity gradually and tailor the programs to introduce new concepts in the limited time I had for the training.

Had written the entire code base in around 2 hours. So there may be scope for improvement and subtle changes. Feel free to build upon this work to teach others.

The code base contains the following sample programs under code/calc

1. c1.py
  - desc:  take num1, operation, num2 from command line and perform simple +, * or / 
  - usage: python c1.py 1 + 2 
  - scope for improvement: make it respect division by zero, make it check if the values provided are numbers.

2. c2.py 
  - desc:  same as c1.py
  - usage: same as c1.py
  - fixes:  checks if command line args are integers
  - scope for improvement: make it respect division by zero

3. c3.py
  - desc:  same as c1.py
  - usage: same as c1.py
  - fixes: c2.py fixes + checks for division by zero
  - scope for improvement: make it useable as a module

4. c4.py
  - desc:  same as c1.py
  - usage: same as c1.py
  - fixes: c3.py fixes + can be used as a module
  - scope for improvement: have separate functions for addition, multiplication, division which can be called separately
  - notes: c4.py has accompanying program - use_c4.py which shows sample import for c4.py

5. c5.py
  - desc:  same as c1.py
  - usage: same as c1.py
  - fixes: c5.py fixes + separate functions for addition, multiplication, division.
  - scope for improvement: create a dict with +, *, / as key and their corresponding functions as values and depending on the key - call the right function.

6. c6.py
  - desc:  same as c1.py
  - usage: same as c1.py
  - fixes: c6.py fixes + dict with +, *, / as keys and their corresponding functions as values.
  - scope for improvement: perform multiple operations e.g. python program_name.py "1 + 2,2 + 4"

7. c7.py 
  - desc: takes multiple operations on the command line, performs the operations and prints results for each operation
  - usage: python c7.py "1 + 2,2 * 4,12 / 7"  
  - fixes: c6.py fixes + ability to perform multiple operations
  - scope for improvement: does not strip the operations for trailing spaces e.g. python c7.py "1 + 2,  2 + 3, 3 * 4" will fail

8. c8.py
  - desc: same as c7.py
  - usage: same as c7.py but with support of stripping spaces. e.g python c8.py "1 + 2, 3 + 4,    12 / 7" will work
  - fixes: c7.py fixes + stripping spaces
  - scope for improvement: same operations appearing multiple times could be served from an in program cache 
    e.g. python c8.py "1 + 2, 123 * 2, 12 * 4, 123 * 2" has the operation "123 * 2" twice. If intermediate results are cached, they can be 
         served by the cache.

9. c9.py
  - desc: same as c8.py
  - usage: same as c8.py
  - fixes: c8.py fixes + serve results from cache if required
  - scope for improvement: decouple the calculation from the input - have a simple server which will perform calculation and a client which will
    read operations from a text file and send them to the server.  

10. c10_server.py 
  - desc: a simple tcp server running on 127.0.0.1:9000 which accepts calculation requests and replies with the response. Search for '127.0.0.1' in the
    program and update it to any other IP if its corresponding client is on a different machine.
  - usage: python c10_server.py 
  - fixes: c9.py fixes + act as a standalone server

11. c10_client.py
  - desc: client for c10_server.py - reads in an input file containing with one or more operation per line (see input.txt for example), sends them
    to the server on 127.0.0.1:9000. Search for '127.0.0.1' in the program and update it to any other IP if its corresponding server is on a different
    machine.
  - usage: python c10_client.py input.txt (requires that c10_server.py be already running)
