import requests

token = 'NGNS2PSVIk5glYDotowpUqDcAUxOQ9KHZ8sRROIVdVk'

response = requests.post(
    url='https://notify-api.line.me/api/notify',
    headers={
        'Authorization': f'Bearer {token}'
    },
    data={
        'message': '我只是機器人 deep01\nyoyo'
    }
)

print(response.status_code)
print(response.text)