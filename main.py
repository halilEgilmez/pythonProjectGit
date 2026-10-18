import os
import sqlite3


def create_database():
    if os.path.exists("students.db"):
        os.remove("students.db")


    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    return conn, cursor

def main():
    conn, corsor = create_database()
