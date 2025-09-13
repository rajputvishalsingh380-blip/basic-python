import smtplib as s
ob = s.SMTP("smtp.gmail.com",587)
ob.ehlo()
ob.starttls()
ob.login("rajputvishalsingh380@gmail.com","mmqs gsgz aoxo ynzm")  #sendar email, app password

subject=" sample testing"
body ="this is a python code files for sending emails"
message="subject:{}\n\n{}".format(subject,body)
address=["vishalsinghrajput861@gmail.com","surendarsinghrajput047@gmail.com"]
ob.sendmail(" rajputvishalsingh380@gmail.com",address,message)
print("sent email successfully")
ob.quit()