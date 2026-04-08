class Solution:
    
    def isPalindrome(self, s: str) -> bool:
        #brute-force
        s = s.strip("");
        
        i = 0
        j = len(s)-1
        print(s)
        while(i<=j and i<len(s) and j>=0):
            if not s[i].isalnum():
                i+=1;
                continue;
            elif not s[j].isalnum():
                j-=1;
                continue;
            
            if (s[i].lower() != s[j].lower()):
                return False

            if (s[i].lower() ==  s[j].lower()):
                i+=1;
                j-=1;
        return True;
                


        