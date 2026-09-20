from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        # Create a graph containing every character.
        #
        # Example:
        # words = ["abc", "bcd"]
        #
        # adj becomes:
        # {
        #     "a": set(),
        #     "b": set(),
        #     "c": set(),
        #     "d": set()
        # }
        #
        # Each character will point to characters that must come after it.
        adj = {
            character: set()
            for word in words
            for character in word
        }

        # Compare every pair of neighboring words.
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            # We only compare positions that exist in both words.
            min_length = min(len(word1), len(word2))

            # Invalid prefix case:
            #
            # word1 = "apple"
            # word2 = "app"
            #
            # A longer word cannot appear before its exact prefix.
            if (
                len(word1) > len(word2)
                and word1[:min_length] == word2[:min_length]
            ):
                return ""

            # Find the first position where the two words differ.
            for j in range(min_length):
                if word1[j] != word2[j]:

                    # Because word1 appears before word2,
                    # word1[j] must come before word2[j].
                    #
                    # Example:
                    # word1 = "wrt"
                    # word2 = "wrf"
                    #
                    # First difference:
                    # t != f
                    #
                    # Therefore:
                    # t → f
                    adj[word1[j]].add(word2[j])

                    # Only the first different character matters.
                    break

        # visit stores the DFS state of each character.
        #
        # Character not in visit:
        #     never visited
        #
        # visit[character] == True:
        #     currently in the DFS path
        #
        # visit[character] == False:
        #     completely processed
        visit = {}

        # Stores letters in reverse topological order.
        result = []

        def dfs(character: str) -> bool:
            # If the character was already visited:
            if character in visit:

                # True means it is currently in the recursion path,
                # so we found a cycle.
                #
                # False means it was already completely processed.
                return visit[character]

            # Mark this character as currently being explored.
            visit[character] = True

            # Visit every character that must come after it.
            for neighbor in adj[character]:
                if dfs(neighbor):#return visit[character] it returns true where tehre is cycle
                    # A cycle was found.
                    return True

            # We finished processing this character.
            visit[character] = False

            # Add it after all letters that must come after it.
            result.append(character)

            # False means no cycle was found.
            return False

        # Run DFS from every character.
        for character in adj:
            if dfs(character):
                # A cycle means there is no valid alphabet order.
                return ""

        # DFS adds the characters backward.
        result.reverse()

        # Convert the list into one string.
        return "".join(result)  

        #1. Put every letter into the graph.
#2. Compare each pair of neighboring words.
#3. Use their first different letters to create an ordering rule.
#4. Use DFS to detect cycles and arrange the letters.
#5. Reverse the DFS result and return it as a string.      