import os
import subprocess
import sys
import csv

# 設定學生程式所在的資料夾
students_folder = 'students_programs'

# 準備 CSV 檔案
csv_file_name = 'grading_results.csv'

# 準備測試案例列表
test_cases = [
    {
        'input': None,  # 如果程式不需要輸入，設為 None
        'expected_output': [
            '期望的輸出結果1',
            '期望的輸出結果2'
        ]
    },
    # 可以添加更多測試案例
]

# 打開 CSV 檔案，準備寫入
with open(csv_file_name, mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    # 寫入表頭
    writer.writerow(['學號', '成績'])

    # 遍歷學生程式資料夾
    for filename in os.listdir(students_folder):
        if filename.endswith('.py'):
            # 提取檔案名稱，不包括副檔名
            basename = filename[:-3]  # 去除 '.py'

            # 提取底線之前的學號
            student_id = basename.split('_')[0]  # 取得底線前的部分

            student_file = os.path.join(students_folder, filename)
            print(f'正在批改學生 {student_id} 的作業...')

            # 記錄學生是否通過所有測試
            all_passed = True

            for index, test_case in enumerate(test_cases):
                print(f'測試案例 {index + 1}：')

                # 構建命令，執行學生的程式
                cmd = [sys.executable, student_file]

                try:
                    # 執行學生的程式
                    process = subprocess.Popen(
                        cmd,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True,
                        timeout=5  # 設定超時
                    )

                    # 傳遞輸入資料（如果有）
                    input_data = test_case.get('input', None)
                    stdout, stderr = process.communicate(input=input_data)

                    # 獲取程式的返回碼
                    return_code = process.returncode

                    # 處理執行結果
                    if return_code != 0:
                        print(f'程式執行錯誤，錯誤訊息：{stderr.strip()}')
                        all_passed = False
                        break  # 可以選擇是否繼續測試下一個案例
                    else:
                        # 比較輸出結果
                        output = stdout.strip()
                        # 將輸出和預期輸出都處理為列表，逐行比較
                        output_lines = output.strip().split('\n')
                        expected_lines = test_case['expected_output']

                        if output_lines == expected_lines:
                            print('通過')
                        else:
                            print(f'未通過，預期輸出：{expected_lines}，實際輸出：{output_lines}')
                            all_passed = False
                            break  # 如果需要測試所有案例，可移除此行

                except subprocess.TimeoutExpired:
                    print('程式執行超時')
                    all_passed = False
                    break  # 可以選擇是否繼續測試下一個案例

            # 如果通過所有測試，記錄到 CSV 檔案
            if all_passed:
                # 假設成績為 100 分
                score = 100
                writer.writerow([student_id, score])
                print(f'學生 {student_id} 的作業通過所有測試，成績為 {score} 分。\n')
            else:
                # 如果未通過，可以選擇是否記錄
                print(f'學生 {student_id} 的作業未通過所有測試。\n')
