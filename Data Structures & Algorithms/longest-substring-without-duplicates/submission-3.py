class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        
        i = 0 
        j = 0
        ans = 0
        output = 0
        seen = set()
        print(n)
        while i<=j and i<=n-1 and j<=n-1:
            # seen.add(s[i])
            print(i,j,s[i],s[j])

            if s[j] in seen:
                # ans = max(output,ans)
                print("this1")
                output =0;
                i +=1
                j=i
                seen.clear()

            else:
                output+=1
                seen.add(s[j])
                
                j += 1
            ans = max(output,ans)
            print(f"\n{seen}")
        return ans



        