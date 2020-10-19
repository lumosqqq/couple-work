import base64
import requests
import re

def get_test_dict():
    url = "http://47.102.118.1:8089/api/challenge/start/218ba788-b0a3-45d0-86b5-33b0e03e13c2"

    payload = "{\r\n    \"teamid\": 46,\r\n    \"token\": \"5d6b1511-a783-4929-aa52-e3a69f197adf\"\r\n}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    r'"raw_title":".+?"'
    data = re.findall(r'\"img\":".+?"', response.text)
    print(response.text)
    data1 = eval(str(data[0]).split(':')[1])
    return data1

def decode_base64(base64_data):
    with open('./base64.jpg', 'wb') as file:
        img = base64.b64decode(base64_data)
        file.write(img)
    return img

if __name__ == '__main__':
    #img_path = './images/background.jpg'
    #test_dict = get_test_dict()
    base64_data = get_test_dict()
    #print("uuid:"+ str(test_dict['uuid']))
    #print(test_dict['step'])
    #print(test_dict['swap'])

    img = decode_base64(base64_data)
    #print(img)
