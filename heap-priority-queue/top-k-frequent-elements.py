class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            counts = Counter(nums)
            top_k = counts.most_common(k)
            empty =[]
            for num,freq in top_k:
                empty.append(num)
            return empty
            




        