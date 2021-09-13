- Currently, user_choice variable is declared but not used:
listed in Problems:
- local variable 'user_choice' is assigned to but never used

Unused variable 'user_choice' 

Unused variable 'row'

Unused variable 'col'

## Bug
- Currently, 
    - When program run4 py runs,
        - does not return anything after user name
- Root Cause:
    - start_game function not called
- Solution:
    - call start_game function in init_game function
- Effect: game runs

## Bug2
- Game does not know when board is full