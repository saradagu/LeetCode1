class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s=" "
        for i in digits:
            s+=str(i)
        n=str(int(s)+1)
        l=[]
        for  i in n:
             l.append(int(i))
        return l

         


        