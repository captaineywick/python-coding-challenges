# Challenge

## Plus One

You are given a large integer represented as an integer array `digits`, where each `digits[i]` is the i-th digit of the integer.  
The digits are ordered from most significant to least significant in left-to-right order.  
The large integer does not contain any leading 0's.  

Increment the large integer by one and return the resulting array of digits.  

Examples:
```bash
    Input: [1,2,3]
    Output: [1,2,4]
    Explanation: The array represents the integer 123.
    Incrementing by one gives 123 + 1 = 124.

    Input: [4,3,2,1]
    Output: [4,3,2,2]
    Explanation: The array represents the integer 4321.
    Incrementing by one gives 4321 + 1 = 4322.

    Input: [9]
    Output: [1,0]
    Explanation: The array represents the integer 9.
    Incrementing by one gives 9 + 1 = 10.
    
    Input: [9,9]
    Output: [1,0,0]
    Explanation: The array represents the integer 99.
    Incrementing by one gives 99 + 1 = 100.
````

Constraints:
* 1 <= digits.length <= 100
* 0 <= digits\[i] <= 9
* `digits` does not contain any leading 0's.
