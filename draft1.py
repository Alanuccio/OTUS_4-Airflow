from time import time
from psycopg2 import extensions, connect, InterfaceError


def check_poll_status(conn: connect):
    """
    extensions.POLL_OK == 0
    extensions.POLL_READ == 1
    extensions.POLL_WRITE == 2
    """

    if conn.poll() == extensions.POLL_OK:
        print("POLL: POLL_OK")
    if conn.poll() == extensions.POLL_READ:
        print("POLL: POLL_READ")
    if conn.poll() == extensions.POLL_WRITE:
        print("POLL: POLL_WRITE")
    return conn.poll()
# End check_poll_status


def get_transaction_status(conn: connect):

    # print the connection status
    print("\nconn.status:", conn.status)

    # evaluate the status for the PostgreSQL connection
    if conn.status == extensions.STATUS_READY:
        print("psycopg2 status #1: Connection is ready for a transaction.")

    elif conn.status == extensions.STATUS_BEGIN:
        print("psycopg2 status #2: An open transaction is in process.")

    elif conn.status == extensions.STATUS_IN_TRANSACTION:
        print("psycopg2 status #3: An exception has occured.")
        print("Use tpc_commit() or tpc_rollback() to end transaction")

    elif conn.status == extensions.STATUS_PREPARED:
        print("psycopg2 status #4:A transcation is in the 2nd phase of the process.")
    return conn.status
# End get_transaction_status


def main():

    conn = None

    try:
        conn = connect("""
            host=rc1c-t29vq5k95bcqks94.mdb.yandexcloud.net
            port=6432
            dbname=db_alanuccio
            user=katakato
            password=k@t@k@tO
            target_session_attrs=read-write
            sslmode=verify-full
        """)

        # curs = conn.cursor()

        # get the poll status BEFORE
        check_poll_status(conn)

        # get transaction status BEFORE
        get_transaction_status(conn)
    except Exception as e:
        raise e
    finally:
        if conn:
            conn.close()

    # query_str = "SELECT table_name FROM information_schema.tables "\
    #             "WHERE table_schema = 'public'"
    # result = curs.execute(query_str)
    # if result:
    #     for n, row in enumerate(result.fetchall(), 1):
    #         print(f'{n}: {row}')
    # else:
    #     print('Nothing to print')
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
