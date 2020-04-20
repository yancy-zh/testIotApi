from framework import requestHandler
import os
import json
import sys

def read_json_in_file(path):
    with open(path, 'r') as f:
        return json.load(f)

workingDirectory = os.getcwd()
# load the configuration file
if len(sys.argv) > 1 and os.path.isfile(os.path.abspath(sys.argv[-1])):
    configFilePath = os.path.abspath(sys.argv[-1])
    print("Config found as \"{0}\"".format(configFilePath))
else:
    configFilePath = os.path.join(workingDirectory, "config", "deviceNumbers.json")
    print("Using default config \"{0}\"".format(configFilePath))

CONFIG_FILE = read_json_in_file(configFilePath)
request_handler = requestHandler.CollectionManagement(CONFIG_FILE)
list_of_cids =[]
if ("begin" in CONFIG_FILE["cid"] and "end" in CONFIG_FILE["cid"]):
    list_of_cids = list(range(CONFIG_FILE["cid"]["begin"], CONFIG_FILE["cid"]["end"]+1))
elif type(CONFIG_FILE["cid"]) is list:
    list_of_cids = CONFIG_FILE['cid']
else:
    print("Collection ids are not given in the configuration file")
