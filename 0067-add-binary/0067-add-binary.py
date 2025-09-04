class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def intval(a): 
            val=a
            n=len(a)
            j,r=0,0
            for i in range(n-1,-1,-1):
                r+=(2**j)*(int(val[i]))
                j+=1
            return r
        d=intval(a)
        e=intval(b)
        c=d+e
        c=str(bin(c))
        return c[2:]   
