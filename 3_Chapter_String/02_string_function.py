# Step 1: Declare a string variable
message = "   Hello, Harsh! Welcome to Python World.   "

# Step 2: Print original string
print("Original String:", repr(message))  # repr() shows whitespace too

# Step 3: Remove whitespace from both ends
stripped = message.strip()
print("After strip():", repr(stripped))

# Step 4: Convert to lowercase
lowered = stripped.lower()
print("After lower():", lowered)

# Step 5: Convert to uppercase
uppered = stripped.upper()
print("After upper():", uppered)

# Step 6: Replace 'Python' with 'Gen AI'
replaced = stripped.replace("Python", "Gen AI")
print("After replace():", replaced)

# Step 7: Split the string by space
split_list = stripped.split(" ")
print("After split():", split_list)

# Step 8: Join the list using '-'
joined = "-".join(split_list)
print("After join():", joined)

# Step 9: Find position of "Harsh"
pos = stripped.find("Harsh")
print("Position of 'Harsh':", pos)

# Step 10: Count how many times 'o' appears
count_o = stripped.count("o")
print("Count of 'o':", count_o)

# Step 11: Check if it starts with 'Hello'
starts = stripped.startswith("Hello")
print("Starts with 'Hello':", starts)

# Step 12: Check if it ends with '.'
ends = stripped.endswith(".")
print("Ends with '.':", ends)

# Step 13: Check if the string is all alphabet
alpha_check = stripped.isalpha()
print("Is alphabet only:", alpha_check)

# Step 14: Check if string is all digits
digit_check = stripped.isdigit()
print("Is digit only:", digit_check)
