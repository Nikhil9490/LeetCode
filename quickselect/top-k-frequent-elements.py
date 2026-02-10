class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            hashmap = defaultdict(int)
            empty = []
            for i in range(len(nums)):
                hashmap[nums[i]]+=1
            j=1
            while j<=k:
                max_key = max(hashmap, key= hashmap.get)
                empty.append(max_key)
                del hashmap[max_key]
                j=j+1
            return empty




        