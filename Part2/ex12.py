# Create a function called check_string
def check_string(text):
    if text.startswith("The"):
        return "Found it!"
    else:
        return "Nope."

# Test cases
str1 = 'The'
str2 = 'Thumbs up'
str3 = 'Three'
str4 = 'Therefore'

print(check_string(str1))    # ➜ Found it!
print(check_string(str2))    # ➜ Nope.
print(check_string(str3))    # ➜ Found it!
print (check_string(str4))