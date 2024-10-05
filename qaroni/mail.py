from qaroni.extensions import mail


def send_mail(recipient: str, asunto: str, body: str):
    try:
        mail.send_message(
            asunto, sender="eliezerfot123@gmail.com", recipients=[recipient], body=body
        )
        return "Send email"
    except Exception as e:
        print(e)
        return "Error sending email"
