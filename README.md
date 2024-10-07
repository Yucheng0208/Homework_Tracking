## 語言選擇 / Language Selection

- [繁體中文](#繁體中文說明)
- [简体中文](#简体中文说明)
- [English](#english-description)

---

## 繁體中文說明

### input_output_checking.py
這個腳本用於批改學生的作業。它會遍歷指定的學生程式資料夾，依據給定的測試案例，執行學生的程式，並比對實際輸出與預期輸出。如果輸出正確，將成績記錄到 CSV 檔案中。該腳本提供了一個自動化批改作業的方式，節省教師大量時間。

#### 主要功能：
- 遍歷指定的資料夾以尋找學生的 `.py` 檔案。
- 逐一執行每個學生程式，並根據預期輸出進行檢查。
- 將測試結果與分數寫入 CSV 檔案。

### unzip_paketage.py
這個腳本用於解壓縮指定資料夾中的所有 ZIP 檔案。每個 ZIP 檔案會被解壓縮到相應的子資料夾，子資料夾名稱與 ZIP 檔案名稱相同。

#### 主要功能：
- 檢查指定資料夾內所有的 ZIP 檔案。
- 解壓縮每個 ZIP 檔案到指定的目標資料夾內。

#### 授權
本專案採用 [MIT 授權條款](./LICENSE) 授權。您可以自由修改和分發程式碼。

---

## 简体中文说明

### input_output_checking.py
这个脚本用于批改学生的作业。它会遍历指定的学生程序文件夹，依据给定的测试用例，执行学生的程序，并比对实际输出与预期输出。如果输出正确，将成绩记录到 CSV 文件中。该脚本提供了一个自动化批改作业的方式，节省教师大量时间。

#### 主要功能：
- 遍历指定的文件夹以寻找学生的 `.py` 文件。
- 逐一执行每个学生程序，并根据预期输出进行检查。
- 将测试结果与分数写入 CSV 文件。

### unzip_paketage.py
这个脚本用于解压指定文件夹中的所有 ZIP 文件。每个 ZIP 文件会被解压到相应的子文件夹，子文件夹名称与 ZIP 文件名称相同。

#### 主要功能：
- 检查指定文件夹内所有的 ZIP 文件。
- 解压每个 ZIP 文件到指定的目标文件夹内。

#### 许可证
本项目采用 [MIT 许可证](./LICENSE) 许可。您可以自由修改和分发代码。

---

## English Description

### input_output_checking.py
This script is designed for grading students' assignments. It iterates over the specified student program folder, executes each student's script based on predefined test cases, and compares the actual output with the expected output. If the output is correct, the result is logged into a CSV file. This script automates the grading process, saving teachers significant time.

#### Key Features:
- Iterates through a specified folder to locate `.py` files of students.
- Executes each student's program one by one and checks the output against expected results.
- Writes the test results and scores into a CSV file.

### unzip_paketage.py
This script is used for extracting all ZIP files in a specified directory. Each ZIP file is extracted into a corresponding subfolder with the same name as the ZIP file.

#### Key Features:
- Scans the specified directory for ZIP files.
- Extracts each ZIP file into a target directory.

#### License
This project is licensed under the [MIT License](./LICENSE). You are free to modify and distribute the code.