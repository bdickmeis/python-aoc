import re

string = "bvwbjplbgvbhsrlpgdmjqwftvncz"

match = re.search(r'(?<!\w)[a-z]{4}(?!\w)', string)

if match:
  print(f"The first 4 unique characters are at position {match.start()}")
else:
  print("No match found")
