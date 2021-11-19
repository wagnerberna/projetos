# https://www.youtube.com/watch?v=JohZzRRGVAM
def sort(string):
    lista = [el for el in string]
    # print(lista)

    for percorrido in range(1, len(lista)):
        # print(f"percorrido:{percorrido}")
        for posicao in range(len(lista) - percorrido):
            # print(f"Posição:{posicao}")
            # print(f"if:{lista[posicao]}, {lista[posicao + 1]}")
            if lista[posicao] > lista[posicao + 1]:
                temp = lista[posicao]
                # print(f"temp: {temp}")
                lista[posicao] = lista[posicao + 1]
                lista[posicao + 1] = temp
                # print(
                #     f"inversão pos: {lista[posicao]}, {lista[posicao + 1]}"
                # )
    # print(lista)
    string_sort = "".join(lista)
    return string_sort


# print(sort("roma"))


def is_anagram(first_string, second_string):
    if len(first_string) == "" or len(second_string) == "":
        return False
    if len(first_string) != len(second_string):
        return False
    first = sort(first_string)
    second = sort(second_string)
    # print(first, second)
    if first == second:
        return True
    else:
        return False


# print(is_anagram("roma", "amor"))
