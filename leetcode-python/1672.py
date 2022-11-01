class Solution(object):
    def maximumWealth(self, accounts):
        sum=0
        sum1=0
        for i in range(0,len(accounts)):
            for j in range(0,len(accounts[i])):
                sum=sum+accounts[i][j]
            print("sum:",sum)
            if sum>=sum1:
                sum1=sum
                sum=0
                print("sum1:",sum1)
            else:
                sum=0
        return sum1