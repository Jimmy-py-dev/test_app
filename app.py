from dotenv import load_dotenv
import os 

load_dotenv(".env.test")

first = os.getenv("test")
print ("neww")
print (first)