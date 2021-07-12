from time import time
import psycopg2


def main():
    conn = psycopg2.connect("""
        host=rc1c-t29vq5k95bcqks94.mdb.yandexcloud.net
        port=6432
        dbname=db_alanuccio
        user=katakato
        password=k@t@k@tO
        target_session_attrs=read-write
        sslmode=verify-full
    """)

    curs = conn.cursor()

    query_str = "SELECT table_name FROM information_schema.tables "\
                "WHERE table_schema = 'public'"

    result = curs.execute(query_str)

    if result:
        for n, row in enumerate(result.fetchall(), 1):
            print(f'{n}: {row}')
    else:
        print('Nothing to print')
# End main


if __name__ == '__main__':
    start_time = time()
    delimiter = '- ' * 20 + '-'
    try:
        print(delimiter)
        main()
    except Exception as e:
        raise e
    finally:
        print(delimiter)
        print('Script took {:.5f} seconds'.format((time() - start_time)))
        print(delimiter)
# End
