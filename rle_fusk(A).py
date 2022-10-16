def rle(text):
    len_str = int(len(text) - 1)
    compressed_str = ""
    i = 0
    while (i <= len_str):
        count = 1
        ch = text[i]
        j = i
        
        while (j < len_str):
            if (text[j] == text[j + 1]):
                count = count + 1
                j = j + 1
            else:
                break
        if (count > 1):
            compressed_str = compressed_str + str(count) + ch
        else:
            compressed_str = compressed_str + ch
        i = j + 1
    return compressed_str

print(rle("AAABBDDDCDD"))