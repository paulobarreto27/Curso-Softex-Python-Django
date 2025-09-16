

def celcius_fahrenheit(temperatura_c: float) -> float:
    temperatura_f = (temperatura_c * (9 / 5)) + 32
    return temperatura_f

temperatura_celsius = float(imput("Informe a temperatura em Celsius: "))
temperatura_f = celcius_fahrenheit(temperatura_celsius)
print(f"A temperatura de {temperatura_celsius:.2f} equivale a {}")