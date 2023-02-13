def main():
    print("Welcome to the email slicer") 
    print("")

    email_input = input("Input your email address")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print(f"Your username is {username} & domain is {domain} and extension is {extension}")

    #print("username : ", username)
    #print("Domain : ", domain)
    #print("Extension: " , extension)

while True:    
    main()