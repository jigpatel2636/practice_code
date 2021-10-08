'''
You are given an array of positive integers w where w[i] describes the weight of ith index (0-indexed).

We need to call the function pickIndex() which randomly returns an integer in the range [0, w.length - 1]. pickIndex() should return the integer proportional to its weight in the w array. For example, for w = [1, 3], the probability of picking the index 0 is 1 / (1 + 3) = 0.25 (i.e 25%) while the probability of picking the index 1 is 3 / (1 + 3) = 0.75 (i.e 75%).

More formally, the probability of picking index i is w[i] / sum(w).



Example 1:

Input
["Solution","pickIndex"]
[[[1]],[]]
Output
[null,0]

Explanation
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. Since there is only one single element on the array the only option is to return the first element.

https://leetcode.com/problems/random-pick-with-weight/

https://www.youtube.com/watch?v=skkJtFzePwQ&ab_channel=thecodingworld

'''
import random
class Solution:
    def __init__(self, w, l):
        self.prefix_sum = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sum.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self):
        random_int = self.total_sum * random.random()
        low, high = 0, len(self.prefix_sum)
        while low < high:
            mid = low + (high-low)//2
            if random_int > self.prefix_sum[mid]:
                low = mid +1
            else:
                high = mid

        return low
l = ["Solution","pickIndex"]
w = [[[1]],[]]
obj = Solution(l, w)
param_1 = obj.pickIndex()
print(param_1)