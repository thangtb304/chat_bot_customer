import requests

# URL của Rasa server đang chạy với REST webhook
url = "http://localhost:5005/webhooks/rest/webhook"
#url = "http://0.0.0:5005/webhooks/rest/webhook"  # kết nối với server API rasa localhost:5005 không được
reset_url = "http://localhost:5005/conversations/test_user42/tracker/events"

# Gửi sự kiện 'restart' để reset session của người dùng
reset_payload = [{"event": "restart"}]
reset_response = requests.post(reset_url, json=reset_payload)

# Payload là tin nhắn từ người dùng gửi đến bot
payload = {
    "sender": "test_user42",  # Tên của người gửi
    "message": "How much does it cost to fly from Tokyo to Seoul"  # Tin nhắn từ người dùng
    #"message": "hi there"  # Tin nhắn từ người dùng
}

# Gửi request POST tới Rasa server với payload JSON
response = requests.post(url, json=payload)

# Kiểm tra phản hồi từ server
if response.status_code == 200:
    print('thành công kết nối')
    print(response.json())  # In ra phản hồi của bot
else:
    print(f"Error: {response.status_code}, {response.text}")
