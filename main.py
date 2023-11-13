#while

numero = int(input("digite um número: "))

contador = 0

while contador <= numero:
  print("Número =", contador)
  print(f"Número = {contador}")
  contador += 1


print("---------------------------------------------")

contador = int(input("digite um número: "))

while contador >= 0:
  print("Número = ", contador)
  contador -= 1


print("---------------------------------------------")

numero = int(input("digite um número para saber a tabuada: "))

i = 0
while i <= 10:
  resultado = numero * i
  print(f"{numero} x {i} = {resultado}")
  i += 1


print("---------------------------------------------")

while True:
  numero = int(input("Digite um número para saber a tabuada: "))
  if numero >=1 and numero <= 10:
    break
  else:
    (print("fora do intervalo permitido"))

i = 0
while i <= 10:
  resultado = numero * i
  print(f"{numero} x {i} = {resultado}")
  i += 1

