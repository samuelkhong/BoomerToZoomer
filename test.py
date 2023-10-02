import os

key = os.environ.get("openai_key")

if key:
    print(f"The value of openai_key is: {key}")
else:
    print("The environmental variable openai_key does not exist.")
