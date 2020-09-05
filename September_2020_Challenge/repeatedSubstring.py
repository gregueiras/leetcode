class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        sub_size = 2
        
        if (len(s) == 1):
            return False
        
        if (len(s) == 2):
            return s[0] == s[1]
        
        last_char = s[0]
        all_same = True
        for i in s:
            if i != last_char:
                all_same = False
                break
                
        if all_same:
            return True
        
        while sub_size <= ceil(len(s) / 2):
            if (len(s) % sub_size != 0):
                sub_size += 1
                continue

            isRepeated = True
            for j in range(floor(len(s) / sub_size) - 1):
                if s[:sub_size] != s[(j + 1) * sub_size : (j + 2) * sub_size]:
                        isRepeated = False
                        break;

            if isRepeated:
                return True
            
            sub_size += 1
            
        