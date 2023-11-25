import requests

url = "https://api.courier.com/auth/issue-token"

payload = {
  "scope": "user_id:user_id_you_want_to_create_scope_for read:messages",
  "expires_in": "2 days"
}
headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)