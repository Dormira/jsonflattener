The json flattener can be run via the following command
	python3 jsonflattener.py [output directory] [input file 1] [input file 2] ... [input file n]
You can also run the set of tests that I wrote by running the following command
	./test.sh
This will run the json flattener on every file in the inputs/ folder.

Test cases on dictionary key:
	* Most of the test cases I designed involved the keys containing periods,
		which are not within the scope of the problem
	* File contains duplicate keys
		* This test is contained in duplicateKeys.json
		* The default python json parser only associates the terminal value associated with a key in the case of duplicates
		* So for example, in the case {a:1, a:3, a:2} the resultant python dictionary from json.load() would be {"a":2}
	* Key is an empty string
		* This test is contained in emptyKey.json
Test cases on dictionary value:
	* Value is empty/None
		* A true null value throws an error on the parser level and so that test should fail
	* Value is empty string
		* I don't anticipate that this would cause an issue but I include it for peace of mind
	* Value is empty list
		* The problem statement says there won't be lists
	* Value is empty dictionary
		* Output an empty dictionary. 
		* I want it to be known that the key exists, but we can consider an empty dictionary to be flat.
        
