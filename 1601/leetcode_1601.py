class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        transfers=collections.defaultdict(int)
        
        def same_state(transfers):
            for i in transfers:
                if transfers[i]!=0:
                    return False
            
            return True



        def calculateAchievableRequests(transfers,start,selected):
            if start==len(requests):
                if(same_state(transfers)):
                    self.maxAchievableRequest=max(selected,self.maxAchievableRequest)
                return 0
           
            x=requests[start][0]
            y=requests[start][1]
            transfers[x]-=1
            transfers[y]+=1
            calculateAchievableRequests(transfers,start+1,selected+1)
            transfers[x]+=1
            transfers[y]-=1
            calculateAchievableRequests(transfers,start+1,selected)
            return 0

            
        





        self.maxAchievableRequest=0
        self.count=0
        ans = calculateAchievableRequests(transfers,0,0)
        return self.maxAchievableRequest
        
