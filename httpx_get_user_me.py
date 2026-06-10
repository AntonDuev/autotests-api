import httpx

login_payload = {
    "email": "user@example.com",
    "password": "string"
}

login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()

print("Login response:", login_response_data)
print("Status Code:", login_response.status_code)

me_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}",
}

me_response = httpx.get('http://localhost:8000/api/v1/users/me', headers=me_headers)
me_response_data = me_response.json()

print("Me response:", me_response_data)
print("Status Code:", me_response.status_code)

