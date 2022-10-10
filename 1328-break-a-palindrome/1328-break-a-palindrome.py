class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""
        else:
            idx = 0
            
            ans = ""    
            while(idx<n and palindrome[idx] == 'a'):
                idx += 1
            if idx == n:
                ans = palindrome[:-1] + 'b'
                return ans
            if(n%2 == 1 and idx==n//2):
                idx += 1
                while(idx<n and palindrome[idx] == 'a'):
                    idx += 1
                if idx == n:
                    ans = palindrome[:-1] + 'b'
                    return ans
            else:
                ans = palindrome[:idx] + 'a' + palindrome[idx+1:]
        return ans
            