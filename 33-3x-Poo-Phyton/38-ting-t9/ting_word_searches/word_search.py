# P/ Teste local
# try:
#     import sys
#     import os

#     sys.path.append(
#         os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
#     )
# except ImportError:
#     raise
# from ting_file_management.file_process import process
# from ting_file_management.queue import Queue

# FIM_TESTE


def exists_word(word, instance):
    filter_word = []
    data = instance.search(0)
    line_check = list(data["linhas_do_arquivo"])
    print("!!!TESTE P1!!!")
    print(word)
    print(data)
    print(line_check)

    filter_word = list(filter(lambda el: word in el, line_check))
    print(filter_word)
    if len(filter_word) == 0:
        return []
    return filter_word


def search_by_word(word, instance):
    """Aqui irá sua implementação"""


# project = Queue()
# process("statics/nome_pedro.txt", project)
# print(word = exists_word("Ratinho", project))
