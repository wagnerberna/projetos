from ting_file_management.file_management import txt_importer
import sys

# P/ Teste local
# try:
#     import sys
#     import os

#     sys.path.append(
#         os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
#     )
# except ImportError:
#     raise
# from ting_file_management.file_management import txt_importer
# from ting_file_management.queue import Queue
# FIM_TESTE

# https://codare.aurelio.net/2007/01/30/python-imprimir-mensagens-de-erro-stderr/


# Recebe arquivo txt processa e add na instância da fila
# verifica se já existe o arquivo na fila
def process(path_file, instance):
    data = txt_importer(path_file)
    # print(data)
    data_details = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data,
    }
    print(data_details["nome_do_arquivo"])
    # print(data_details)
    for el in instance.data:
        if path_file == el["nome_do_arquivo"]:
            return False

    instance.enqueue(data_details)
    return sys.stdout.write(f"{data_details}\n")


# remove 1º el da fila
# verifica se a fila está vazia
def remove(instance):
    if not len(instance):
        return sys.stdout.write("Não há elementos\n")
    # file_removed = instance.dequeue()
    # file_removed_name = file_remove["nome_do_arquivo"]
    # ou
    file_removed_name = instance.dequeue()["nome_do_arquivo"]
    return sys.stdout.write(
        f"Arquivo {file_removed_name} removido com sucesso\n"
    )


# busca info do arquivo na posição da fila
def file_metadata(instance, position):
    try:
        info = instance.search(position)
        print(info)
        sys.stdout.write(f"{info}\n")
    except IndexError:
        sys.stderr.write("Posição inválida")


# if __name__ == "__main__":
# instance_test = Queue()
# print(process("statics/arquivo_teste.txt", instance_test))
