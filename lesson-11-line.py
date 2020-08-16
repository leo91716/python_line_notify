import requests

token = 'e5a52d9L5eOt6sOUy7IxNFNlFR8uAKVDZ8vv344CYuE'

response = requests.post(
    url='https://notify-api.line.me/api/notify',
    headers={
        'Authorization': f'Bearer {token}'
    },
    data={
        'message': '我只是機器人 deep01 hahaha'
    }
)

print(response.status_code)
print(response.text)


response = requests.post(
    url='https://notify-api.line.me/api/notify',
    headers={
        'Authorization': f'Bearer {token}'
    },
    data={
        'message': '我 deep01 hahaha'
    }
)

print(response.status_code)
print(response.text)