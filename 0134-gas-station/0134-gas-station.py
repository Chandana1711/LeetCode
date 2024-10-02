class Solution:
       
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = 0  # Tracks overall gas balance for the entire trip
        curr_tank = 0   # Tracks gas balance for the current trip segment
        start = 0       # Starting gas station index
    
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]  # Update total gas balance
            curr_tank += gas[i] - cost[i]   # Update current segment gas balance
        
            # If at any point, the current segment balance goes negative,
            # it means the trip can't start from any of the previous stations.
            if curr_tank < 0:
                # Reset start to the next station
                start = i + 1
                # Reset the current segment gas balance
                curr_tank = 0
    
        # If the total gas balance is negative, return -1 (can't complete the trip)
        if total_tank < 0:
            return -1
    
         # Otherwise, return the starting index
        return start
    

        
