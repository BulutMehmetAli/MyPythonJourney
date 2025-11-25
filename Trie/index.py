class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    
    def __init__(self):
        self.root = TrieNode()

    def insert(self , word:str):
        temp = self.root
        word = word.lower()
        for letter in word:
            if letter not in temp.children:
                temp.children[letter] = TrieNode()
            temp = temp.children[letter]
        temp.endOfWord = True
    
    def search(self , word):
        if self.root is None:
            return False
        word = word.lower()
        temp = self.root

        for letter in word:
            if letter not in temp.children:
                return False
            temp = temp.children[letter]
        
        return True
    
    def startWith(self , word):
        if self.root is None:
            return False
        temp = self.root
        word = word.lower()
        for letter in word:
            if letter not in temp.children:
                return False
            temp = temp.children[letter]
        return True
    
    def insertToGeeksForGeeks(self , word:str):
        temp = self.root
        word = word.lower()

        for l in word:
            result = ord(l) - ord('a')

            if result < 0 or result > 25:
                raise ValueError(f"Unsupported character: {l}")
            
            if temp.children[result] is None:
                
                temp.children[result] = TrieNode()
            temp = temp.children[result]
        temp.endOfWord = True

myTrie = Trie()

myTrie.insert("Merhaba")
print(myTrie.search("merhaba"))
print(myTrie.startWith("merker"))
        
    