# coding = utf-8
import json
import logging
import urllib.parse
import urllib.request
from time import *

logging.basicConfig(level=logging.DEBUG)
# def post_json_by_http(json_value, url, headers):
#     data = urllib.parse.urlencode(json_value).encode('utf-8')
#     request = urllib.request.Request(url, data, headers)
#     urllib.request.urlopen(request).read().decode('utf-8')

def urllib2_send_post(send_url, data, headers=[]):
    req = urllib.request.Request(send_url, data=data)
    for header in headers:
        req.add_header(header.split(':', 1)[0], header.split(':', 1)[1])
    resJson = None
    try:
        response = urllib.request.urlopen(req)
        res = response.read()
        resJson = json.loads(eval(res))
    except urllib.error.HTTPError as e:
        logging.error(e.code)
        logging.error(send_url)
    except urllib.error.URLError as e:
        logging.error(e.reason)
        logging.error(send_url)
    except Exception as e:
        logging.error(str(e))
        logging.error(send_url)
    return resJson


def getValue(cluster, service, component, component_state, host, ip):
    my_dict = {'cluster': cluster,
               'service': service,
               'component': component,
               'component_state': component_state,
               'host': host,
               'ip': ip,
               'ts': '1234555566'
               }
    # my_json = json.dumps(my_dict).encode()
    # return my_json
    return my_dict


collect_time = time()
url = "http://192.168.52.19:4444/test_json_by_http"
headers = ["Content-Type:application/json; charset=utf-8"]
count = 0
bounary = 10_11
datas_collect_list = []
while count < bounary:
    count = count + 1
    cluster = 'cluster' + str(count)
    service = 'service' + str(count)
    component = 'component' + str(count)
    component_state = 'componentState' + str(count)
    host = 'leader-myhost' + str(count)
    ip = '192.168.52.' + str(count)
    result_json = getValue(cluster, service, component, component_state, host, ip)
    # 单独发送！！！
    # urllib2_send_post(url, result_json, headers)
    # 合并为列表后推送
    datas_collect_list.append(result_json)

# 下面没有encode()方法就是没有进行反序列化，需要添加encode进行反序列化
# urllib2_send_post(url, json.dumps(datas_collect_list), headers)
# urllib2_send_post(url, json.dumps(datas_collect_list).encode(), headers)
size = len(datas_collect_list)
index = 1
temp_list = []
# 令列表的长度为500，发送合适大小的数据到http端口
batch_size = 500
while index <= size:
    temp_list.append(datas_collect_list[index -1])
    if index % batch_size == 0:
        print("index:" + str(index) + ' data')
        print(temp_list)
        urllib2_send_post(url, json.dumps(temp_list).encode(), headers)
        temp_list = []
    index += 1

if len(temp_list) != 0:
    print("余下的:")
    print(len(temp_list))
    print(temp_list)
    urllib2_send_post(url, json.dumps(temp_list).encode(), headers)
print("=== end ===")
