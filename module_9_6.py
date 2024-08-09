def all_variants(text):
    variants_txt = [text[char_0:char_1] for char_0 in range(len(text)) for char_1 in range(char_0 + 1, len(text) + 1)]
    variants_txt.sort(key=len, reverse=False)
    for i in range(len(variants_txt)):
        yield variants_txt[i]
        i += 1


if __name__ == '__main__':
    varinats_lst_obj = all_variants('abc')
    for line in varinats_lst_obj:
        print(line)
