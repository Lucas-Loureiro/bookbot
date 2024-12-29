def count_words(text):
  return len(text.split())

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
    print(f"The '{list_dict[i]["char"]}' character was found {list_dict[i]["value"]} times")
  

def main():
  print("--- Begin report of books/frankenstein.txt ---")
  with open("books/frankenstein.txt") as f:
    file_contents = f.read()
  print(f"{count_words(file_contents)} words found in the document")
  count_same_char(file_contents)
  print("--- End report ---")


main()