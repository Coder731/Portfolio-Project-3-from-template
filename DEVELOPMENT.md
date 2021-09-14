- commit

- check git_ignore has node_modules/

- terminal run 
    - npm install index.js
    - accidental

- terminal run
    - npm install node index.js

- terminal upgrade recommended
    run
    - npm install -g npm

- Add DEVELOPMENT.md

- run py
    - cut line and indent for flask8 character count

## Step completed previously
Ensure keys are strings for dictionaries

## Get terminal user input working

Used code from https://techeplanet.com/python-read-input-from-terminal-stdin/ to test whether problem with typing in terminal was to do with configuration or code.
Code added (to run.py):
    name = input("Enter Name ")
    print("Name entered is : ",name)
    print(type(name))
Result:
    - Works
Conclusion:
    - Since this test code worked, the previous code is at fault.

## Next step

Add code to check if integer is used, using a while loop.


## Bug KeyError: 0
Solved Using:
- https://replit.com/~
- https://pythontutor.com/

- Code causing error:
    values = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5,
                "f": 6, "g": 7, "h": 8, "i": 9}

    print("\t| {} | {} | {} |".format(values[0], values[1], values[2]))

- Corrected Code used:
    values = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5,
                "f": 6, "g": 7, "h": 8, "i": 9}

    print("\t| {} | {} | {} |".format(values["a"], values["b"], values["c"]))

- Solution:
    - Change values key from 0 to "a" for first key


- Mentor Call 2
    - Received instruction on the following:
        - separate game into functions
        - use join method to make board display code more elegant
        - use row and column 
        - create function to switch symbol per player
        - use a space in a string for cells on table

- Game working
    - Issues
        - Consider Adding Basic Logic for Single Player
        - Add logic to tell:
            - if game is over
                - if board is full
                - if three in a row
        - Add logic for strategy
            - If two in a row block third
            - Block one square beside opponent symbol

- Add run5 py
    - Remove comments for ease of readability

- Currently,
    - counting matrix rows using numpy
    from site:
    # https://stackoverflow.com/questions/53101229/how-to-iterate-through-a-matrix-column-in-python

- Create run6.py from run5.py

- Create run7.py from run6.py 
    - run7.py is a shortened version of the file to focus on issue

- board is not a matrix but a list of lists

- run8_iterate.py
    - Error:
        - TypeError: list indices must be integers or slices, not list

    - Root Cause:
        - r in board
            - used in for loop
        - r is a list
            - r = [' ', ' ', ' ']