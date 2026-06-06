# LeetCode 208 - Implement Trie (Prefix Tree)
# Time:
# insert() -> O(n)
# search() -> O(n)
# startsWith() -> O(n)
# Space: O(total characters)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

        node.end = True

    def search(self, word: str) -> bool:
        node = self.root

        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]

        return node.end

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]

        return True


# ---------- TEST ----------
trie = Trie()

trie.insert("apple")
print(trie.search("apple"))      # True
print(trie.search("app"))        # False
print(trie.startsWith("app"))    # True

trie.insert("app")
print(trie.search("app"))        # True
