from google.cloud import bigquery

def main():
    orderdict = get_most_recent_order()
    insert_order_details('1', '2024-05-01T10:00:00Z', 'Item A,Item B', 'Shipped')
    q = ''

def get_most_recent_order():
    client = bigquery.Client()
    table_id = "leafy-star-418020.OrbitMetricsData.orders"
    table = client.get_table(table_id)

    query =f"""
    SELECT *
    FROM {table_id}
    ORDER BY order_date DESC
    LIMIT 1;
    """

    rows = client.query(query).result()

    single_order_as_dict = {}
    # size of rows will be one, since the query was limited to 1 result
    for row in rows:
        single_order_as_dict['order_id'] = row.get('order_id') 
        single_order_as_dict['order_date'] = row.get('order_date')
        single_order_as_dict['order_details'] = row.get('order_details')
        single_order_as_dict['order_status'] = row.get('order_status')
       
    return single_order_as_dict   

def insert_order_details(order_id, order_date, order_details, order_status):
    client = bigquery.Client()
    table_id = "leafy-star-418020.OrbitMetricsData.orders"
    table = client.get_table(table_id)

    query =f"""
    INSERT INTO {table_id} (order_id, order_date, order_details, order_status)
    VALUES
    ({order_id}, '{order_date}', '{order_details}', '{order_status}');
    """

    response = client.query(query).result()
    j = ''
if __name__ == '__main__':
    main()
