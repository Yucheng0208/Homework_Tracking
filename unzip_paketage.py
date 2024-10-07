import zipfile
import os

def extract_all_zips_in_directory(directory_path, extract_to_directory):

    # 檢查目標資料夾是否存在，若不存在則建立
    if not os.path.exists(extract_to_directory):
        os.makedirs(extract_to_directory)
    
    # 遍歷資料夾下的所有檔案
    for file_name in os.listdir(directory_path):
        # 確認檔案是以 .zip 結尾
        if file_name.endswith(".zip"):
            zip_file_path = os.path.join(directory_path, file_name)
            print(f"正在解壓縮: {zip_file_path}")
            
            # 解壓縮 ZIP 檔案
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                # 解壓縮到對應目標資料夾內的子資料夾，以 ZIP 檔案名稱命名
                output_path = os.path.join(extract_to_directory, os.path.splitext(file_name)[0])
                if not os.path.exists(output_path):
                    os.makedirs(output_path)
                zip_ref.extractall(output_path)
                print(f"已成功解壓縮至: {output_path}")

# 使用範例
zip_directory = 'your_zip_folder'  # 包含 ZIP 檔案的資料夾
output_directory = 'output_folder'  # 解壓縮的目標資料夾
extract_all_zips_in_directory(zip_directory, output_directory)
