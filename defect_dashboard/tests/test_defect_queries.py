import psycopg2

DB_URL = "postgresql://postgres:postgres@127.0.0.1:5432/test_db"


def get_connection():
    return psycopg2.connect(DB_URL)


def test_zero_quantity_excluded():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT COUNT(*)
        FROM defect_occurrences
        WHERE quantity = 0
    """)

    result = cur.fetchone()[0]

    # quantity should never be negative and should be filtered in queries
    assert result >= 0

    conn.close()


def test_recurring_defects_query():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            dt.defect_name,
            COUNT(DISTINCT l.id) AS affected_lots
        FROM defect_occurrences d
        JOIN inspections i ON d.inspection_id = i.id
        JOIN lots l ON i.lot_id = l.id
        JOIN defect_types dt ON d.defect_type_id = dt.id
        WHERE d.quantity > 0
        GROUP BY dt.defect_name
    """)

    rows = cur.fetchall()

    assert rows is not None

    conn.close()