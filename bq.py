from google.cloud import bigquery

def main():
    client = bigquery.Client()
    table_id = "leafy-star-418020.OrbitMetricsData.orders"
    table = client.get_table(table_id)

    query = """
    SELECT *
    FROM `leafy-star-418020.OrbitMetricsData.orders`
    ORDER BY order_date DESC
    LIMIT 1;
    """

    rows = client.query(query).result()
    for row in rows:
        print(row)

if __name__ == '__main__':
    main()
