from celery import task 
from celery import shared_task 
# We can have either registered task 
from .models import UserProfile
from datetime import datetime, timezone
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
from reportlab.pdfgen import canvas 
import os

@shared_task 
def send_notifiction():
  qs = UserProfile.objects.all()
  for obj in qs:
    diff = datetime.now(timezone.utc) - obj.last_activity
    duration_in_s = diff.total_seconds() 
    minutes = divmod(duration_in_s, 60)[0]
    print(minutes)
    if minutes>=5 and obj.email_sent==False:
      try:
        generate_pdf.delay(obj.email, obj.questions)
        obj.email_sent = True
        obj.save()
      except Exception as e:
        raise e


@shared_task 
def send_email(email, file_name):
  try:
    print("sending email")
    recipients = [email] 
    emaillist = [elem.strip().split(',') for elem in recipients]
    msg = MIMEMultipart()
    msg['Subject'] = "Similar questions pdf link from doubtnut"
    msg['From'] = 'utreja.akash@gmail.com'

    html = """\
    <html>
      <head></head>
      <body>
      <p>Go to this file URL</p>
        {0}
      </body>
    </html>
    """.format("{}".format(file_name))

    part1 = MIMEText(html, 'html')
    msg.attach(part1)
    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()

    mail.starttls()
    mail.login('greyskyler1996@gmail.com', 'raprmjsixwqkrfqw')
    mail.sendmail(msg['From'], emaillist, msg.as_string())
    mail.quit()
    print("email sent")
  except Exception as e:
    raise e



@shared_task
def generate_pdf(email, data):
  try:
    current_epoch_time = int(datetime.now().strftime("%s"))
    dirname = os.path.dirname(__file__)
    file_name = os.path.join(dirname, 'temp/{}.pdf'.format(current_epoch_time))
    pdf = canvas.Canvas(file_name)    
    pdf.setTitle(file_name)
    pdf.drawCentredString(290,720, "Questions List")
    text = pdf.beginText(40, 680)
    text.setFont("Courier", 12)
    for index,value in enumerate(data):
        text.textLine("{}. {}".format(index+1,value))
    pdf.drawText(text)
    pdf.save()
    print("pdf generated")
    send_email.delay(email, file_name)
  except Exception as e:
    raise e