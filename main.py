PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt") as guest:
    guest_list = guest.readlines()
    print(guest_list)

with open("Input/Letters/starting_letter.txt", "r") as file:
    letter = file.read()
    for name in guest_list:
        stripped_name = name.strip()
        invitation = letter.replace(PLACEHOLDER,stripped_name)
        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode= "w") as completed_invitation:
            completed_invitation.write(invitation)