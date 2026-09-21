class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
        
        keys = list(counts.keys())
        top_k = []
        for i in range(k):
            top_k.append(keys[i])
        
        return top_k