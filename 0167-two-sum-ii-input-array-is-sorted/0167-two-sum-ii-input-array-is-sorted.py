class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # index_list = []
        i= 0
        j = len(numbers)-1 
        
        
        
        while i < j:
            curr_sum = numbers[i]+numbers[j]
            
            if curr_sum == target:
                return [i+1, j+1]
            elif curr_sum < target:
                i+=1
            else:
                j-=1
                
        # return []  
#                 if (numbers[i] + numbers[j]) == target:
#                     index_list.append(i+1)
#                     index_list.append(j+1)
#                     return 
            
#             i+=1
                   
                
#                 # else:
#                 #      break
#         return index_list
                    