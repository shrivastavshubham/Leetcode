class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def isPalin(word):
            return word == word[::-1] if len(word) > 1 else True
        resDict = {} ; res=set()
        for i,elem in enumerate(words):
            resDict[elem[::-1]] = i
        for i,elem in enumerate(words):
            for j in range(len(elem)+1):
                prefix = elem[:j]
                prerest = elem[j:]
                if prefix in resDict and resDict[prefix]!=i and isPalin(prerest):
                    res.add((i,resDict[prefix]))
            for k in range(len(elem),-1,-1):
                suffix = elem[k:]
                sufrest = elem[:k]
                if suffix in resDict and resDict[suffix]!=i and isPalin(sufrest):
                    res.add((resDict[suffix],i))
        print(res)
        return [[ress[0],ress[1]] for ress in res]
