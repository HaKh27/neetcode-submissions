from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store=defaultdict(list) 

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        left=0
        right= len(self.store[key])-1
        result=-1
        while left<=right: 
            mid= (left+right)//2
            if self.store[key][mid][0]<=timestamp:
                result=mid 
                left=mid+1 
            else:
                right=mid-1 

        if result==-1:
            return "" 
        
        return self.store[key][result][1]

        
