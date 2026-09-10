
import sqlite3
import getpass


conn=sqlite3.connect("taskmanager.db")
cursor = conn.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS user(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,   
                    username VARCHAR UNIQUE,
                    password TEXT
                    )
                    """)

cursor.execute("""CREATE TABLE IF NOT EXISTS Tasks(
                    id  INTEGER PRIMARY KEY AUTOINCREMENT,
                    task_name VARCHAR(20),
                    task_des TEXT,
                    u_id INTEGER,
                    FOREIGN KEY (u_id) REFERENCES user(id)
             )""")

conn.close()

def adduser():
    conn=sqlite3.connect("taskmanager.db")
    cursor=conn.cursor()
    uname=input("enter the user name: ")
    pas=("enter the password: ")
    cursor.execute("""
                INSERT INTO user(username,password)
                VALUES (?,?)""",(uname,pas)
                )
    conn.commit()
    print("user registered")

def addtask(user_id):
    conn=sqlite3.connect("taskmanager.db")
    cursor=conn.cursor()
    tname=input("enter task name:- ")
    tdes=input("enterthe task des:- ")

    cursor.execute("""
                INSERT INTO Tasks(task_name,task_des,u_id)
                VALUES (?,?,?)""",(tname,tdes,user_id))
    conn.commit()

def findtask(user_id):
    conn = sqlite3.connect("taskmanager.db")
    cursor=conn.cursor()
    t_id=int(input("enter the task_id: "))
    cursor.execute('''  SELECT * FROM tasks WHERE id = ? AND u_id = ? ''',(t_id,user_id))   #if ther is only one value in parameter then put one comma after that
    task=cursor.fetchone()                                              #tofetch onlypne field of data
    print(task)
    if task:
        print("taskfound")
        print(f"task_name:-{task[1]} \n description:-{task[2]}")
    else:
        print("task not found !....")

def update(user_id):
    conn=sqlite3.connect("taskmanager.db")
    cursor=conn.cursor()
    t_id=int(input("enter the task_id: "))
    tname=input("enter task name:- ")
    tdes=input("enterthe task des:- ")
    cursor.execute('''UPDATE Tasks SET task_name = ?,task_des = ? WHERE id = ? AND u_id = ?''',(tname,tdes,t_id,user_id))
    conn.commit()
    print("task updated........")    


def delete(user_id):
    conn=sqlite3.connect("taskmanager.db")
    cursor=conn.cursor()
    t_id=int(input("enter the task_id: "))
    ch=input(f"are you sure you want to delete task\nY/N:- \t").lower()
    if ch =="y":
        cursor.execute('''DELETE FROM Tasks WHERE id = ? AND u_id = ?''',(t_id,user_id))
        conn.commit()
        print("task deleted..........")
    else:
        print("task not deleted!...")
    
def view_task(user_id):
    conn=sqlite3.connect("taskmanager.db")
    cursor=conn.cursor()
    cursor.execute("""SELECT * FROM Tasks WHERE u_id = ?""",(user_id,))
    task=cursor.fetchall()           #retrives a list of data from last executed query 
    if task:
        print("tasks founded.....\n")
        for i in task:
            print(i[1])
    else:
        print("no current tasks!!!!")


def login():
    conn=sqlite3.connect("taskmanager.db")
    cursor=conn.cursor()
    uname=input("enter user name:- ")
    pas=getpass.getpass("enter the password: ",echo_char='*')
    cursor.execute(""" SELECT id FROM user WHERE username=? AND password=?""",(uname,pas))
    user = cursor.fetchone()
    if user:
        print("logged in successfully")
        return user[0]
    else:
        print("incorrect username or password!..try again")
        


def dash():
    print(".................Welcome.................!!!")
    while True:
        print('-'*60)
        ch = int(input("please select an option :\n1.Register\n2.Login :-"))
        if ch == 1:
            adduser()
        elif ch == 2:
            user_id = login() 
            if user_id:
                main1(user_id)

        elif ch == 3:
            break
        else:
            print("invalid option !...")
    

def main1(user_id):
    print("Welcome to task management system..\n")
    while True:
        print('-'*120)
        print("choose your options")
        ch=int(input("1.Add Task\n2.View task\n3.find task\n4.update task\n5.delete task\n6.logout\n"))
        if ch==1:
            addtask(user_id)
        elif ch==2:
            view_task(user_id)
        elif ch ==3:
            findtask(user_id)
        elif ch ==4:
            update(user_id)
        elif ch == 5:
            delete(user_id)
        elif ch==6:
            break
        else:
            print("invalid input!...")


dash()