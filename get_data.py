import os
import requests

base_url = "https://quanlytramxang.asigroup.vn/uploads/"

folder_path = '.'

# Danh sách để lưu trữ các đường dẫn ảnh
image_paths = []

for file_name in os.listdir(folder_path):
    # Kiểm tra xem file có phải là file .sql không
    if file_name.endswith('.sql'):
        # Tạo đường dẫn đầy đủ tới file
        file_path = os.path.join(folder_path, file_name)

# Mở file để đọc
        with open(file_path, 'r', encoding='utf-8') as file:
            # Bỏ qua dòng đầu tiên chứa tên các cột
            next(file)
            # Đọc từng dòng dữ liệu
            for line in file:
                parts = line.strip().split(',')
                image_path = parts[1]
                image_paths.append(image_path)

download_folder = "DATA_FULL"
if not os.path.exists(download_folder): os.makedirs(download_folder)

for image_path in image_paths:
    # Tạo URL đầy đủ cho ảnh
    image_url = base_url + image_path
    filename = image_path.replace("/", "_")  # Thay thế '/' với '_' để tránh lỗi đường dẫn
    filepath = os.path.join(download_folder, filename)
    
    # Thực hiện GET request để tải ảnh
    response = requests.get(image_url)
    
    # Kiểm tra xem request có thành công không
    if response.status_code == 200:
        with open(filepath, 'wb') as f:
            f.write(response.content)