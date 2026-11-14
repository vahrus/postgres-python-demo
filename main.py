
import os
import sys

import psycopg2
from dotenv import load_dotenv


def main():
    load_dotenv()
    conn = None

    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT", "5432"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            connect_timeout=5,
        )

        print("Подключение к PostgreSQL успешно!\n")

        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT id, name, age FROM public.users ORDER BY id;"
            )
            users = cursor.fetchall()

            print(f"Найдено пользователей: {len(users)}\n")

            for user_id, name, age in users:
                print(f"ID: {user_id}, Имя: {name}, Возраст: {age}")

    except psycopg2.Error as error:
        print(f"Ошибка PostgreSQL: {error}", file=sys.stderr)
        sys.exit(1)

    finally:
        if conn is not None:
            conn.close()
            print("\nСоединение с PostgreSQL закрыто.")


if __name__ == "__main__":
    main()
