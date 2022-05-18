import sys
import rule_manager
import document_manager

def main()
  
  document_name = sys.argv[1]
  
  document_object = Document_manager(document_name)
  rules_object = Rule_manager()
  
  for iter in document_object.body:
    
    rules_object.apply_rules(iter)
    
  new_document = Document_manager(f"a{document_name}")
  
  rules_object.proposed_changes.write_to_file()
  
  
if __name__ == "__main__":
  
  main()
