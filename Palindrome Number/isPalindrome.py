'''
Level: Easy
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:

        array_of_int = list(str(x)) # Converts intteger into a string and then into a list of characters
        rightIndex = 1
        for leftIndex in range(len(array_of_int)):
            left = array_of_int[leftIndex]
            right = array_of_int[len(array_of_int) - rightIndex]
            print(left, right)
            if left != right:
                return False

            rightIndex += 1
        return True

        # Follow up: Could you solve it without converting the integer to a string?


Solution().isPalindrome(121)