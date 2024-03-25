import unittest
from cadastrar_tarefa import Tarefa, cadastrar_tarefa, visualizar_tarefas, atualizar_tarefa, excluir_tarefa

class TestTarefa(unittest.TestCase):
    def test_init(self):
        descricao = "Estudar"
        data_vencimento = "2024-05-10"
        prioridade = "alta"

        tarefa = Tarefa(descricao, data_vencimento, prioridade)
        self.assertEqual(tarefa.descricao, descricao)
        self.assertEqual(tarefa.data_vencimento, data_vencimento)
        self.assertEqual(tarefa.prioridade, prioridade)

class TestCadastrarTarefa(unittest.TestCase):
    def test_cadastrar_tarefa(self):
        descricao = "Estudar"
        data_vencimento = "2024-05-10"
        prioridade = "alta"

        tarefa = cadastrar_tarefa(descricao, data_vencimento, prioridade)
        self.assertIsNotNone(tarefa)
        self.assertEqual(tarefa.descricao, descricao)
        self.assertEqual(tarefa.data_vencimento, data_vencimento)
        self.assertEqual(tarefa.prioridade, prioridade)

class TestVisualizarTarefas(unittest.TestCase):
    def test_visualizar_tarefas(self):
        lista_tarefas = [
            Tarefa("Estudar", "2024-05-10", "alta"),
            Tarefa("Trabalhar", "2024-05-15", "média"),
            Tarefa("Ler", "2024-05-20", "baixa")
        ]
        visualizar_tarefas(lista_tarefas)
        lista_tarefas = []

class TestAtualizarTarefa(unittest.TestCase):
    def test_atualizar_tarefa(self):
        lista_tarefas = [
            Tarefa("Estudar", "2024-05-10", "alta"),
            Tarefa("Trabalhar", "2024-05-15", "média"),
            Tarefa("Ler", "2024-05-20", "baixa")
        ]
        
        resposta_input = ['1', 'Nova descrição', '2024-05-12', 'média']
        def input_mock(prompt):
            return resposta_input.pop(0)
        
        original_input = __builtins__.input
        __builtins__.input = input_mock
        
        try:
            atualizar_tarefa(lista_tarefas)
        finally:
    
            __builtins__.input = original_input
            
        lista_tarefas = []   

class TestExcluirTarefa(unittest.TestCase):
    def test_excluir_tarefa(self):
        lista_tarefas = [
            Tarefa("Estudar", "2024-05-10", "alta"),
            Tarefa("Trabalhar", "2024-05-15", "média"),
            Tarefa("Ler", "2024-05-20", "baixa")
        ]
        
        resposta_input = ['2']
        def input_mock(prompt):
            return resposta_input.pop(0)
        
        original_input = __builtins__.input
        __builtins__.input = input_mock
        
        try:
            excluir_tarefa(lista_tarefas)
        finally:
            __builtins__.input = original_input
        lista_tarefas = []        

if __name__ == '__main__':
    unittest.main()
