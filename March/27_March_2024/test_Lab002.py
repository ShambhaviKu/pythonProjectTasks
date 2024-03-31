from dotenv import load_dotenv
import os

def test_user_CRED():
    load_dotenv()
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    print(username)
    print(password)


