class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        for num in nums:
            if num-1 not in nums: #we have to start counting from first number of a consecutuve sequence. if previous num exists, just skip it and go with next num in for loop.
                streak=1 #if prev num doesnt exist, streak starts.
                current = num
                while current+1 in nums: #now keep on checking if next number exists while incrementing the current number and streak
                    streak+=1
                    current+=1
                longest = max(longest,streak) #once while loop ends, store the streak. for loop continues and longest gets updated when longer streak comes in
        return longest

