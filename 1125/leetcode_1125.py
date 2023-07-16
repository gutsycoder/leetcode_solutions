class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skilled_people = collections.defaultdict(list)
        for index,skills in enumerate(people):
            for skill in skills:
                skilled_people[skill].append(index)
        result=[]
        part_of_result=collections.defaultdict(lambda: False)
        self.ans=[];
        def findSmallestSufficientTeam(result,index):
            if index>=len(req_skills):
                if len(result)<len(self.ans) or len(self.ans)==0:
                    self.ans=result[:]
                return
            skill_choose = req_skills[index]
            for choose_people in skilled_people[skill_choose]:
                if not part_of_result[choose_people]:
                    part_of_result[choose_people]=True
                    findSmallestSufficientTeam(result+[choose_people],index+1)
                    part_of_result[choose_people]=False
                else:
                    findSmallestSufficientTeam(result,index+1)
            return


        

        findSmallestSufficientTeam(result,0)
        return self.ans
            
