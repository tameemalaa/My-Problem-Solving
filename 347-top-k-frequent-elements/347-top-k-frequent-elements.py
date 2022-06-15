class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = Counter(nums)
        l=  [[] for _ in range(len(nums) + 1)]
        for i,j in x.items():
            l[j].append(i)
        a = list(chain(*l))
        print(a)
        return a[len(a)-k:]