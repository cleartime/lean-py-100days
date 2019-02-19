# -*- coding:utf-8 -*-
from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '15563140'
API_KEY = 'zlP76BOOMHiEhvjzPV1I9eDN'
SECRET_KEY = 'c2pz9QdnolSLhmZjk49QNA9DL2tmutiK'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('1.png')
front = get_file_content('front.jpg')
back = get_file_content('back.jpg')

options = {}
options["result_type"] = "json"
res = client.tableRecognitionAsync(image)
request_id = res['result'][0]['request_id']
print(request_id)
request = client.getTableRecognitionResult('15563140_890441', options)
print(request)