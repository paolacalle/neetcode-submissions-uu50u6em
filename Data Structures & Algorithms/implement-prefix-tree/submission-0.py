class TrieNode:
    def __init__(self):
        self.kids = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.tree = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.tree
        for c in word:
            next_curr = curr.kids.get(c, None)

            if not next_curr: 
                curr.kids[c] = TrieNode()
                next_curr = curr.kids[c]

            curr = next_curr

        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.tree 
        for c in word:
            next_curr = curr.kids.get(c, None)

            if not next_curr:
                return False

            curr = next_curr

        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.tree 
        for c in prefix:
            next_curr = curr.kids.get(c, None)

            if not next_curr:
                return False

            curr = next_curr

        return True
        