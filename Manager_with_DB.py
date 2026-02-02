import json
import sqlite3

con = sqlite3.connect("youtube_DB.db")
cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL

            )''')

def list_videos():
    cursor.execute("SELECT * FROM videos")  # THIS GIVES AN TUPLE AS AN OUTPUT
    for row in cursor.fetchall():
        print(row)



def add_video(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?,?)" ,(name, time))
    con.commit()

def update_video(id , new_name , new_time):
    cursor.execute("UPDATE videos SET name = ? ,time = ? WHERE id = ?", (new_name, new_time , id))
    con.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos where id = ?", (video_id,))
    con.commit()


def main():
    while True:
        print("\n Youtube Manager app with DB: ")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit")
        choice = input("Enter you choice: ")

        match choice:
            case '1':
                list_videos()
            case '2':
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                add_video(name, time)
            case '3':
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                video_id = input("Enter the video ID: ")
                update_video(video_id, name , time)
            case '4':
                video_id = input("Enter the video id to be deleted: ")
                delete_video(video_id)
            case '5':
                break
            case _:
                print("Invalid choice")

    con.close()           



if __name__ == "__main__":
    main()
