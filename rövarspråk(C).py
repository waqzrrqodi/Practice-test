konsonanter = ["b","c","d","f","g","h","i","j","k","l","m","n","p","q","r","s","t","v","w","x","z","å""B","C","D","F","G","H","I","J","K","L","M","N","P","Q","R","S","T","V","W","X","Z","Å"]

def rovar_sprak(str):
    len_str = len(str) - 1
    i = 0
    new_word = ""
    while i < len_str:
        if str[i] in konsonanter:
            new_word = new_word + str[i] + "o" + str[i]
        else:
            new_word = new_word + str[i]
        i += 1
    return new_word



print(rovar_sprak("Kaka kaka!"))
