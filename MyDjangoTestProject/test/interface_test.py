import requests
import unittest

class GetEventListTest(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:8000/api/get_event_list/"
    
    def test_get_event_null(self):
        r = requests.get(self.url,params={'eid':''})
        result = r.json()
        print(result)
        self.assertEqual(result['status'],10021)
        self.assertEqual(result['message'],'parameter error')
        
    def test_get_event_success(self):
        r = requests.get(self.url,params={'eid':'1'})
        result = r.json()
        print(result)
        
        assert result['status'] == 200
        assert result['message'] == "success"
        assert result['data']['name'] == "Apple发布会"
        assert result['data']['address'] == "美国苹果总部中心"
        assert result['data']['start_time'] == "2019-09-11T18:00:00"
        
        
if __name__ == '__main__':
        unittest.main()