# Copy text from 

#! python3

import re
import pyperclip

# Create a regex object for phone numbers
phoneRegex = re.compile(r'''

# 337-555-0000, 555-0000, (337) 555-0000, 555-0000 ext 12345, ext. 12345, x12345

()
((\d\d\d) | (\(\d\d\d)))?        # area code (optional)
(\s|-)                           # first separator
\d\d\d                           # first 3 digits
-                                # separator
\d\d\d\d                         # last 4 digits
(((ext(\.)?\s) | x)              # extension
 (\d{2.5}))?
 )

'''. re.VERBOSE)

# ToDo: Create a regex object for email addresses
emailRegex = re.compile(r'''

[a-zA-Z0-9_.+]+       # Name
@                    # @ Symbol
[a-zA-Z0-9_.+]+       # Domain

''', re.VERBOSE)

# ToDo: Get the text off the clipboard
text = pyperclip.paste()


# ToDo: Extract the email/phone from the text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

print (extractedPhone)
print (extractedEmail)


# ToDo: Copy the extracted email/phone to the clipboard

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)