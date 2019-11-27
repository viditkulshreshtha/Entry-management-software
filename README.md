# Innovacer-Software-Intern

Simple Entry Management Software which keeps the record of the visitors who visit the office

## Installation
Clone this directory.  
`git clone https://github.com/viditkulshreshtha/Innovacer-Software-Intern.git`  

Enter the directory.  
`cd Innovacer-Software-Intern`  

Install pip3 package  
`sudo apt install python-pip3`  

Install the requirements  
`pip3 install -r requirements.txt`  


## Usage  
To check-in for a visitor run `python3 checkin.py`   

To check-out for a visitor run `python3 checkout.py`  

The email is sent to the user by the `smtplib` library of python and sms will be sent to the user by `twilio` library  


NOTE - Make sure that you have python3 installed on the system. Also both the files `checkin.py` and `checkout.py` must be in the **same directory**  


## How it Works  
For checking in, first the host has to enter his details which will be prompted on the terminal. Host details will be saved in a file named `Host_Info` and the client details will be saved in a file named `Client_Info`
Firstly the site manager must create an account and register his mobile number from this [link](https://www.twilio.com/try-twilio).  
![alt text](https://github.com/viditkulshreshtha/Innovacer-Software-Intern/blob/master/Twilio_details.png "Twilio details")

After registration the site manager will get`account_sid` and `auth_token` which he will have to put in `checkin.py`.  

![alt text](https://github.com/viditkulshreshtha/Innovacer-Software-Intern/blob/master/Details.png "")  

The sms and e-mail will be sent to the host during the time of check-in.  

For check-out, run `checkout.py`  and enter the e-mail id of the client to check out. The email will be sent to the client at the time of checkout.  




