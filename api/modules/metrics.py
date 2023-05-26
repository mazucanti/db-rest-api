from sqlalchemy.sql import text

def hired_higher_than_avg(db):
    sql = (
        "WITH hired_count AS (\n"
        "    SELECT\n"
        "        d.id AS id,\n"
        "        d.department AS department,\n"
        "        COUNT(e.id) AS hired\n"
        "    FROM\n"
        "        employees e\n"
        "    INNER JOIN\n"
        "        departments d\n"
        "    ON\n"
        "        d.id = e.department_id\n"
        "    WHERE\n"
        "        EXTRACT(YEAR FROM e.datetime) = 2021\n"
        "    GROUP BY\n"
        "        d.id\n"
        "    ORDER BY\n"
        "        hired\n"
        "    DESC\n"
        "),\n"
        "hired_mean AS (\n"
        "    SELECT\n"
        "        AVG(hired) AS mean\n"
        "    FROM\n"
        "        hired_count\n"
        ")\n"
        "SELECT\n"
        "    c.id,\n"
        "    c.department,\n"
        "    c.hired\n"
        "FROM\n"
        "    hired_count AS c\n"
        "CROSS JOIN\n"
        "    hired_mean AS m\n"
        "WHERE\n"
        "    m.mean < c.hired"
    )
    with db.engine.connect() as conn:
        table = conn.execute(text(sql))
    return table
     