# Explicação do Código `num_primos.py`

Este arquivo define uma função `is_prime(n)` que verifica se um número inteiro `n` é primo.

## Como funciona

1. `if n <= 1:`
   - Números menores ou iguais a 1 não são primos.
   - Retorna `False`.

2. `if n <= 3:`
   - Os números 2 e 3 são primos.
   - Retorna `True`.

3. `if n % 2 == 0 or n % 3 == 0:`
   - Elimina divisíveis por 2 ou por 3.
   - Retorna `False` para múltiplos de 2 ou 3.

4. `i = 5`
   - Usa uma técnica otimizada que testa apenas números na forma `6k - 1` e `6k + 1`.

5. `while i * i <= n:`
   - Verifica divisores até a raiz quadrada de `n`.
   - Isso é suficiente porque qualquer fator maior que a raiz quadrada teria um par menor.

6. `if n % i == 0 or n % (i + 2) == 0:`
   - Testa `i` e `i + 2` (ex: 5 e 7, 11 e 13, etc.).
   - Se `n` for divisível por qualquer um, retorna `False`.

7. `i += 6`
   - Avança para o próximo par de candidatos de teste.

8. `return True`
   - Se nenhum divisor for encontrado, `n` é primo.

## Execução direta do arquivo

Quando o arquivo é executado como programa principal (`python num_primos.py`), ele testa uma lista de exemplos:

- `[1, 2, 3, 4, 17, 18, 19, 20]`

E imprime o resultado de `is_prime(valor)` para cada valor.

## Observações

- O algoritmo é eficiente para números moderados, porque evita testar todos os números e usa apenas verificações até a raiz quadrada.
- A função retorna sempre um valor booleano (`True` ou `False`).
