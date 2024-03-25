class Tarefa:
    def __init__(self, descricao, data_vencimento, prioridade):
        self.descricao = descricao
        self.data_vencimento = data_vencimento
        self.prioridade = prioridade

def cadastrar_tarefa(descricao=None, data_vencimento=None, prioridade=None):
    if descricao is None:
        descricao = input("Digite a descrição da tarefa: \n")
    if data_vencimento is None:
        data_vencimento = input("Digite a data de vencimento da tarefa (formato YYYY-MM-DD): \n")

    lista_prioridades = ['baixa', 'média', 'alta']
    tentativas = 0
    while tentativas < 3:
        if prioridade is None:
            prioridade = input("Digite a prioridade da tarefa com valor válido (baixa, média, alta): \n")
        if prioridade in lista_prioridades:
            nova_tarefa = Tarefa(descricao, data_vencimento, prioridade)
            return nova_tarefa
        print("Por favor, digite uma prioridade válida (baixa, média, alta).")
        tentativas += 1
    else:
        print("Limite de tentativas atingido. Não foi possível cadastrar a tarefa.")
        return None

def visualizar_tarefas(lista_tarefas):
    if not lista_tarefas:
        print("Não há tarefas cadastradas.")
    else:
        print("Tarefas cadastradas:")
        
        tarefas_ordenadas = sorted(lista_tarefas, key=lambda x: x.prioridade)

        for idx, tarefa in enumerate(tarefas_ordenadas, start=1):
            print(f"Tarefa {idx}:")
            print("Descrição:", tarefa.descricao)
            print("Data de vencimento:", tarefa.data_vencimento)
            print("Prioridade:", tarefa.prioridade)
            print()


def atualizar_tarefa(lista_tarefas):
    visualizar_tarefas(lista_tarefas)
    if not lista_tarefas:
        return

    idx_tarefa = int(input("Digite o número da tarefa que deseja atualizar: ")) - 1
    if idx_tarefa < 0 or idx_tarefa >= len(lista_tarefas):
        print("Número de tarefa inválido.")
        return

    tarefa = lista_tarefas[idx_tarefa]
    print(f"Tarefa selecionada: {tarefa.descricao}")

    descricao = input("Digite a nova descrição da tarefa: ")
    data_vencimento = input("Digite a nova data de vencimento da tarefa (formato YYYY-MM-DD): ")
    prioridade = input("Digite a nova prioridade da tarefa (baixa, média, alta): ")

    tarefa.descricao = descricao
    tarefa.data_vencimento = data_vencimento
    tarefa.prioridade = prioridade
    print("Tarefa atualizada com sucesso!")

def excluir_tarefa(lista_tarefas):
    visualizar_tarefas(lista_tarefas)
    if not lista_tarefas:
        return

    idx_tarefa = int(input("Digite o número da tarefa que deseja excluir: ")) - 1
    if idx_tarefa < 0 or idx_tarefa >= len(lista_tarefas):
        print("Número de tarefa inválido.")
        return

    tarefa = lista_tarefas.pop(idx_tarefa)
    print(f"Tarefa '{tarefa.descricao}' excluída com sucesso!")

def main():
    lista_tarefas = []

    while True:
        print("\nOpções:")
        print("1. Cadastrar nova tarefa")
        print("2. Visualizar tarefas cadastradas")
        print("3. Atualizar tarefa")
        print("4. Excluir tarefa")
        print("5. Sair do programa")

        opcao = input("Digite o número da opção desejada: ")
        if opcao == '1':
            tarefa_cadastrada = cadastrar_tarefa()
            if tarefa_cadastrada:
                lista_tarefas.append(tarefa_cadastrada)
        elif opcao == '2':
            visualizar_tarefas(lista_tarefas)
        elif opcao == '3':
            atualizar_tarefa(lista_tarefas)
        elif opcao == '4':
            excluir_tarefa(lista_tarefas)
        elif opcao == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, digite um número de 1 a 5.")

if __name__ == "__main__":
    main()
