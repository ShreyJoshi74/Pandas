class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        ls= [0]*k
        print(ls)
        i = 0
        for item in energy:
            index = i % k
            ls[index] += item
            i += 1
        print(ls)
        max = -2 ** 31
        i = 0
        for item in energy:
            groupIndex = i % k
            if ls[groupIndex] > max:
                max = ls[groupIndex]
            ls[i % k] -= item
            i += 1
        return max