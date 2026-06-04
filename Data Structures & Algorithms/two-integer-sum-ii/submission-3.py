class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ind_2 = len(numbers) -1
        ind_1 = 0
        while ind_1 < ind_2:
            if numbers[ind_1] + numbers[ind_2] > target:
                ind_2 -= 1
            elif numbers[ind_1] + numbers[ind_2] < target:
                ind_1 += 1
            else:
                return [ind_1+1, ind_2+1]
            
            