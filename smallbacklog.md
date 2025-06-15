# Backlog
# Introduction

This backlog serves to keep track of what needs to be done. Also, it serves as an specification tracker of sorts.
Thats that.

# DONE!
Items on done are finished, meaning they got the tests AND the code AND the code passes the tests. For simplicity sake, 

| ID | ITEM | DESCRIPTION |
| -- | ---- | ----------- |
|    |  NOT |  DONE!      |


# TODO
Every item on the todo list has an id. Every time an item gets completed, it should be moved to the DONE list

| ID     | ITEM                               | DESCRIPTION                                                                                  |
|--------|------------------------------------|-------------                                                                                 |
| TD01   | SALARY                             | THE USER SHOULD BE ABLE TO REGISTER AND GET BACK HIS SALARY                                  |
| TD02   | SOCIAL SECURITY OR PRIVATE PENSION | THE USER SHOULD BE ABLE TO REGISTER HIS PENSION OR SOCIAL SECURITY AND ASSOCIATED DEDUCTIONS |
| TD03   | DEPENDANT                          | THE USER SHOULD BE ABLE TO REGISTER ONE OR MORE DEPENDANTS AND GET ASSOCIATED DEDUCTIONS     |

# SPECIFICATION
This contains an specification of the items.

## TD01 - SALARY
THE USER MUST BE ABLE TO STORE HIS SALARY
ADDITIONAL SALARY AND TAXABLE INCOME MUST BE SUMMED TO THE INITIAL SALARY OR INCOME
THE INITIAL REGISTERED INCOME MUST BE 0. 

## TD02 - PENSION
THE USER MUST BE ABLE TO STORE HIS PENSION
A NEW PENSION OVERWRITES THE OLD PENSION

## TD03 - DEPENDANTS
THE USER MUST BE ABLE TO STORE AND RETRIEVE HIS DEPENDANTS.
(FOR SIMPLICITY SAKE) EVERY DEPENDANT GENERATES A 150 UNIT REDUCTION.