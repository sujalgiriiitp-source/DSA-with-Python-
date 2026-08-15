class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
              
              freq = {}

              for ch in magazine:
                  freq[ch]= freq.get(ch, 0) + 1
              
              for ch in ransomNote:
                  if freq.get(ch, 0) == 0:
                      return False
                  
                  freq[ch] -= 1
              return True
        