import emails

def sendMail(email, name):
    
    html_text = '''<p><strong><span style='font-family: "Trebuchet MS", Helvetica, sans-serif; background-color: rgb(239, 239, 239);'>Hello Dear,</span></strong></p>
    <p><span style="background-color: rgb(239, 239, 239);"><span style="font-family: 'Trebuchet MS', Helvetica, sans-serif;"><strong>This is my first mail through python script.</strong></span></span></p>
    <p><span style="background-color: rgb(239, 239, 239);"><span style="font-family: 'Trebuchet MS', Helvetica, sans-serif;"><strong>I am learning new stuff from LetsUpgrade.</strong></span></span></p>
    <p><span style="background-color: rgb(239, 239, 239);"><strong><span style='font-family: "Trebuchet MS", Helvetica, sans-serif;'>You can also come and join me.</span></strong></span></p>
    <p><span style="background-color: rgb(239, 239, 239); color: rgb(251, 160, 38);"><br></span></p>
    <p><span style="background-color: rgb(239, 239, 239);"><span style="font-family: Impact, Charcoal, sans-serif;">Regards</span></span></p>
    <p><span style="background-color: rgb(239, 239, 239);"><span style="font-family: Impact, Charcoal, sans-serif;">Ayush Kumar</span></span></p>
    <p><br></p>'''
    
    subject = "Hey dear "+ name + ", you have EMAIL From Ayush"
    
    message = emails.html(html=html_text,
                          subject=subject,
                          mail_from=('Ayush Kumar', 'ayushkumar.cse.srmu@gmail.com'))

    
    mail_via_python = message.send(to=email, 
                               smtp={'host': 'smtp.gmail.com', 
                                     'timeout': 5,
                                    'port':587,
                                    'user':'YOUREMAIL@REQUIRED>COM',
                                    'password':'YourPassWordREquired',
                                    'tls':True})
    return mail_via_python.status_code

if __name__ == "__main__":
    name= input("Enter Receiver's Name:\n")
    email= input("Enter Receiver's Email:\n")
    print(sendMail(email,name))

