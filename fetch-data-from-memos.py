import sqlite3
import sys
import datetime

sql_fetch_memo = """
    SELECT * FROM memo;
"""

sql_fetch_resource = """
    SELECT * FROM resource;
"""

separator = '---------'

def stage1(file_path, record_file):
    conn = sqlite3.connect(file_path)
    cursor = conn.cursor()

    cursor.execute(sql_fetch_memo)
    memos = cursor.fetchall()

    cursor.execute(sql_fetch_resource)
    resources = cursor.fetchall()


    with open(record_file, 'w') as record:
        for memo in memos:
            time = datetime.datetime.fromtimestamp(memo[4]) \
                    .strftime('[%Y-%m-%d %H:%M] : ')
            record.write(separator + '\n')
            record.write(time)

            content = memo[-2]
            record.write(content + '\n')

        for resource in resources:
            blob = resource[-6].decode('utf-8')
            record.write(separator + '\n')
            record.write(blob + '\n')

    cursor.close()
    conn.close()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("give me memos' sqlite db")
        sys.exit(1)

    file_path = sys.argv[1]
    stage1(file_path, 'record_file.txt')