__author__ = 'shenyineng'

import json
import httplib

hot_url = "/api/topics/hot.json";

httpClient = httplib.HTTPConnection(host="www.v2ex.com",port=80)
httpClient.request(method="GET", url=hot_url)

hot_response = httpClient.getresponse()

hot_result = hot_response.read(amt=hot_response.length)
# print hot_result
hot_json_result = json.loads(hot_result)

for i in range(len(hot_json_result)):
    print hot_json_result[i]['title']