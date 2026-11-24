from datetime import datetime
today = datetime.now()
formatted_date = today.strftime("%B %d, %Y")
print(formatted_date)