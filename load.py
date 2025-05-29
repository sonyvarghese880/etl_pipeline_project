import sqlite3

def load_data(df, db_file):
    conn = sqlite3.connect(db_file)
    df.to_sql('users', conn, if_exists='replace', index=False)
    conn.close()