from flask import Flask, render_template, request, jsonify
import sqlite3
from python_function import extract_data_from_postgre, encrypt, write_data_to_contract, read_data_from_contract, decrypt

app = Flask(__name__)

# Endpoint for research data upload page
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        search_date = request.form['search_date']
        search_time = request.form['search_time']
        search_employee_id = request.form['search_employee_id']
        
        # Connect to the database and search for transaction hash
        conn = sqlite3.connect('search.db')
        c = conn.cursor()
        c.execute("SELECT distinct transactionHash_str FROM search WHERE date=? AND time=? AND employee_id=?",
                  (search_date, search_time, search_employee_id))
        tx_hash = c.fetchone()
        conn.commit()
        conn.close()

        if tx_hash is not None:
            return render_template('upload.html', error_message='transaction is already in SQLite database')

        else:
            # Call function to extract data from Postgres database
            data = extract_data_from_postgre(search_date, search_time, search_employee_id)
            
            # if data not founs, return error
            if data is None:
                return render_template('upload.html', error_message='No data found for the given search criteria')
    
            # Encrypt data
            base64_data = encrypt(data)
            
            # write data to blockchain
            tx_hash = write_data_to_contract(search_date, search_time, search_employee_id, base64_data)
    
            return render_template('up_result.html', date=search_date, time=search_time, employee_id=search_employee_id, tx_hash=tx_hash)

    # If method is GET, just render the upload page
    return render_template('upload.html')

    
# Endpoint for research data download page
@app.route('/transactions', methods=['GET', 'POST'])
def transactions():
    # If method is POST, execute the data from blocchain
    if request.method == 'POST':
        selected_date = request.form['date']
        selected_time = request.form['time']
        selected_employee_id = request.form['hempId']
        
        # Connect database and extract transaction hash
        conn = sqlite3.connect('search.db')
        c = conn.cursor()
        c.execute("SELECT distinct transactionHash_str FROM search WHERE date=? AND time=? AND employee_id=?",
                  (selected_date, selected_time, selected_employee_id))
        tx_hash = c.fetchone()
        tx_hash = tx_hash[0]
        conn.commit()
        conn.close()

        # if transaction hash not found, return error
        if tx_hash is None:
            return render_template('transactions.html', error_message='No data found for the given search criteria')      

        # send transaction hash to block chain and read the data
        encrypted_data = read_data_from_contract(tx_hash)
        
        # decrypt data
        data = decrypt(encrypted_data)

        return render_template('down_result.html', date=selected_date, time=selected_time, employee_id=selected_employee_id,
                               data=data)

    # If method is GET, just render the upload page
    # connect database and extract date
    conn = sqlite3.connect('search.db')
    c = conn.cursor()
    c.execute('SELECT DISTINCT date FROM search ORDER BY date DESC')
    dates = c.fetchall()
    conn.close()

    # return date lists
    return render_template('transactions.html', dates=dates)

# extract time from sqlite database
@app.route('/get_times')
def get_times():
    # Get the selected date from the query string parameters
    selected_date = request.args.get('date')

    # connect database and extract time
    conn = sqlite3.connect('search.db')
    c = conn.cursor()
    c.execute('SELECT DISTINCT time FROM search where date = ? ORDER BY time DESC', (selected_date,))
    times = c.fetchall()
    conn.close()

    # return time lists
    return jsonify(times=times)
  
# extract employee id from sqlite database  
@app.route('/get_empIds')
def get_empIds():
    # Get the selected date and time from the query string parameters
    selected_date = request.args.get('date')
    selected_time = request.args.get('time')

    # connect database and extract employee id
    conn = sqlite3.connect('search.db')
    c = conn.cursor()
    c.execute('SELECT DISTINCT employee_id FROM search where date = ? and time = ? ORDER BY time DESC', (selected_date, selected_time,))
    empIds = c.fetchall()
    conn.close()

    # return employee id lists
    return jsonify(empIds=empIds)


if __name__ == '__main__':
    app.run(debug=True)
