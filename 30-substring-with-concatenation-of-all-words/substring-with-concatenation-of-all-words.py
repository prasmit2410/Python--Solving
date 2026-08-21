class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        if total_len > len(s):
            return []

        # Frequency of each word required
        word_freq = {}

        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

        result = []

        # Try every possible starting offset
        for offset in range(word_len):
            left = offset
            count = 0
            current_freq = {}

            for right in range(offset, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                # Word is not required
                if word not in word_freq:
                    current_freq.clear()
                    count = 0
                    left = right + word_len
                    continue

                # Add current word
                current_freq[word] = current_freq.get(word, 0) + 1
                count += 1

                # Too many occurrences of this word
                while current_freq[word] > word_freq[word]:
                    left_word = s[left:left + word_len]
                    current_freq[left_word] -= 1
                    left += word_len
                    count -= 1

                # Found a valid concatenation
                if count == word_count:
                    result.append(left)

                    # Move window forward for next possible match
                    left_word = s[left:left + word_len]
                    current_freq[left_word] -= 1
                    left += word_len
                    count -= 1

        return result