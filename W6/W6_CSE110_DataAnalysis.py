# Abre el archivo y lee los datos
with open('life-expectancy.csv') as file:
    data = file.readlines()

# Variables para almacenar información global
max_life_exp = float('-inf')
min_life_exp = float('inf')

# Iterar sobre los datos y obtener los valores mínimos y máximos de esperanza de vida
for line in data[1:]:  # Omitir la primera fila de encabezados
    parts = line.strip().split(',')
    life_exp = float(parts[3])  # Suponiendo que la columna 3 contiene la esperanza de vida

    if life_exp > max_life_exp:
        max_life_exp = life_exp

    if life_exp < min_life_exp:
        min_life_exp = life_exp

# Imprimir resultados
print(f"Máxima esperanza de vida: {max_life_exp}")
print(f"Mínima esperanza de vida: {min_life_exp}")
