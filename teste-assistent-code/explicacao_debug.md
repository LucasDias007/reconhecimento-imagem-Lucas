# Erros e Correções em `debug.py`

## Problemas encontrados

1. **Prompt de input sem aspas**
   - Código original: `item1 = float(input(Preço do item 1? ))`
   - Causa: O prompt estava escrito sem aspas, então o Python tentou interpretar `Preço` como um nome de variável.
   - Erro gerado: `SyntaxError`.

2. **Valor de desconto lido como texto**
   - Código original: `desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))`
   - Causa: A função `input()` retorna uma string. Em seguida, o código fazia `desconto_cupom / 100`.
   - Erro gerado: `TypeError` ao tentar dividir uma string por um número.

3. **Comparação inválida de tipos**
   - Código original: `if desconto_cupom > 0:`
   - Causa: `desconto_cupom` ainda era uma string; comparar string com inteiro não é válido.
   - Erro possível: `TypeError` ou comportamento incorreto.

4. **Impressão sem f-string**
   - Código original: `print(" Item 2:        R$ {total_item2:.2f}")`
   - Causa: A string não era uma f-string, então `{total_item2:.2f}` não foi substituído pelo valor real.
   - Resultado: A mensagem exibida mostraria o texto literal em vez do valor formatado.

5. **Indentação incorreta no bloco condicional**
   - Código original:
     ```python
     if desconto_cupom > 0: 
     print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
     ```
   - Causa: A linha dentro do `if` não estava indentada.
   - Erro gerado: `IndentationError`.

## Correções aplicadas

- Adicionei funções auxiliares `read_int()` e `read_float()` para tornar a leitura mais expressiva.
- Corrigi a chamada de `input()` para `item1` e usei `float()` corretamente no prompt.
- Converti o valor do cupom de desconto para `float` imediatamente após a leitura.
- Usei `desconto_percentual` como variável numérica para comparação e cálculo.
- Corrigi a impressão do item 2 usando uma f-string.
- Ajustei a indentação do bloco `if desconto_percentual > 0:`.
- Incluí `if __name__ == "__main__"` para organizar a execução do script.

## Resultado

O código agora funciona corretamente, calcula subtotal, imposto e desconto, e imprime o relatório com valores formatados em reais.
