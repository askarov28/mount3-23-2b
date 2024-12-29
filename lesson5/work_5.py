
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# smtp_host = "smtp.gmail.com"
# smtp_port = 587
# sender_email = 'askarov228666@gmail.com'
# sender_password = "ahnksxivebahxgde"

# receiver_email = "abdulloahmedov524@gmail.com"
# subject = "22-2B"

# try:
#     while True:
#         message = MIMEMultipart()
#         message['From'] = sender_email
#         message['To'] = receiver_email
#         message['Subject'] = subject

#         body = "Бексултан Салам Алейкум"
#         message.attach(MIMEText(body, 'plain'))

#         server = smtplib.SMTP(smtp_host, smtp_port)
#         server.starttls()
#         server.login(sender_email, sender_password)

#         text = message.as_string()
#         server.sendmail(sender_email, receiver_email, text)
#         print("Успешно отправлена")
# except Exception as e:
#         print("ОШибка", e)
# finally:
#         server.quit()