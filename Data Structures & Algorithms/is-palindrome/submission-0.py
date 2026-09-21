class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = "".join(char for char in s if char.isalnum())
        cleaned_text.replace(" ","")
        cleaned_text = cleaned_text.lower()
        print(cleaned_text)

        length = len(cleaned_text)
        if length % 2 == 1:
            front = cleaned_text[:(int(length/2))]
            print(front)
            back = cleaned_text[int(length/2)+1:]
            print(back)
        else:
            front = cleaned_text[:int(length/2)]
            print(front)
            back = cleaned_text[int(length/2):]
            print(back)

        reversed_back = "".join(reversed(back))
        print(reversed_back)
        if(front == reversed_back):
            return True
        else:
            return False


        
