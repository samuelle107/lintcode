from typing import List

class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def weightCapacity(self, weights: List[int], maxWeight: int) -> int:
      dp = [False for _ in range(maxWeight+ 1)]
      dp[0] = True;
      maxW = 0

      for weight in weights:
        for j in range(maxWeight - weight, -1, -1):
          if dp[j]:
            capacity = weight + j
            dp[capacity] = True
            maxW = max(maxW, capacity)        
  
      return maxW
