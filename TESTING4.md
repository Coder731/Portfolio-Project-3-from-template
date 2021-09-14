# Add the following code from this site:
    # https://www.includehelp.com/python/row-numbers-in-a-matrix.aspx
    import numpy as np

    # Use of np.array() to define a matrix
    V = np.array([[1,2,3],[2,3,5],[3,6,8],[323,623,823]])
    print("--The Matrix-- \n",V)

    # number of rows
    num = len(V)

    print("Number of rows in the Given Matrix : ", num)

# to count matrix rows

run:
    - python run5.py
    - note: error should have run python3 run5.py
error:
    - ModuleNotFoundError: No module named 'numpy'
run:
    - pip3 install numpy
warning:
    WARNING: You are using pip version 21.2.3; however, version 21.2.4 is available.
    You should consider upgrading via the '/home/gitpod/.pyenv/versions/3.8.11/bin/python3 -m pip install --upgrade pip' command.
run:
    - /home/gitpod/.pyenv/versions/3.8.11/bin/python3 -m pip install --upgrade pip
repeat error:
    WARNING: You are using pip version 21.2.3; however, version 21.2.4 is available.
    You should consider upgrading via the '/home/gitpod/.pyenv/versions/3.8.11/bin/python3 -m pip install --upgrade pip' command.
repeat run:
    /home/gitpod/.pyenv/versions/3.8.11/bin/python3 -m pip install --upgrade pip
returned:
    Requirement already satisfied: pip in /workspace/.pip-modules/lib/python3.8/site-packages (21.2.4)


## Bug
- in run6.py
    - in combo function 
    - print statement not working
- Attempted solution    
    - call function
- Solution
    - In progress

## Bug
Errors:
    - variable r undefined
    - variable c undefined
Plan:
    - 