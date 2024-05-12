import json

# Dữ liệu mẫu
requests_data = [
    {"method": "GET"},
    {"method": "POST", "data": {"title": "New Post 1", "body": "This is a new post 1"}},
    {"method": "PUT", "data": {"id": 1, "title": "Updated Post 1", "body": "This post has been updated 1"}},
    {"method": "DELETE", "data": {"id": 1}},
    {"method": "PATCH", "data": {"id": 2, "title": "Patched Post 2"}},
    {"method": "POST", "data": {"title": "New Post 3", "body": "This is a new post 3"}},
    {"method": "PUT", "data": {"id": 3, "title": "Updated Post 3", "body": "This post has been updated 3"}},
    {"method": "DELETE", "data": {"id": 3}},
    {"method": "PATCH", "data": {"id": 4, "title": "Patched Post 4"}},
    {"method": "HEAD"}
]

# Tạo và ghi dữ liệu vào tệp JSON
with open("C:\Users\phuon\OneDrive - actvn.edu.vn\Máy tính\MANGUON/requests.json", "w") as json_file:
    json.dump(requests_data, json_file)