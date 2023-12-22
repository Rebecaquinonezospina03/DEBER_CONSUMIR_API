import requests

url = 'https://dummy.restapiexample.com/api/v1/employees'
empleados = requests.get(url).json()

# Cantidad de empleados
cantidad_empleados = len(empleados['data'])
print(f"Cantidad de empleados es: {cantidad_empleados}")

# Calcular promedio de salario
salarios = [empleado['employee_salary']
            for empleado in empleados['data']]
promedio_salario = sum(salarios) / cantidad_empleados
print(f"Promedio de salario es: {promedio_salario:.2f}")

# Calcular promedio de edad
edades = [empleado['employee_age']
          for empleado in empleados['data']]
promedio_edad = sum(edades) / cantidad_empleados
print(f"Promedio de edad es: {promedio_edad:.1f}")

# Salario mínimo y máximo
salario_minimo = min(salarios)
print(f"Salario mínimo que hay es: {salario_minimo}")

salario_maximo = max(salarios)
print(f"Salario máximo que hay es: {salario_maximo}")

# Edad mínima y máxima
edad_minima = min(edades)
print(f"La edad mínima es: {edad_minima}")

edad_maxima = max(edades)
print(f"La edad máxima: {edad_maxima}")
