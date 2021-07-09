"""
Permite adiconar/remover no começo e no final da lista

"""
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