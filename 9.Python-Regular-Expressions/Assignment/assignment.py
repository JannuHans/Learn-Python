#1. Extract Email Addresses

import re

# text = "Contact us at support@test.com or admin123@gmail.com"
# pattern = r'[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+'

# ans = re.findall(pattern,text)
# print(ans)

#2. Validate Password

# password = "Jannumm134"

# pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

# if re.match(pattern, password):
#     print("Valid Password")
# else:
#     print("Invalid Password")


#3. Extract Dates

# text = "
# Meeting on 12-05-2026 and another on 2026-06-01
# "

# pattern = r'\b(?:\d{2}[-/]\d{2}[-/]\d{4}|\d{4}-\d{2}-\d{2})\b'

# dates = re.findall(pattern, text)

# print(dates)

# 4. Find Duplicate Words

# text = "This is Is a Sample sample text"

# pattern = r'\b(\w+)\s+\1\b'

# duplicates = re.findall(pattern, text, re.IGNORECASE)

# print(duplicates)

# #55. Convert Multiple Spaces to One

# text = "   Hello     World\t\tPython   "

# result = re.sub(r'\s+', ' ', text).strip()

# print(result)

#6. Log File Parser

# logs = """
# 2026-06-01 10:23:45 ERROR Database connection failed
# 2026-06-01 10:24:12 INFO User login successful
# """

# pattern = r'(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\s+(\w+)\s+(.*)'

# matches = re.findall(pattern, logs)

# result = [
#     {
#         "timestamp": ts,
#         "log_level": level,
#         "message": msg
#     }
#     for ts, level, msg in matches
# ]

# print(result)

#7. Extract HTML Tags

# html = """
# <div>Hello</div>
# <p>World</p>
# <a href="#">Link</a>Give feedback
# """

# pattern = r'<(\w+)\b[^>]*>'

# tags = re.findall(pattern, html)

# print(tags)

#8 Extract Currency Values


# text = "Revenue was $1,200.50, profit ₹50,000 and loss €300"

# pattern = r'[$₹€]\d[\d,]*(?:\.\d+)?'

# currencies = re.findall(pattern, text)

# print(currencies)