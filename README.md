# nCr_strings
A python function to generate groups of all the possible pairings of the first N natural numbers. The code is a test example for how difficult it is to deal with computational complexities.
## Description:
There can be N+1 different ways of grouping the first N natural numbers, and there are a total of ![](https://latex.codecogs.com/gif.latex?2%5EN) members in the groups. For example, the first 4 numbers can be grouped as:
* **G0** = {NULL} has 1 member
* **G1** = {1,2,3,4} has 4 members
* **G2** = {12,13,14,23,24,34} has 6 members
* **G3** = {123,124,134,234} has 4 members
* **G4** = {1234} has 1 member

and make a total of 1+4+6+4+1 = 16 = ![](https://latex.codecogs.com/gif.latex?2%5E4) members. Thus, this code has a growth rate of ![](https://latex.codecogs.com/gif.latex?O%282%5EN%29). Using this function, one would quickly realize that these groups would become increasingly difficult to calculate!
