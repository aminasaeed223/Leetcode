class Solution:
    def reverseWords(self, s: str) -> str:
        # using split function to separate each word in string
        split_words = s.split()
        # print(split_words)
        # Now we will reversed these words using slicing
        reversed_words = split_words[::-1]
        # print(reversed_words)
        # we have to return answer in string, so we will convert list into string again separated with spaces
        reversed_string = " ".join(reversed_words)
        
        return reversed_string

        