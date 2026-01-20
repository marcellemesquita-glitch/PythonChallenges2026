import re
from collections import Counter

'''
Processe um texto longo e identifique padrões: palavras mais frequentes, comprimento médio, palavras únicas. 
Pense: como você organizaria esses dados para consultas rápidas? 
Qual estrutura facilita contar ocorrências?

'''
text = input("Digite o seu texto: ")

def TextAnaliser(text):
    text = text.lower()
    all_words = re.split(r"[!?.:, ]", text)

    # Remover espaços em branco da lista de palavras
    for word in all_words:
        if word == '':
            all_words.remove(word)
    
    # Cria um set com as palavras únicas e crie um dicionário as palvras e suas repetições
    unique_words = set(all_words)
    contagem = Counter(all_words)

    # Identificar as repetições máximas e criar uma lista com as palavras mais repetidas
    repeticoes_max = max(contagem.values())
    maximos = {k: v for k, v in contagem.items() if v == repeticoes_max}

    tam_words = []
    for i in all_words:
        x = len(i)
        tam_words.append(x)

    # Exibir relatório com os dados
    print(f"\n--- RELATÓRIO DE ANÁLISE ---")
    print(f"   Número de palavras: {len(all_words)}")
    print(f"   Número de palavras únicas: {len(unique_words)}")
    print(f"   Palavras mais repetidas: ", end="")
    print(", ".join(maximos))
    print(f"   Comprimento médio das palavras: {round(sum(tam_words)/len(all_words))}")

TextAnaliser(text)


