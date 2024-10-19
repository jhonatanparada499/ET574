email = "jhonatanparada499@gmail.com"

email_address = email[:]
user_name = email[:email.index("@")]
company_name = email[email.index("@") + 1:email.rindex(".")]

print(
  f"Email address: {email_address}",
  f"User name: {user_name.lower()}",
  f"Company_name: {company_name.upper()}",
  sep='\n'
)

