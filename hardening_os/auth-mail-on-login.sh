#!/bin/bash

#Author: Aditya Naga Sanjeev, Yellapu
#Date: 28 Jan 2018

#Description: Script to send e-mail on each login. 
#Last Updated: 28 Jan 2018
#version=0.1




if [ "$PAM_TYPE" != "close_session" ]; then
    host="`hostname`"
    if [ $PAM_RHOST == "" ]; then
	$PAM_RHOST=$host
    fi
   
    subject="Login: $PAM_USER from $PAM_RHOST on $host"

    # PAM environment variables have different values, need to double check and remove the following and replace them directly with os.environ in python below.
    export user="$(echo $USER)$PAM_USER"
    export pwd=$(echo $PWD)
    export term=$(echo $TERM)
    export ssh_tty="$(echo $SSH_TTY)$PAM_TTY"
    export logname=$(echo $LOGNAME)
    export date=$(date)

export host
export subject
export message

python - <<EOF

import os
import smtplib

server = smtplib.SMTP('mail.jpberlin.de', 587)
#server.connect("mail.jpberlin.de", 587)

server.ehlo()
server.starttls()
server.ehlo()

#log in to the server
server.login("secure-monitor@theDomain.com", "@56aFS%T9$7axV#L")
subject = os.environ['subject']
_date = os.environ['date']
user = os.environ['user']
pwd = os.environ['pwd']
term = os.environ['term']
ssh_tty = os.environ['ssh_tty']
logname = os.environ['logname']

msg = 'DATE:{}\nUSER:{}\nPWD:{}\nTERM:{}\nSSH_TTY:{}\nLOGNAME:{}\n'.format(_date,user,pwd,term,ssh_tty,logname)

message = 'Subject: {}\n\n{}'.format(subject, msg)


#Send the mail
server.sendmail("secure-monitor@theDomain.com", "system.admins@theDomain.com", message)
server.quit()
EOF
fi
