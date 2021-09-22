import requests
import json
import utils

def creat_package():

    url = "https://test-codecamp-teaching-system.codemao.cn/packages/base"
    data=utils.read_yaml("package.yaml")
    headers = {
        'Cookie': '__ca_uid_key__=2ec8d972-5ac5-4368-8d51-a359922a1fc6; test_internal_account_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUb2tlbiIsImF1dGgiOiJST0xFX0FETUlOIiwibmFtZSI6IuiBguS6mui_kCIsImVuaWQiOjEwNSwiaWF0IjoxNjMxOTQ3MzkxLCJqdGkiOiJmMTY5NTVjNi04Nzk3LTQyOTEtYjUzYy1kYzQyODNmYzI1Y2MifQ.7gPuK6_ySyushUiRnDzuD46ocyU6ZwxrmP0cpfRzJjA; test-admin-authorization=Bearer+eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3R5cGUiOiJhZG1pbiIsInVzZXJfaWQiOjg3ODQsImlhdCI6MTYzMTkxODU5MSwianRpIjoiYjBmMzk1ZTgtMTg0Yi0xMWVjLThiYmQtNmQ1ODU2YmFhNTBiIn0.SvV6jS-nmps2rDoMjL5EhPWcAKTKuTUSxKgaDZ4NUjk',
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=json.dumps(data))

    return response.json()


if __name__=="__main__":
    creat_package()

