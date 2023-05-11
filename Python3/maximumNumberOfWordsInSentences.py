## Feel Free to use this code.
## OpenSource Rulez!

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxWords = 0
        for sentence in sentences:
            words = re.findall(r'\w+', sentence)
            if len(words)> maxWords:
                maxWords = len(words)
        
        return maxWords
