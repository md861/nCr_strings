# nCr_strings
A python function to generate groups of all the possible pairings of the first N natural numbers. The code is a test example for how difficult it is to deal with poor scaling of computational complexities.
## Description:
There can be N different ways of grouping the first N natural numbers, and there are a total of ![2N](https://latex.codecogs.com/gif.download?2%5EN). For example, the first 4 numbers can be grouped as:
* **G0** = {NULL} has 1 member
* **G1** = {1,2,3,4} has 4 members
* **G2** = {12,13,14,23,24,34} has 6 members
* **G3** = {123,124,134,234} has 4 members
* **G4** = {1234} has 1 member
