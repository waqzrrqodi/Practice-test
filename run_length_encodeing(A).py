def rle(text):
    len_str = int(len(text) - 1)
    compressed_str = ""
    i = 0
    while i <= len_str:
        count = 1
        ch = text[i]
        how_many = i
        while how_many < len_str:
            if text[how_many] == text[how_many + 1]:
                count = count + 1
                how_many = how_many + 1
            else:
                break
        
        if count > 1:
            compressed_str = compressed_str + str(count) + ch
        else:
            compressed_str = compressed_str + ch
        i = how_many + 1
    return compressed_str

print(rle("AAABBBDD"))