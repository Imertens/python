def new_password(oldpassword,newpassword):
    if oldpassword != newpassword and len(newpassword) > 6:
        print('true')
    else:
        print('Je nieuwe wachtwoord is hetzelfde als je oude wachtwoord of hij is niet langer dan 6 tekens')

oldpassword = input('Wat is je oude wachtwoord? :')
newpassword = input('Wat is je nieuwe wachtwoord? :')

new_password(oldpassword,newpassword)
