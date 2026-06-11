class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(s.split(" "))
        print(s)
        i = 0
        j = len(s)-1
        while i<j:
            while i<j and not s[i].isalnum():
                i+=1
            while i<j and not s[j].isalnum():
                j-=1
            if s[i].lower() == s[j].lower():
                i+=1
                j-=1
            else:
                return False
        return True