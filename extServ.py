# Extension Server
# oversees the extensions

void main:
    # some extension asks for primer
    # get the company id from the request
    getPrimer(companyID)
    
    # database needs public key from some user
    # use the ID to go to whichever extension
    sendPublicKey(srcUserID)
    
    # some extension needs a public key from bob. gives bobs id
    getEmployeePublicKey()
    
    # every once in a while you backup
    backup()
    
Extension createExt(User):
    # creates an instance of the extension for each user
    # given a user to bind to the extension

int sendPublicKey(srcUserID):
    # ping the extension with srcUserID
    # prompts ext to call its method to sendPublicKey
    
    return errorCodeIfNoPublicKeyFoundOrUserDoesntExistHolyHeckThisIsALongVariable

# has whatever it takes to run as a server in a client-server relationship
if __name___ == "__main__":
    main()