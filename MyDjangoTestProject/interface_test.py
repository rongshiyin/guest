import requests

url = "http://127.0.0.1:8000/api/get_event_list/"
r = requests.get(url,params={'eid':'1'})
result = r.json()
print(result)

assert result['status'] == 200
assert result['message'] == "success"
assert result['data']['name'] == "Apple发布会"
assert result['data']['address'] == "美国苹果总部中心"
assert result['data']['start_time'] == "2019-09-11T18:00:00"