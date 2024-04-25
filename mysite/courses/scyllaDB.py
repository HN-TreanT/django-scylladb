from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import json
from cassandra.query import ordered_dict_factory
# try:
#     auth_provider = PlainTextAuthProvider(username='cassandra', password='cassandra')
#     cluster = Cluster(['172.17.0.2'], port=9042, auth_provider=auth_provider)
#     print("connecting.....")
#     session = cluster.connect()
#     print("Connected to the cluster")
#     rows = session.execute('SELECT release_version FROM system.local')
#     for row in rows:
#         print(row)
#     session.shutdown()
#     cluster.shutdown()
# except Exception as e:
#     print("Error:", e)


def connect_to_scylla(ip, username, password):
    auth_provider = PlainTextAuthProvider(username=username, password=password)
    cluster = Cluster([ip], port=9042, auth_provider=auth_provider)
    session = cluster.connect(keyspace="test2_keyspace", wait_for_all_pools=False) 
    session.row_factory = ordered_dict_factory
    return session
def create_keyspace(session, keyspace): 
    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS %s
        WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '1' }\
        """ % keyspace)
    session.set_keyspace(keyspace)
def create_table(session, table_name):
    create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id int,
            name text,
            PRIMARY KEY (id)
        )
    """
    session.execute(create_table_query)
def insert_data(session, value1, value2, table_name):
    insert_query = f"""
        INSERT INTO {table_name} (id, name) VALUES (%s, %s)
    """
    session.execute(insert_query, (value1, value2))
def query_data(session, value, table_name):
    select_query = f"SELECT * FROM {table_name} WHERE id = %s"
    result = session.execute(select_query, (value,))
    json_result = []
    for row in result:
        json_result.append(dict(row))
    return json.dumps(json_result)
def update_data(session, new_value, id):
    update_query = "UPDATE test SET name = %s WHERE id = %s"
    session.execute(update_query, (new_value, id))
def delete_data(session, key):
    delete_query = "DELETE FROM test WHERE id = %s"
    session.execute(delete_query, (key,))
def main():
    session = connect_to_scylla("172.17.0.2","cassandra", "cassandra")
    # create_keyspace(session=session, keyspace="test2_keyspace")
    # create_table(session=session, table_name="test")
    # insert_data(session=session,value1=1, value2="Nam", table_name="test")
    # result = query_data(session=session, value=1, table_name="test")
    # print(result)
    
    # update_data(session=session,new_value="name2",id=1)
    delete_data(session=session,key=1)    
    session.shutdown()
    


main()
    
    
    
    
