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