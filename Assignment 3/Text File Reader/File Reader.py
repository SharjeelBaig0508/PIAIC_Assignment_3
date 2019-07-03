# File Opening
file_path = "sample_text_file.txt4"
file = open(file_path, 'r')
contents = file.read()

# -----------------( Calculations )-------------------

# Word Count
words = contents.split()
num_words = len(words)

# Line Count
lines = contents.split("\n")
num_lines = len(lines)

# Non-Space Characters, Spaces, Tabs Count
num_characters, num_spaces, num_tabs = 0, 0, 0
for character in contents:
	if character == " ":
		num_spaces += 1
	elif character == "\t":
		num_tabs += 1
	else:
		num_characters += 1

# Paragraph Count
paragraphs = contents.split("\n\t")
num_paragraphs = len(paragraphs)

# --------------( Calculation Ends )----------------

# ---------------------( Output )-----------------------

# Words
print(f"There are {num_words} words in the file {file_path}")

# Lines
print(f"There are {num_lines} lines in the file {file_path}")

# Characters
print(f"There are {num_characters} non-space characters in the file {file_path}")

# Spaces
print(f"There are {num_spaces} spaces in the file {file_path}")

# Tabs
print(f"There are {num_tabs} tabs in the file {file_path}")

# Paragraphs
print(f"There are {num_paragraphs} paragraphs in the file {file_path}")

# ------------------( Output Ends )-----------------

#File Closing
file.close()

# ---------------( Program Ends )-----------------