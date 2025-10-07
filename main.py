from imapclient import IMAPClient
import os
from dotenv import load_dotenv

def main() -> None:
    
    load_dotenv()
    secrit_password = os.getenv("PASSWORD") 
    
    
    server:str = "imap.gmail.com"
    email:str = "imkerjasper@gmail.com"
    password:str = secrit_password #type:ignore

    with IMAPClient(server, ssl=True) as client:
        client.login(email, password)
        client.select_folder("INBOX")
        messages = client.search("ALL")
        print(f"Aantal mails in inbox: {len(messages)}")

if __name__ == "__main__":
    main()