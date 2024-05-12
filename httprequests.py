import requests
import json

def execute_requests(url, requests_data):
    valid_methods = {"GET", "POST", "PUT", "DELETE", "PATCH", "HEAD"}

    for request_data in requests_data:
        method = request_data.get("method", "").upper()
        data = request_data.get("data")

        if method not in valid_methods:
            print(f"Invalid method {method} in request. Skipping...")
            continue

        try:
            if method == "GET":
                response = requests.get(url)
                if response.status_code == 200:
                    data1 = response.json() # Chuyển đổi dữ liệu JSON thành một đối tượng Python
                    print("Data reveived:")
                    print(data1) # In dữ liệu nhận được
            elif method == "POST":
                response = requests.post(url, json=data)
                if response.status_code == 201:  # Kiểm tra nếu POST thành công (status code 201 Created)
                    print("Data posted successfully:")
                    print(response.json())  # In ra dữ liệu vừa được post
            elif method == "PUT":
                response = requests.put(f"{url}/{data['id']}", json=data)
                if response.status_code == 200:  # Kiểm tra nếu PUT thành công (status code 200 OK)
                    print("Data updated successfully:")
                    print(response.json())  # In ra dữ liệu vừa được cập nhật
            elif method == "DELETE":
                response = requests.delete(f"{url}/{data['id']}")
            elif method == "PATCH":
                response = requests.patch(f"{url}/{data['id']}", json=data)
                if response.status_code == 200:  # Kiểm tra nếu PATCH thành công (status code 200 OK)
                    print("Data patched successfully:")
                    print(response.json())  # In ra dữ liệu vừa được patch
            elif method == "HEAD":
                response = requests.head(url)
                if response.status_code == 200:
                    print("Headers received:")
                    print(response.headers)  # In các tiêu đề của tài nguyên

            if response.status_code >= 200 and response.status_code < 300:
                print(f"{method} request was successful with status code {response.status_code}")
            elif response.status_code == 405:
                print(f"Method {method} is not allowed for URL {url}")
            else:
                raise Exception(f"{method} request failed with status code {response.status_code}")
        except Exception as e:
            print(f"An exception occurred during {method} request: {e}")

def main():
    url = 'https://jsonplaceholder.typicode.com/posts'
    
    # Đọc dữ liệu từ tệp JSON
    with open("C:\Users\phuon\OneDrive - actvn.edu.vn\Máy tính\MANGUON/requests.json", "r") as json_file:
        requests_data = json.load(json_file)

    execute_requests(url, requests_data)

if __name__ == "__main__":
    main()