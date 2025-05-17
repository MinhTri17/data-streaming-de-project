from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import uuid

import json
from kafka import KafkaProducer
import time


default_args = {
    'owner': 'justin',
    'start_date': datetime(2024,12,4)
}


def get_data():
    import requests

    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    res = res['results'][0]

    return res

def format_data(res):
    data = {}
    location = res['location']
    data['id'] = str(uuid.uuid4())
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
                      f"{location['city']}, {location['state']}, {location['country']}"
    data['post_code'] = location['postcode']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['registered_date'] = res['registered']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium']

    return data

def stream_data():
    producer = KafkaProducer(bootstrap_servers=['broker:29092'], max_block_ms=5000)
    curr_time = time.time()


    while time.time() < curr_time + 60:
        try:
            print(time.time())
            res = get_data()
            res = format_data(res)
            print(json.dumps(res,indent=3))
    
            producer.send('users_created', json.dumps(res).encode('utf-8'))
        except Exception as e:
            continue

dag =  DAG('user_automation',
            default_args=default_args,
            schedule_interval='@daily',
            catchup=False) 

streaming_task = PythonOperator(
        task_id='stream_data_from_api',
        python_callable=stream_data,
        dag = dag
    )
stream_data