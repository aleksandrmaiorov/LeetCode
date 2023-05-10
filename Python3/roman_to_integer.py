## MY SOLUTION
##Feel free to use this code.

class Solution:
    def romanToInt(self, s: str) -> int:
        romali ={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        i = 0
        num = 0
        while i < len(s):
            if i+1<len(s) and s[i:i+2] in romanli:
                num+=romali[s[i:i+2]]
                i+=2
            else:
                num+=romali[s[i]]
                i+=1
        return num

### BEST SOLUTION
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_conversion = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900, "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ret = 0
        for k, v in roman_conversion.items():
            if k in s:
                ret += s.count(k) * v
                s = s.replace(k, "")

        return ret
