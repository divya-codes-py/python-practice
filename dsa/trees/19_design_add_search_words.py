# LeetCode 211 - Design Add and Search Words Data Structure
# Time:
# addWord() -> O(n)
# search() -> O(n) average
# Space: O(total characters)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

        node.end = True

    def search(self, word: str) -> bool:

        def dfs(i, node):
            if i == len(word):
                return node.end

            ch = word[i]

            if ch == ".":
                for child in node.children.values():
                    if dfs(i + 1, child):
                        return True
                return False

            if ch not in node.children:
                return False

            return dfs(i + 1, node.children[ch])

        return dfs(0, self.root)


# ---------- TEST ----------
obj = WordDictionary()

obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")

print(obj.search("pad"))   # False
print(obj.search("bad"))   # True
print(obj.search(".ad"))   # True
print(obj.search("b.."))   # True
