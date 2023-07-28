gas=[5,1,2,3,4]
cost=[4,4,1,5,1]

def canCompleteCircuit( gas, cost):

    if sum(gas)<sum(cost):
        return -1
    iter=0
    myTank=0
    
    for i in range(len(gas)):
        myTank+=gas[i]-cost[i]
        if myTank<0:
            iter=i+1
            myTank=0
    return iter  

canCompleteCircuit(gas,cost)
