# 2023_9_16
import json
import json
from python_function import encrypt, write_data_to_contract, read_data_from_sqlite, read_data_from_contract, decrypt
import requests
import schedule
import time
import datetime

# 接受一個輸入參數代表每天幾點幾分開始 Call API 並上傳至以太坊
import argparse
# 創建ArgumentParser對象
parser = argparse.ArgumentParser(description='提供在每天固定時間 Call API 並上傳至以太坊')
# 添加命令行參數
parser.add_argument('upLoadTime', type=str, default='03:00', help='請輸入要在每天幾點幾分上傳，例如 03:00')
# 解析命令行參數
args = parser.parse_args()
# 輸出消息

# 打開一個文件以進行寫入，如果文件不存在，則會自動創建
with open('dailyUpload.log', 'w') as file:
    file.write('每天上傳時間是：' + args.upLoadTime + '\n')
# 文件在離開"with"區塊後自動關閉




# 设置警告消息过滤 2023_9_10
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

json_data = "";
    
def get_data():
    # Call BRook API to read Research Data to upload to Ethereum
    # 定义API的URL
    api_url = "http://10.0.129.5:8000/api/rbook/give_to_block_chain/"

    # 发起GET请求
    response = requests.get(api_url)
    global json_data

    # 检查是否成功获取响应
    if response.status_code == 200:
        # 如果响应成功，可以打印响应内容
        json_data = response.text
    else:
        # 打開一個文件以進行寫入，如果文件不存在，則會自動創建
        with open('dailyUpload.log', 'w') as file:
            # 如果响应失败，打印错误信息
            file.write("请求失败，状态码: " + response.status_code + '\n')
        # 文件在離開"with"區塊後自動關閉

    try:
        # Encrypt the JSON data using the 'encrypt' function from python_function
        encrypted_data = encrypt(json_data)
 
        # Call the function to write data to the contract and get the transaction hash
        tx_hash = write_data_to_contract(encrypted_data)
        
        done_upload_tim = datetime.datetime.now()
        # 格式化时间为字符串
        formatted_time = done_upload_tim.strftime("%Y-%m-%d %H:%M:%S")
        # 创建带有时间的字符串
        message = f"@{formatted_time} 上傳以太坊完成。"
        # 输出带有时间的字符串
       
        # 打開一個文件以進行寫入，如果文件不存在，則會自動創建
        with open('dailyUpload.log', 'w') as file:
            file.write(message)
        # 文件在離開"with"區塊後自動關閉

       
        return json.dumps(message=tx_hash.hex())
    except Exception as e:
        return json.dumps({'error': str(e)})

if __name__ == '__main__':
    scheduler = schedule.Scheduler()
    job = schedule.every().day.at(args.upLoadTime).do(get_data).tag('上傳以太坊')
    
    current_time = datetime.datetime.now()
    next_run_time = job.next_run
    datetimeDiff = job.next_run - datetime.datetime.now();
    secondsDiff = datetimeDiff.total_seconds();
    
    # 打開一個文件以進行寫入，如果文件不存在，則會自動創建
    with open('dailyUpload.log', 'w') as file:
        file.write("当前时间: " + current_time.strftime("%Y-%m-%d %H:%M:%S") + "; 下一次执行时间: " + next_run_time.strftime("%Y-%m-%d %H:%M:%S") + "; 等待到达执行时间: " + str(datetimeDiff) + " 相當於 " + str(secondsDiff) + " 秒." + "\n");
    # 文件在離開"with"區塊後自動關閉
    
    while True:
        # 等待到达下次执行
        time.sleep((job.next_run - datetime.datetime.now()).total_seconds());

        # 执行任务
        schedule.run_pending()

        # 等待到达执行时间
        current_time = datetime.datetime.now()
        next_run_time = job.next_run
        datetimeDiff = job.next_run - datetime.datetime.now()
        #datetimeDiff_str = str(datetimeDiff);
        secondsDiff = datetimeDiff.total_seconds();

        # 打開一個文件以進行寫入，如果文件不存在，則會自動創建
        with open('dailyUpload.log', 'w') as file:
            file.write("当前时间: " + current_time.strftime("%Y-%m-%d %H:%M:%S") + "; 下一次执行时间: " + next_run_time.strftime("%Y-%m-%d %H:%M:%S") + "; 等待到达执行时间: " + str(datetimeDiff) + " 相當於 " + str(secondsDiff) + " 秒." + "\n");
        # 文件在離開"with"區塊後自動關閉
