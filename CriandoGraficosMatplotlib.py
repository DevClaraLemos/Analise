import matplotlib.pyplot as plt

idades = [23, 78, 22, 19, 45]
nomes = ['João', 'Ana', 'Maria', 'Carlos', 'Pedro']

plt.bar(nomes, idades)
plt.xlabel('Nomes')
plt.ylabel('Idades')
plt.title('Idades por Nome')
plt.show()
