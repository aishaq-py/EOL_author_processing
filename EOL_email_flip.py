
email = input("Email: ")
email = email.lower()
email = email.replace(" ",".")
# =============================================================================
# email = email.replace(".[at].","@")
# email = email.replace("[at]","@")
# =============================================================================

#landrumAThcpDOTmedDOTharvardDOTedu

at_modifiers = ["*",".[at]."," [at] ","[at]",".(at)."," (at) ","(at)"]
for i in at_modifiers:
    if i in str(email):
        email.replace(i,"@")
        print(i)
        

print(email)
keywords = [".de",".org", ".com", ".edu",".co",".ac",".ku",".163"]


for words in keywords:
    if words not in email:
        email = email [::-1]
        break
    else:
        pass

print(email)

asdasd = "giuliana|locascio*azosp|vr|it <== Replace | with . and * with @ to have the right email address."