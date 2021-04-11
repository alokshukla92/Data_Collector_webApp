
import sqlite3
from email.mime.text import MIMEText
import smtplib

def connect():
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM data")
    rows=cur.fetchall()
    conn.close()
    return rows

def insert(email, height):
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO data VALUES (NULL,?,?)",(email, height))
    conn.commit()
    conn.close()

def email():
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("SELECT email FROM data")
    rows = cur.fetchall()
    conn.close()
    return rows


#email1 = 'alokshukla994@gmail.com'
connect()
print(type(email()))
print(email())
def email_exists(email1):
    for i in email():
        if email1 in list(i):
            print("True")
    print("false")
email_exists('alokshukla994@gmail.com')
# if email1 in l1:
#     print("True")
# else:
#     print("False")

def height_average():
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("SELECT AVG(height) FROM data")
    rows = cur.fetchall()
    conn.close()
    return rows[0][0]


def send_email(email, height):
    avg_height = height_average()
    from_email = "YourEmail_address"
    from_password = "yourPassword"
    to_email = email

    subject = "Height Data"
    message = "Hey there,The height entered by you is <strong> %s </strong>... The average height entered by all users is <strong> %s </strong>. "% (str(height), str(avg_height))

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)






def delete():
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM data")
    conn.commit()
    conn.close()

#delete()
print(view())
print(type(height_average()))
