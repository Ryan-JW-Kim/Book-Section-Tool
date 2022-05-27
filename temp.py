
global_str = ""
delimiter = "^"

search_for = "test"

for paragraph in paragraphs.text:
  global_str += f"{paragraph}{delimiter}"
  
sentences = global_str.split(".")
flags = {"quotes": [],
         "internal": [],
         "dashed": [],
         "searchWord": []}

count = 0

for sentence in sentences:

  if "\"" in sentence:
    flags["quotes"].append(count)
   
  elif "\'" in sentence:
     flags["internal"].append(count)
      
  elif "--" in sentnece:
      flags["dashed"].append(count)
     
  if search_for in sentence:
      flags["searchWord"].append(count)
    
   count += 1
