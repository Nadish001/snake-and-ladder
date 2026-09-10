
import sqlite3

conn=sqlite3.connect("mytasks.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Tasks(
                    id  INTEGER PRIMARY KEY AUTOINCREMENT,
                    task_name VARCHAR(20),
                    task_des TEXT
             )""")


conn.close()


def addtask():
    conn=sqlite3.connect("mytasks.db")
    cursor=conn.cursor()
    tname=input("enter task name:- ")
    tdes=input("enterthe task des:- ")

    cursor.execute("""
                INSERT INTO Tasks(task_name,task_des)
                VALUES (?,?)""",(tname,tdes))
    conn.commit()

def findtask():
    conn = sqlite3.connect("mytasks.db")
    cursor=conn.cursor()
    t_id=int(input("enter the task_id: "))
    cursor.execute('''  SELECT * FROM tasks WHERE id = ? ''',(t_id,))   #if ther is only one value in parameter then put one comma after that
    task=cursor.fetchone()                                              #tofetch onlypne field of data

    print(task)
    if task:
        print("taskfound")
        print(f"task-{task[1]} des-{task[2]}")
    else:
        print("task not found")

def update():
    conn=sqlite3.connect("mytasks.db")
    cursor=conn.cursor()
    t_id=int(input("enter the task_id: "))
    tname=input("enter task name:- ")
    tdes=input("enterthe task des:- ")
    cursor.execute('''UPDATE Tasks SET task_name = ?,task_des = ? WHERE id = ?''',(tname,tdes,t_id))
    conn.commit()
    print("task updated........")    
def delete():
    conn=sqlite3.connect("mytasks.db")
    cursor=conn.cursor()
    t_id=int(input("enter the task_id: "))
    ch=input(f"are you sure you want to delete task\nY/N").lower()
    if ch =="y":
        cursor.execute('''DELETE FROM Tasks WHERE id = ?''',(t_id,))
        conn.commit()
        print("task deleted..........")
    else:
        print("task not deleted")
    
def view_task():
    conn=sqlite3.connect("mytasks.db")
    cursor=conn.cursor()
    cursor.execute("""SELECT * FROM Tasks""")
    task=cursor.fetchall()           #retrives a list of data from last executed query 
    if task:
        print("tasks found\n")
        for i in task:
            print(i[1])
    else:
        print("no current tasks")

def main():
    print("Welcome to task management system..\n")
    while True:
        print("choose your options")
        ch=int(input("1.Add Task\n2.View task\n3.find task\n4.update task\n5.delete task\n6.exit\n"))
        if ch==1:
            addtask()
        elif ch==2:
            view_task()
        elif ch ==3:
            findtask()
        elif ch ==4:
            update()
        elif ch == 5:
            delete()
        elif ch==6:
            break
        else:
            print("invalid input")


main()