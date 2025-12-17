from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables
import streamlit as st
import os
import mysql.connector
import google.generativeai as genai
import re

## Configure Genai Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

safety_settings = [
    {
        "category": "HARM_CATEGORY_DANGEROUS",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
]

## Load model
model=genai.GenerativeModel('gemini-pro', safety_settings=safety_settings)

## Function To Load Google Gemini Model and provide queries as response
def get_gemini_response(question, prompt, db_contents):
    contents = [prompt[0], question, db_contents]
    response = model.generate_content(contents)
    if response:
        return response.text
    else:
        return str('')


## Fucntion To retrieve query from the database
def read_sql_query(sql,db):
    host = 'localhost'
    user = 'root'
    passwd = 'Linbaynj0601'
    conn=mysql.connector.connect(user=user, password=passwd, host=host, database=db)
    cr=conn.cursor()
    cr.execute(sql)
    rows=cr.fetchall()
    conn.commit()
    cr.close()
    conn.close()
    for row in rows:
        print(row)
    return rows


## renew DB data txt file
def renew_DB(state, db, table_name=None):
    # Renew ALL DB
    if state == 'ALL DB':
        cmd = r'"C:/Program Files/MySQL/MySQL Server 8.0/bin/mysqldump.exe" -u root -p{} -h localhost {} > DBdata.txt'.format('Linbaynj0601', db)
        try:
            # Execute the command using os.system()
            result = os.system(cmd)
            if result == 0:
                print(f"DB '{db}' export successful")
            else:
                print(f"Error occurred during db'{db}' export")
        except Exception as e:
            print(f"An error occurred: {e}")

    if state == 'TABLE':
        # Construct the mysqldump command for a single table
        cmd = r'"C:/Program Files/MySQL/MySQL Server 8.0/bin/mysqldump.exe" -u root -pLinbaynj0601 -h localhost {} {} > {}.txt'.format(db, table_name, table_name)
        try:
            # Execute the command using os.system()
            result = os.system(cmd)
            if result == 0:
                print(f"Table '{table_name}' export successful")
            else:
                print(f"Error occurred during table '{table_name}' export")
        except Exception as e:
            print(f"An error occurred: {e}")

## read DB data txt file
def read_DB(state,table_name=None):
    if state == 'ALL DB':
        with open("DBdata.txt", 'r', encoding='utf-8') as file:
            db_content = file.read()
    elif state == 'TABLE':
        with open(f"{table_name}.txt", 'r', encoding='utf-8') as file:
            db_content = file.read()
    return db_content

def extract_table_name(sql_query):
    # 提取 insert 语句中的表名
    insert_pattern = r'insert\s+into\s+(\w+)'
    match = re.search(insert_pattern, sql_query, re.IGNORECASE)
    if match:
        return match.group(1)

    # 提取 create 语句中的表名
    create_pattern = r'create\s+table\s+(\w+)'
    match = re.search(create_pattern, sql_query, re.IGNORECASE)
    if match:
        return match.group(1)

    return None

## Define Your Prompt
prompt=[
    """
    You are an expert in converting questions to mySQL query, 
    and no matter what, your response must be valid mysql command.
    \n
    also you must confirm the mysql command perfectly fit the database you're using before you respond.
    \n
    also the sql code should not have ``` in beginning or end and sql word in output.
    \n
    the database info I would like to search from is as follow
    """

]

## Streamlit App

st.set_page_config(page_title="I can convert you sentense to MySQL query!")
st.header("Lazy-man's database management system")

## 設定文字輸入框，label 為 widget 的顯示文字，key 是 widget 的 ID
question=st.text_input(label="Input: ",key="input")

# choose db
choice = read_sql_query('show databases', None)
choice_list = list()
table_names = []
views_names = []
db = str()
for i in range(len(choice)):
    choice_list.append(choice[i][0])

db_option = st.sidebar.selectbox(
    'Select Database',
    choice_list)
if db_option:
    db = db_option
    read_sql_query(f'use {db}', db)
    # 首先了解db內容和有的table
    renew_DB(state='ALL DB', db=db)
    all_db_content = read_DB(state='ALL DB')
    table_names = re.findall(r'CREATE TABLE `(\w+)`', all_db_content)
    views_names = re.findall(r'CREATE VIEW `(\w+)`', all_db_content)
    st.markdown(f':orange[Tables] in :blue[{db}] are  {table_names}')
    st.markdown(f':green[Views] in :blue[{db}] are  {views_names}')
    for table in table_names:
        renew_DB(state='TABLE', db=db, table_name=table)

response = None
if question:
    tables_used = re.findall(r'`(\w+)`', question)

    if tables_used:
        for table in tables_used:
            if table in table_names:
                db_contents = read_DB(state='TABLE', table_name=table)
                response = get_gemini_response(question, prompt, db_contents)
    else:  # 如果沒有提到 table 就讀 DBdata.txt
        renew_DB(state='ALL DB', db=db)
        all_db_content = read_DB(state='ALL DB')
        response = get_gemini_response(question, prompt, all_db_content)
        
    # 如果 response 修改了資料庫
    if 'insert' in response.lower() or 'create' in response.lower():
        table_name = extract_table_name(response)
        if table_name:
            renew_DB(state='TABLE', db=db, table_name=table_name)
            
    # 立即執行並顯示 response 結果
    # st.subheader(f'The SQL command is:')
    # st.write(response)
    output = read_sql_query(response, db)
    
    # 保存 response 到 session_state 供編輯用
    if 'question' not in st.session_state:
        st.session_state['question'] = None
    if question != st.session_state['question']:
        st.session_state['response'] = response
        st.session_state['output'] = output
        if 'edited_query' in st.session_state:
            del st.session_state['edited_query']
    if ('edit_query_shown' not in st.session_state) or (question != st.session_state['question']):
        st.session_state['edit_query_shown'] = False
    st.session_state['question'] = question
    
    # 立即執行並顯示 response 結果
    st.subheader(f'The SQL command is:')
    st.write(st.session_state['response'])

# 顯示結果
if 'output' in st.session_state:
    st.subheader("The Response is:")
    for row in st.session_state['output']:
        st.write(row)

if 'edit_query_shown' not in st.session_state:
        st.session_state['edit_query_shown'] = False

# 添加 Edit Query 按鈕
if 'response' in st.session_state:
    # if 'edit_query_shown' not in st.session_state:
    #     st.session_state['edit_query_shown'] = False

    if st.button('Edit Query') or st.session_state['edit_query_shown']:
        st.session_state['edit_query_shown'] = True
        edited_query = st.text_area("Edit your query:", value=st.session_state['response'])
        if st.button('Submit Edited Query'):
            st.session_state['edited_query'] = edited_query
            # 立即執行用戶編輯過的查詢
            st.session_state['output'] = read_sql_query(st.session_state['edited_query'], db)

# 顯示經過編輯的查詢及結果
if 'edited_query' in st.session_state and st.session_state['edit_query_shown']:
    st.subheader("The Edited SQL command is:")
    st.write(st.session_state['edited_query'])
    st.subheader("The Edited Response is:")
    for row in st.session_state['output']:
        st.write(row)