
def table():
    table = """\
    CREATE TABLE IF NOT EXISTS club
    (
    dt date,
    data_time timestam,
    club TEXT,
    load INTEGER,
    taken INTEGER,
    free INTEGER,
    guest INTEGER,
    resident INTEGER,
    admin INTEGER,
    workers INTEGER,
    school INTEGER
    );
"""
    return table

def ins_club_stat():
    return 'insert into club values (?,?,?,?,?,?,?,?,?,?,?)'