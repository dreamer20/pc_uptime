from .db import get_db
import psycopg2.extras as extras


def get_uptime():
    db = get_db()
    cursor = db.cursor(cursor_factory=extras.DictCursor)
    cursor.execute('SELECT total_uptime, last_update FROM uptime')

    return cursor.fetchone()


def update_total_uptime(uptime):
    db = get_db()
    cursor = db.cursor()
    current_uptime = get_uptime()
    new_total_uptime = current_uptime['total_uptime'] + int(uptime)
    cursor.execute(
        'UPDATE uptime SET total_uptime = %s, last_update = (SELECT NOW()) WHERE id = 1',
        (new_total_uptime, )
    )
    cursor.close()
    db.commit()

    return get_uptime()
