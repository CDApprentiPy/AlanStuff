# Week 2 - Wednesday

## Daily Schedule
9  am - Algorithms
10 am - Lecture: 
11 am - Group Work
12 pm - Luncheon
1  pm - Lecture: TDD
2  pm - Open
3  pm - Open
4  pm - Demo
5  pm - EOD Check In

### Lectures
- AM: None, work on stuff
- PM: TDD! make our code better?
    - Things to make our code more maintainable and easier to use
        - Comments
        - Naming conventions
        - Style
        - Assertions
        
        - Testing
    - Comments, Convention, and Style
        - Avoid repeating yourself
        - PEP  for Python stylings
            - https://www.python.org/dev/peps/pep-0008/
            - https://www.python.org/dev/peps/pep-0257/
            - https://www.python.org/dev/peps/pep-0484/
            - http://barry.warsaw.us/software/STYLEGUIDE.txt
    - Logging
        - What & Why
            - That thing we do to debug/see stuff 
            - looks sloppy in production code, what if there was a systematic way to log things?
        - How
            - display formatting
            - debug.logging('your debugging thing here')
    - Assertions
        - What
            - A quick statement of 'this is what it should be'
        - Why
            - Use it to check conditions, or to validate that they are as they should be. Examples would be checking pre and post conditions of functions. Can be turned off with a optimization flag in compiling
        - How
            - assert(stuff, things)
    - High level: What is testing and why do we do it?
        - Why don't we do it more?
        - Pros:
            - helps working in teams
            - dev methodology, it can provide direction
            - makes app more robust
            - can help pinpoint issues
        - Cons:
            - slows you down
            - not super engaging
        - Basics:
            - Python testing, something easy
                - import unittest
            - Front-End testing
                - what is selenium
            - Flask testing
                - flask_test
            - Testing with DB
                - hao?