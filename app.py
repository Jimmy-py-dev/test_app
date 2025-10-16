from dotenv import load_dotenv
import os 

load_dotenv(".env.test")

first = os.getenv("test")
print ("i removed as a branch")
print (first)