def is_email_valid(email):
    return "@" in email and email.endswith((".com", ".ru", ".net"))


def send_email(message, recipient, *, sender="university.help@gmail.com"):
    for email in [recipient, sender]:
        if not is_email_valid(email):
            print(
                f"It is impossible to send a letter from the address {sender} to the address {recipient}"
            )
            return

    if sender == recipient:
        print("You can't send a letter to yourself!")
    elif sender == "university.help@gmail.com":
        print(
            f"The letter was successfully sent from the address {sender} to the address {recipient}."
        )
    else:
        print(
            f"NON-STANDARD SENDER! The letter was sent from the address {sender} to the address {recipient}"
        )


send_email("This message is for checking the connection", "vasyok1337@gmail.com")
send_email(
    "You see this message as the best student of the course!",
    "urban.fan@mail.ru",
    sender="urban.info@gmail.com",
)
send_email(
    "Please correct the task", "urban.student@mail.ru", sender="urban.teacher@mail.uk"
)
send_email(
    "I remind myself of the webinar",
    "urban.teacher@mail.ru",
    sender="urban.teacher@mail.ru",
)
