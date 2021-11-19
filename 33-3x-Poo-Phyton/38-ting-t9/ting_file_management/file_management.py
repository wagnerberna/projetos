import sys

# import os.path

# https://www.delftstack.com/pt/howto/python/python-print-to-stderr/
# https://pt.stackoverflow.com/questions/2823/como-checar-se-um-arquivo-existe-usando-python


# def check_file(path_file):
#     if not path_file.endswith("txt"):
#         return sys.stderr.write("Formato inválido\n")
#     is_file = os.path.isfile(path_file)
#     print(is_file)
#     if not is_file:
#         return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
#     return True


def txt_importer(path_file):
    # check_file(path_file)
    if not path_file.endswith("txt"):
        return sys.stderr.write("Formato inválido\n")
    try:
        with open(path_file, mode="r") as file:
            txt = file.read().split("\n")
        return txt
    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")


if __name__ == "__main__":
    print(txt_importer("statics/arquivo_teste.txt"))
    print(txt_importer("statics/arquivo_teste.csv"))
    print(txt_importer("statics/arquivo_testeeee.txt"))
