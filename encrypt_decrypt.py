def encrypt_decrypt():
    choice=int(input("Type 1 for encyption and 2 for decryption: "))
    text=input("enter message: ")
    shift=int(input("enter the shift value: "))
    #for encryption 
    if choice==1:
        for i in text:       
            i=ord(i)                             #covert characters to ASCII values
            i+=shift
            i=chr(i)                             #covert ASCII values back to characters
            print(i,end="")
    #for decryption
    elif choice==2:
        for i in text:
            i=ord(i)                             #covert characters to ASCII values
            i-=shift
            i=chr(i)                             #covert ASCII values back to characters
            print(i,end="")
    else:
        print("enter valid choice.")
        print("Thankyou.") 
encrypt_decrypt()
