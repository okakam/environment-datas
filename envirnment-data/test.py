from google.cloud import bigquery

project_id = "okazaki-data-project"
dataset_id = "environment"
table_id = "environment"

client = bigquery.Client(project=project_id, location="asia-southeast1")
table_ref = client.dataset(dataset_id).table(table_id)

data = {
    'temp': 10.00,
    'hum': 10.00,
    'pressure': 10.00,
    'co2': 10.00
}

print(f"data : {data}")

# BigQuery に挿入するための行を作成します
rows_to_insert = [data]

try:
    # データを BigQuery に挿入します
    errors = client.insert_rows_json(table_ref, rows_to_insert)
    print(f"errors : {errors}")
    if errors == []:
        print("New rows have been added.")
    else:
        print(f"Encountered errors while inserting rows: {errors}")
except Exception as e:
    print(f"Exception : {e}")
    