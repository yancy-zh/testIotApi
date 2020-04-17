import sys
from datetime import datetime
import framework.connection as connection

def get_date_from_timestamp(date_time_str):
    return datetime.strptime(date_time_str.split('T')[0], "%Y-%m-%d")

def time_delta_from_now(date_time_obj):
    return datetime.now() - get_date_from_timestamp(date_time_obj)

class CollectionManagement():
    def __init__(self, p_config):
        self.config = p_config["connection"]
        try:
            self.connection = connection.Connection(host=self.config['host'],
                                                      port=self.config['port'],
                                                    project=self.config['project'],
                                                    user_email= self.config['username'],
                                                    password= self.config['password'],
                                                    token=self.config['initial_token']
                                                        )
        except Exception as ex:
            print("Failed to initialize the CLOUD globals with exception {}".format(ex))
            sys.exit(-1)

    def retrieve_collection_by_cid(self, cid):
        params = {
            'cid': cid,
        }
        resp = self.connection.send_get_request(
            '/collections/{}'.format(cid),
            params=params
        )
        return resp

    def create_a_collection(self, collection_id):
        body = {
        "collection": collection_id,
          "fields": [
            {
              "field": "id",
              "type": "integer",
              "datatype": "int",
              "length": 11,
              "interface": "numeric",
              "primary_key": True
            }
          ]
        }

        resp = self.connection.send_post_request(
            '/collections',
            json=body,
        )
        return resp

    def update_a_collection(self, collection_id):
        body = {
            "note": "This is a test of updateing the field of a collection. "
        }
        resp = self.connection.send_patch_request(
            '/collections/{}'.format(collection_id),
            json=body,
        )
        return resp

    def delete_a_collection(self, collection_id):
        resp = self.connection.send_delete_request(
            '/collections/{}'.format(collection_id),
        )
        return resp