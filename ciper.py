def main():
    orig_alphabet = input()
    ciper_alhpabet = input()
    orig_message = input()
    ciper_message = input()
    dic_ciper = {}
    dic_unciper = {}
    for i in range(len(orig_alphabet)):
        dic_ciper[orig_alphabet[i]] = ciper_alhpabet[i]

    for i in range(len(ciper_alhpabet)):
        dic_unciper[ciper_alhpabet[i]] = orig_alphabet[i]

    rezult_crypt = ""
    for each in orig_message:
        rezult_crypt += dic_ciper.get(each)

    rezult_encrypt = ""
    for each in ciper_message:
        rezult_encrypt += dic_unciper.get(each)

    print(rezult_crypt)
    print(rezult_encrypt)


# start program
main()