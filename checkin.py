"""entry management software
user enters the details as prompted in the terminal
and sends the information to the host.
host enters emailId of client and recieves
information regarding his visit."""

import smtplib
from twilio.rest import Client
import time
from time import gmtime, strftime
import re


class SiteManager:
    def manager_info(self):
        address = "your_address_here"
        account_sid = 'your_sid_here'
        auth_token = 'your_token_here'
        twilio_contact = 'your_contact_here'
        login_id = "email"
        login_password = "password"
        return address,account_sid,auth_token,twilio_contact,login_id,login_password



def store_host_info(host_name, host_phone, host_email):
    file = open(r"Host_Info","a")
    for L in [host_name, " ", host_email, " ", host_phone]:
        file.writelines(L)
    file.writelines("\n")
    file.close()
    client_details(host_name)


def host_info():
    print("Enter host name:", end = " ")
    host_name = input()

    print("Enter host phone number:", end = " ")
    host_phone = input()

    print("Enter host email-id:", end = " ")
    host_email = input()

    print("Host details saved.")
    store_host_info(host_name,host_phone,host_email)

#function to strore the client info into a file

def store_client_info(client_name, client_email, client_phone, checkin_time, host_name):
    client_file = open(r"Client_Info","a")
    for L in [client_name, " ", client_email, " ", client_phone, " ", checkin_time, " ",host_name]:
        client_file.writelines(L)
    client_file.writelines("\n")
    client_file.close()

    message = "\nName: " + client_name + "\n" "Email: " + client_email + "\n" + "Phone: " + client_phone + "\n" + "Check-in Time: " + checkin_time
    
    email_to_host(message,host_name)

#checks for a valid name
def is_valid_name(client_name):
    valid_name = re.compile(r"[A-Za-z]( [A-Za-z])?")
    return valid_name.match(client_name)

#checks for valid phone number
def is_valid_number(client_phone):
    valid_phone = re.compile(r"[0-9]{10}")
    return valid_phone.match(client_phone)

#checks for a valid email
def is_valid_email(client_email):
    valid_email = re.compile(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$')
    return re.search(valid_email,client_email)


def client_details(host_name):
    try:
        print("Enter Client name:",end=" ")
        client_name = input()
        is_valid_name(client_name)
    except:
        print("Please enter a valid name")
        print("Name:",end=" ")
        client_name = input()
    
    try:
        print("Enter Client email:",end=" ")
        client_email = input()
        is_valid_email(client_email)
    except:
        print("Please enter a valid email")
        print("Enter Client email:",end=" ")
        client_email = input()

    try:
        print("Enter Client Phone:",end=" ")
        client_phone = input()
        is_valid_number(client_phone)
    except:
        print("Please enter a valid number")
        print("Enter Client phone:",end=" ")
        client_phone = input()

    

    checkin_time = strftime("%Y-%m-%d/%H:%M:%S", time.localtime())
    
    store_client_info(client_name, client_email, client_phone, checkin_time,host_name)


# sending message to host
def sms_to_host(message, account_sid, auth_token, twilio_contact, host_phone):

    client = Client(account_sid, auth_token) 
    message = client.messages.create( 
                              from_= twilio_contact, 
                              body = message, 
                              to = host_phone
                          )


#sending email to host
def email_to_host(body_text,host_name):

    site_manager_obj = SiteManager()

    address, account_sid, auth_token, twilio_contact, login_id, login_password = site_manager_obj.manager_info()

    host_phone = ""
    host_email = ""
    file = open(r"Host_Info", "r")
    for entry in file.readlines():
        entry = entry.split()
        if entry[0] == host_name:
            host_phone = entry[2]
            host_email = entry[1]

    subject = "Client visit at " + address + "."
    message = 'Subject: {}\n\n{}'.format(subject, body_text)
    try:    
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(login_id, login_password)
    except:
        print("Enter valid credentials")
    
    try:
        s.sendmail(login_id, host_email, message)
        print("Client Check-in Successful")
    except:
        print("Check-in Failed!")
    s.quit()
    
    sms_to_host(message, account_sid, auth_token, twilio_contact, host_phone)

#function to store the client info
def store_client_info(client_name, client_email, client_phone, checkin_time,  host_name):
    file = open(r"Client_Info","a")
    for L in [client_name, " ", client_email, " ", client_phone, " ", checkin_time, " ", host_name]:
        file.writelines(L)
    file.writelines("\n")
    file.close()

    message = "\nName: " + client_name + "\n" "Email: " + client_email + "\n" + "Phone: " + client_phone + "\n" + "Check-in Time: " + checkin_time
    
    email_to_host(message,host_name)

if __name__ == "__main__":
    host_info()