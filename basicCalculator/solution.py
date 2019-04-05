class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        sign = [1,1]
        i = 0 ; res = 0
        while i<len(s):
            c = s[i]
            if c.isdigit():
                st = i
                while i<len(s) and s[i].isdigit():i+=1
                #print sign
                res += sign.pop() * int(s[st:i])
                continue
            if c in "+-(":
                #print sign
                sign.append(sign[-1] * -1 if c=="-" else sign[-1] * 1)
                #print sign
            elif c ==")":
                sign.pop()
            i+=1
        #print sign
        return res
