from fastapi import FastAPI
from pydantic import BaseModel
import smtplib
from jinja2 import Environment, FileSystemLoader, select_autoescape
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from schemas.user import UserCreate

class MailService:
    
    def send_password_by_email(self,user: UserCreate):
        reset_token = "FakeToken"
        
        # Cargar el template HTML
        env = Environment(
            loader=FileSystemLoader("templates"),
            autoescape=select_autoescape(["html", "xml"]),
        )
        template = env.get_template("password_reset_email_template.html")

        # Renderizar el template con los datos necesarios
        email_content = template.render(
            reset_link=f"http://example.com/reset?token={reset_token}"
        )
        
        sender_email = "pprobado80@gmail.com"
        sender_password = "czzu eodb dspn vawb"
        # Crear el mensaje
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = user.email
        message["Subject"] = "Password Reset Request"
        message.attach(MIMEText(email_content, "html"))

        # Conectar al servidor SMTP de Gmail
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, user.email, message.as_string())
            return True