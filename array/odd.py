class Solution:
    def trainingPlan(self, actions: List[int]) -> List[int]:
        i = 0
        j =len(actions) -1
        while i < j:
            while i < j and actions[i] %2 == 1:
                i += 1
            while i < j and actions[j] %2 == 0:
                j -= 1
            temp = actions[i]
            actions[i] = actions[j]
            actions[j] =  temp
            i += 1
            j -= 1
        return actions