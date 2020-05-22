class Solution:
    
    def findAnagrams(self, s: str, p: str):

        if len(s) == 0  or len(s) < len(p):
            return []
        
       
        
        A = [0]*26
        B = [0]*26

        p_len = len(p)

        ret = []
       
        for i in range(p_len):
            A[ord(p[i]) - ord('a')] += 1
            B[ord(s[i]) - ord('a')] += 1

        if A == B:
            ret.append(0)

        for i in range(p_len, len(s)):
            B[ord(s[i-p_len]) - ord('a')] -= 1
            B[ord(s[i]) - ord('a')] += 1
            if A == B:
                ret.append(i - p_len + 1)
              
            
        return ret


if __name__ == "__main__":
    s = Solution()
    #x = s.findAnagrams("abab", "ab")
    x = s.findAnagrams("cbaebabacd",  "abc")
    print(x)
   
