import random
from email.message import EmailMessage
import smtplib
import ssl


subject1 = 'Free Web Design Offer'
subject2 = 'Your FREE Website'

body = '''Hello - I saw your services on Yellow Pages and wanted to see if you had any problems running your business.\n\nI help decrease operating expenses and alleviate heavy workloads by automating existing workflows without having to change the way you do business.\n\n\nHere are some example use cases that can be implemented in your business:\n\n - [Problem 1] You collect orders through google forms, manually input the information into an invoice document, and then email it.\n - [Solution 1] I would create a Google AppScript function that automatically converts the form response into an invoice templated document and emails it to the customer after they submit the form.\n\n - [Problem 2] You run a plumbing business where you manually have to give different quotes to customers depending on their needs.\n - [Solution 2] I would build out a dynamic contact form that takes in a variety of answers from the customer and once they submit the form, they'll be given an accurate quotation (or a rough estimate) of what their project will cost.\n\n - [Problem 3] You want to sell something to real estate agents so you go to a site like realtor . com and manually type the data you find into a spreadsheet.\n - [Solution 3] I would create a script that automatically goes to this website and extract the information you need at a faster and more scalable pace.\n\n - [Problem 4] You run an eBay store where you spend 2 hours a day posting/deleting products and making sure everything matches your company website.\n - [Solution 4] I would create a central database that compiles the product information and would make a bot that posts and deletes products as needed.\n\n - [Problem 5] You have a pizza truck that uses a POS containing various customer data and you need help identifying the locations that made you the most money and on which days.\n - [Solution 5] I would build a script that takes the exported data from your POS and input it into a simple database like Google Sheets and use that to create a dashboard that presents an analytical visualization of trends among your customers and their buying patterns.\n\n\nHopefully, this gives you an idea of the type of tasks that can be accomplished while minimizing your operational costs and time spent doing these manually.\n\nIf you're interested in this or have an idea of how I can help, I'd like to hop on a quick call to better understand your business needs and see what solutions we could implement.\n\nI look forward to your response.\n\nBest,\nDavid Sanusi'''
body2 = '''Hello - I saw your services on Yellow Pages and wanted to see if you needed help automating reptetitve, costly, and time consuming tasks.\n\nI help decrease operating expenses and alleviate heavy workloads by automating existing workflows without having to change the way you do business. \n\nIf you're interested in this or have an idea of how I can help, I'd like to hop on a quick call to better understand your business needs and see what solutions we could implement.\n\nI look forward to your response.\n\nBest,\nDavid Sanusi'''
subjects = [subject1, subject2]
bodies = [body]
print(body2)

# subject = random.choice(subjects)
#
#
# email_sender = "kayusidigital@gmail.com"
# email_password = "rwmkhokhhkgdtrby"
# email_receiver = 'davidksanusi@gmail.com'
#
# em = EmailMessage()
# em['From'] = email_sender
# em['To'] = email_receiver
# em['Subject'] = subject
# em.set_content(body)
#
# context = ssl.create_default_context()
#
# with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
#     smtp.login(email_sender, email_password)
#     smtp.sendmail(email_sender, email_receiver, em.as_string())
#     print("Email sent.")
