import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email():
  sender = ... # email pengirim
  password = ... # email password atau 2fa
  receiver = ... # email penerima
  
  # membuat email
  msg = MIMEMultipart()
  msg['From'] = sender
  msg['To'] = receiver
  msg['Subject'] = "automated email using python"
  
  body = """
  Hallo,
  email ini dikirim secara otomatis menggunakan python script.
  """
  
  msg.attach(MIMEText(body, 'plain'))
  
  try:
      print("menghubungakan ke server SMTP...")
      server = smtplib.SMTP("smtp.gmail.com", 587)
      print("memulai enkripsi tls untuk email")
      server.starttls() # enkripsi tls
      print("login ke email")
      server.login(sender, password)
      print("sedang mengirim email")
      server.sendmail(sender, receiver, msg.as_string())
      server.quit()
      print("email berhasil dikirim")
  except Exception as e:
      print(f"Gagal mengirim email : {e}")
      
if __name__ == "__main__":
  send_email()