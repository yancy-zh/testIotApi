from framework import requestHandler
import os
import json
import sys
from typing import List
def read_json_in_file(path):
    with open(path, 'r') as f:
        return json.load(f)

def loop_for_list_of_cids(list_of_cids:List[str], handler: requestHandler.CollectionManagement):
    for i in range(list_of_cids.__len__()):
        resp = handler.retrieve_collection_by_cid(list_of_cids[i])
        print("tid is {}, resp is {}, msg is {}".format(list_of_cids[i], resp.status, resp.status_message))

if __name__ == '__main__':
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

    # test case against collections

    # Create
    loop_for_list_of_cids(list_of_cids, request_handler)
    # Retrieve

    # Update
    # Delete
