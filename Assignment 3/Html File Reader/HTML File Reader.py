
# File Opening
file_path = "example_html_file.html"
file = open(file_path, "r")
contents = file.read()

# Calculations
num_tags = 0
for characters in contents:
	if characters == "<":
		num_tags += 1

name_tags = []
tags = contents.split("\n")
for tag in tags:
	if "<" in tag:
		name_tags.append(tag[tag.index("<") + 1: tag.index(">")])
			

#Output

print(f"There are {num_tags} tags in the html file {file_path}")

print("The names of the tags are :")
for name_tag in name_tags:
	print(name_tag)

# File Closing
file.close()