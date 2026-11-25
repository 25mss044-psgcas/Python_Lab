text = input("Enter a string: ")

reversed_text = text[::-1]
print(f"Reversed String: {reversed_text}")

clean_text = text.replace(" ", "").lower()
is_palindrome = (clean_text == clean_text[::-1])
print(f"Is Palindrome?: {is_palindrome}")

vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in text if char in vowels)
word_count = len(text.split())
print(f"Vowel Count: {vowel_count}")
print(f"Word Count: {word_count}")

old_sub = input("Enter substring to replace: ")
new_sub = input("Enter new substring: ")
modified_text = text.replace(old_sub, new_sub)
print("Formatted Output: '{}'".format(modified_text.title()))