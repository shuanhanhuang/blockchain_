# 2023_9_10 原版

import json
from flask import Flask, render_template, request, jsonify
from python_function import encrypt, write_data_to_contract, read_data_from_sqlite, read_data_from_contract, decrypt
import requests
import schedule
import time

# 设置警告消息过滤 2023_9_10
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

json_data = "";
    
@app.route('/upload/')
def upload():
    return render_template('upload.html')

@app.route('/get_data', methods=['GET'])
def get_data():
    # Return the JSON data directly
    # return jsonify(data=json_data)

    print("@ /encrypt_and_print")
        
    # Call BRook API to read Research Data to upload to Ethereum
    # 定义API的URL
    # api_url = "http://59.124.122.57:8000/api/rbook/give_to_block_chain/"
    api_url = "http://10.0.129.5:8000/api/rbook/give_to_block_chain/"

    # 发起GET请求
    response = requests.get(api_url)

    # 检查是否成功获取响应
    if response.status_code == 200:
        # 如果响应成功，可以打印响应内容
        print("响应内容:")
        global json_data
        json_data = response.text
        #print("@ /get_data, json_data = ", json_data)
    else:
        # 如果响应失败，打印错误信息
        print("请求失败，状态码:", response.status_code)

    return jsonify(data=json_data)

@app.route('/encrypt_and_print', methods=['POST'])
def encrypt_and_print():
    try:
        print("@ /encrypt_and_print")
        # Encrypt the JSON data using the 'encrypt' function from python_function
        global json_data;
        #print("@ /encrypt_and_print = json_data", json_data)

        encrypted_data = encrypt(json_data)
        # print("encrypted_data: ", encrypted_data)
        # Call the function to write data to the contract and get the transaction hash
        tx_hash = write_data_to_contract(encrypted_data)
        print("@ /encrypt_and_print", tx_hash)
        return jsonify(message=tx_hash.hex())
    except Exception as e:
        return jsonify(error=str(e))

@app.route('/get_options', methods=['GET'])
def get_options():
    # Get the options (results) from the database
    options = read_data_from_sqlite() # print(options)
    return jsonify(options=options)

@app.route('/transaction/')
def transaction():
    return render_template('transactions.html')

@app.route('/transactions_2023_9_11/')
def transactions_2023_9_11():
    return render_template('transactions_2023_9_11.html')

@app.route('/transactions_2023_9_10/')
def transactions_2023_9_10():
    return render_template('transactions_2023_9_10.html')

@app.route('/find_data', methods=['GET'])  # Specify GET method
def find_data():
    try:
        # print("@ find_data...Entering")
        selectedValue = request.args.get('selectedValue')  # Retrieve the selected value from the query parameter
        # print("@ find_data, selectedValue = ", selectedValue)
        parts = selectedValue.split(",")
        selected_part = parts[1]
        # print("@ find_data, parts[1] = ", parts[1])
        encrypted_data=read_data_from_contract(selected_part)
        # print("@ find_data, encrypted_data = ", encrypted_data)
        result = decrypt(encrypted_data)
        # print("@ find_data, decrypt result = ", result)

        # 寫入檔案開始

        # 指定要写入的文件名
        file_name = '研究紀錄資料自區塊鏈下載.txt'

        # 打开文件以进行写入
        with open(file_name, 'w') as file:
            # 将字符串写入文件
            file.write(result)

        # print(f'交易收据已写入文件: {file_name}')  
        # 寫入檔案結束
  
        return jsonify(result=result)

    except Exception as e:
        return jsonify(error=str(e))
        
@app.route('/jsontohtml/')
def jsontohtml():
    return render_template('jsontohtml.html')

@app.route('/tab_example/')
def tab_example():
    return render_template('tab_example.html')

@app.route('/upload_test/')
def upload_test():
    return render_template('upload_test.html')

@app.route('/upload_test2/')
def upload_test2():
    return render_template('upload_test2.html')

@app.route('/transactions_Table/')
def transactions_Table():
    return render_template('transactions_Table.html')

if __name__ == '__main__':
    app.run(debug=True)
