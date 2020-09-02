#!/usr/bin/python
import json #For parsing JSON
import sys  #For getting system input
import os #For dealing with filenames


def flattenDictionary(dictionary, name=[]):
    """
    This function takes
        name, a string which is the name of the dictionary being passed
        and
        dictionary, a dictionary to be flattened
    It returns
        flattenedDict, a flattened version of dictionary

    We flatten the dictionary by iterating through the keys
    If the associated value is not a dictionary, then that portion is already flat and we can add it as it is
    If the associated value is a dictionary, then we flatten that portion recursively and merge it after flattening
    """
    flattenedDict = {}
    for key in dictionary.keys():
        subname = name+[key]
        #If the key refers to a non-empty dictionary, flatten it and merge
        if type(dictionary[key]) == dict and len(dictionary[key].keys()) != 0:
            subdict = flattenDictionary(dictionary[key], subname)
            flattenedDict.update(subdict)
        #Otherwise add it as it is
        else:
            flattenedDict[".".join(subname)] = dictionary[key]

    return flattenedDict
 

if __name__ == "__main__":
    """
    argv[0] = script name by default 
    argv[1] = output directory name
    All subsequent arguments must be input file names

    """
    outputDir = sys.argv[1]
    assert os.path.exists(outputDir), "Output directory is not a valid path. Please specify an existing directory to output to."

    for fpath in sys.argv[2:]:
        basename = os.path.basename(fpath)
        with open(os.path.join(outputDir,basename), "w") as outputFile:
            try:
                with open(fpath) as json_file:
                    jsonDict = json.load(json_file)
                    flattenedDict = flattenDictionary(jsonDict)
                    #pretty print the json to file so its readable
                    json.dump(flattenedDict, outputFile, indent=1)
            except Exception as e:
                outputFile.write("Couldn't load json file "+str(fpath)+": "+str(e))
