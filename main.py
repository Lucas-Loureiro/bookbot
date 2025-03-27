import sys
from stats import count_words

def sort_on(dict):
  return dict["value"]

def transform_list(dict):
  list = []
  for char in dict:
    if char.isalpha():
      list.append({"char": char, "value": dict[char]},)
  return list

def count_same_char(text):
  dict = {}
  for i in text.lower():
    if i in dict:
      dict[i] += 1
    else:
      dict[i] = 1
  list_dict = transform_list(dict)
  list_dict.sort(reverse=True, key=sort_on)
  for i in range(len(list_dict)):
    print(f"{list_dict[i]["char"]}: {list_dict[i]["value"]}")
  

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1) 
    
  print(f"--- Begin report of {sys.argv[1]} ---")
  with open(sys.argv[1]) as f:
    file_contents = f.read()
  print(f"{count_words(file_contents)} words found in the document")
  count_same_char(file_contents)
  print("--- End report ---")


main()