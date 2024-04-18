def calculate_L(lambda_val, mu_val):
    L = (1 - (lambda_val / mu_val)) * ((lambda_val / mu_val) ** 0)
    return L

lambda_val = 30
mu_val = 35

#insiso A
L = calculate_L(lambda_val, mu_val)
print("probabilidad de que haya 0 clientes en el sistema",L*100,"%")

#inciso B
fraction = lambda_val / mu_val
print("utilización del empleado en la caja registradora ",fraction*100,"%")

#insiso C
num_pro=lambda_val/(mu_val-lambda_val)
print("numero promedio de clientes en el sistema",round(num_pro),"clientes")

#Insiso D
Lq=((lambda_val)**2)/(mu_val*(mu_val-lambda_val))
print("numero promedio de clientes formaos en la linea",round(Lq),"clientes")

#Insiso E
W=1/(mu_val-lambda_val)
print("tiempo que los clientes es ",W*60,"minutos")

#Insiso F
Wq=Lq/lambda_val
print("el tiempo promedio de atencion es ", Wq*60," minutos")