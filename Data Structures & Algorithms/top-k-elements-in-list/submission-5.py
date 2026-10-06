import heapq
class Solution:
    #Understand: need to return a list 
    #I need to find the elements that appear the most in a list 
    #only return k amount of frequent elements 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency={}
        heap=[]
        for num in nums:
            frequency[num]=frequency.get(num,0)+1

        for key, val in frequency.items():
            heapq.heappush(heap, (-val, key))     

        result=[]
        for i in range(k):
            popped= heapq.heappop(heap)
            result.append(popped[1])

        return result    