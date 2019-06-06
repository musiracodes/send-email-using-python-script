############################## Email notification ##############################
def send_mail(recipient, subject, message):
    import smtplib
    # for python 3.x
    # from email.mime.multipart import MIMEMultipart
    # for python 2.x change above line to
    from email.MIMEMultipart import MIMEMultipart

    # for python 3.x
    # from email.mime.text import MIMEText
    # for python 2.x change above line to
    from email.MIMEText import MIMEText

    username = "sender_email@email.com"
    password = "sender_password"
    cc = ""  # add the number of cc emails required separated by a comma inside the quotation marks
    rcpt = cc.split(",") + [recipient]

    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = recipient
    msg['Cc'] = cc
    msg['Subject'] = subject
    msg.attach(MIMEText(message))

    try:
        print('\nThe process was successful, sending notification mail to ' +
              recipient + ' on ' + subject + '\n')

        mailServer = smtplib.SMTP('smtp-mail.outlook.com', 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(username, password)
        mailServer.sendmail(username, rcpt, msg.as_string())
        mailServer.close()

    except Exception as e:
        print(str(e))


send_mail('youremail@outlook.com', 'Your subject', 'Your message body')
