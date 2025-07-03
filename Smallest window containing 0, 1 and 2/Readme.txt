Given a string S of size N consisting of the characters 0, 1 and 2, the task is to find the length of the smallest 
substring of string S that contains all the three characters 0, 1 and 2. If no such substring exists, then return -1.

Input: S = "01212"
Output: 3
Explanation: The substring 012 is the smallest substring that contains the characters 0, 1 and 2.

Input:  S = "12121"
Output: -1
Explanation:  As the character 0 is not present in the string S, therefore no substring containing 
all the three characters 0, 1 and 2 exists. Hence, the answer is -1 in this case.

[Approach - 1] Index Tracking - O(n) Time and O(1) Space
Keep track of the last seen indices of '0', '1', and '2' while iterating through the string. Once all three characters are found, compute the substring length as the difference between the maximum and minimum of the three indices. Update the minimum length found and return the result.

[Approach - 2] Using a sliding window - O(n) Time and O(1) Space
Use two pointers (i and k) and a frequency array to track the count of '0', '1', and '2'. Expand the window by moving k, and when all three characters are present, shrink it from the left (i) to maintain the smallest valid substring. Return the minimum length found.