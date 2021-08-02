"""
Permite adiconar/remover no começo e no final da lista
"""

# esse tipo de collection não é padrão precisa ser importado
from collections import deque

deq = deque("Leandro")
print(deq)

deq.appendleft("Adiciona no início")
print(deq)

deq.append("Adiciona no final")
print(deq)

# Remove do ínicio e no final
print(deq.popleft())
print(deq.pop())
print(deq)