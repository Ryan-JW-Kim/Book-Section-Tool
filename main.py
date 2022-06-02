from document_manager import DocManager
import argparse
import sys
import os


def main():

	parser = argparse.ArgumentParser()

	parser.add_argument("-q", action = "store_true")
	parser.add_argument("-i", action = "store_true")
	parser.add_argument("-d", action = "store_true")
	parser.add_argument("-s", action = "store_true")
	args = parser.parse_args()

	
	document_name = f"test.docx"#sys.argv[1]

	document_object = DocManager(document_name)

	flag_list = document_object.flag_markers(args)

	new_document = DocManager.assemble_from_flags(f"edited-{document_name}", flag_list, document_object)

	new_document.save()

if __name__ == "__main__":

	main()
