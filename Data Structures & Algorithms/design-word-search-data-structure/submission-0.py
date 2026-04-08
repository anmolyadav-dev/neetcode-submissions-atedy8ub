class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curLetter = self.root
        for c in word:
            if c not in curLetter.children:
                curLetter.children[c] = TrieNode()
            curLetter = curLetter.children[c]
        curLetter.end = True
    def search(self, word: str) -> bool:
        def dfs(ind,root):
            curLetter = root
            for i in range(ind,len(word)):
                c = word[i]
                if c == ".":
                    for child in curLetter.children.values():
                        if dfs(i+1,child):
                            return True
                    return False   
                else:       
                    if c not in curLetter.children:
                        return False
                    curLetter = curLetter.children[c]
            return curLetter.end
        return dfs(0,self.root)
