import json
import os

# Dados das transações
transacoes = []

def adicionar_transacao(tipo, valor, descricao, data):
    if tipo not in ['receita', 'despesa'] or valor < 0:
        print("Erro ao adicionar transação. Verifique o tipo e o valor inserido.")
        return

    transacao = {
        'tipo': tipo,
        'valor': valor,
        'descricao': descricao,
        'data': data
    }
    transacoes.append(transacao)
    print("Transação adicionada com sucesso:")
    print(transacao)

def remover_transacao(identificador):
    if isinstance(identificador, int) and identificador < len(transacoes):
        transacao = transacoes.pop(identificador)
        print("Transação removida:")
        print(transacao)
    else:
        print("Erro ao remover transação. Verifique o identificador.")

def visualizar_relatorio():
    receitas = sum(transacao['valor'] for transacao in transacoes if transacao['tipo'] == 'receita')
    despesas = sum(transacao['valor'] for transacao in transacoes if transacao['tipo'] == 'despesa')
    saldo = receitas - despesas

    print("Relatório Financeiro:")
    print(f"Receitas totais: {receitas}")
    print(f"Despesas totais: {despesas}")
    print(f"Saldo atual: {saldo}")

def obter_insights():
    receitas = sum(transacao['valor'] for transacao in transacoes if transacao['tipo'] == 'receita')
    despesas = sum(transacao['valor'] for transacao in transacoes if transacao['tipo'] == 'despesa')
    saldo = receitas - despesas

    if saldo < 0:
        print("Você está gastando mais do que está recebendo. Considere reduzir suas despesas.")
    elif saldo == 0:
        print("Seus gastos estão equilibrados com suas receitas.")
    else:
        print("Você está economizando mais do que está gastando. Parabéns!")

def salvar_dados():
    with open('transacoes.json', 'w') as arquivo:
        json.dump(transacoes, arquivo)
    print("Dados salvos com sucesso.")

def carregar_dados():
    global transacoes
    try:
        with open('transacoes.json', 'r') as arquivo:
            transacoes = json.load(arquivo)
        print("Dados carregados com sucesso.")
    except (FileNotFoundError, json.JSONDecodeError):
        print("Nenhum dado encontrado ou erro ao carregar os dados.")