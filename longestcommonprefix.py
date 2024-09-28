class Solution:
    def longestCommonPrefix(self, strs):
        ls=len(strs)
        if ls<2:
            return strs[0]
        cp=""
        for i,j in zip(strs[0],strs[1]):
            if i==j:
                cp=cp+i
            else:
                break
        if ls==2:
            return cp
        if not cp:
            return ""
        for j in range(2,ls):
            z=''
            for i,k in zip(cp,strs[j]):
                if i==k:
                    z=z+i
                else:
                    break
            cp=z
            if not cp:
                return ""
        return cp
sol=Solution()
x=[["flower","flow","flight"],["dog","racecar","car"]]
for i in x:
    print(sol.longestCommonPrefix(i))
