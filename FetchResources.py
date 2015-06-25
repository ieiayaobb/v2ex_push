__author__ = 'shenyineng'

import json
import httplib

hot_url = "/api/topics/hot.json";

class FetchResources():
    httpClient = None;
    def __init__(self):
        self.httpClient = httplib.HTTPConnection(host="www.v2ex.com",port=80)
    def fetch(self):
        self.httpClient.request(method="GET", url=hot_url)

        hot_response = self.httpClient.getresponse()

        hot_result = hot_response.read(amt=hot_response.length)
        print hot_result
        hot_json_result = json.loads(hot_result)

        return hot_json_result