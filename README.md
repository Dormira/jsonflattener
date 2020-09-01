
# JSON Flattener
## How to run
The JSON flattener can be run via the following command

	python3 jsonflattener.py path/to/output/directory [input json file 1] ... [input json file n]
                                                                                                                                                                                                                                                                                                           
You can also run the flattener on every file in the inputs/ by running the following command

	./test.sh
This will also output an error message if a test's output differs from its baseline in expectedOutputs/

## Test cases on dictionary key
### File contains duplicate keys
`inputs/duplicateKeys.json`

The default Python3 json parser only associates the terminal value associated with a key in the case of duplicates. So for example, loading the following JSON file

	{"a": 1,
	 "a": 3,
	 "a": 2} 		

would result in the following Python dictionary
	
	{"a": 2}
Because this happens during parsing I do not check for it.
### Key is an empty string
`inputs/emptyKey.json`
## Test cases on dictionary value
### Value is empty/None
`inputs/nullValues.json`

This should fail with an exception
### Value is empty string
`inputs/emptyValues.json`
### Value is empty list
`inputs/emptyValues.json`

The problem statement says there won't be lists, but the code handles empty lists so I include it for completions sake.
### Value is empty dictionary
`inputs/terminallyEmpty.json`
`inputs/fullyEmpty.json`

This should still print the key name to dictionary, since presumably we want to know that the key existed in the non-flattened verion as an empty dict. I think we can consider an empty dictionary to be flattened.
