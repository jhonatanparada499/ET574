email = "jhonatanparada499@gmail.com"

email_address = email[::]
user_name = email[:email.find("@")]
company_name = email[email.find("@") + 1:email.rfind(".")]

print(
f"\
Email address: {email_address}\n\
User name: {user_name.lower()}\n\
Company_name: {company_name.upper()}\
"
)

