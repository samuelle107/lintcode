from typing import List

class Solution:
    """
    @param weights: A list of numbers.
    @param maxWeight: An integer.
    @return: A number. The max weight of plate.
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
