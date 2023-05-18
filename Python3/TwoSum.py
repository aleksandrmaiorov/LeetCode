##Feel free to use this code.
## OpenSource Rulez



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sonuc = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in sonuc:
                return [sonuc[diff], i]
            sonuc[n] = i
