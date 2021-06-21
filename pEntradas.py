import sys
texto=sys.argv[1]

print(len(sys.argv))

print("El texto es: {:>20})".format(texto))
print("El texto es: {:.3}".format(texto))
print("El texto es:{:^20.1}".format(texto))
print("El texto es: {:05d}".format(150))
print("El texto es: {:7d}".format(7887))
print("El texto es: {:07.3f}".format(20.02))
