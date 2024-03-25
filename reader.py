import sys
import csv

def read_csv(file_name):
    with open(file_name, 'r', newline='') as file:
        reader = csv.reader(file, delimiter=';')  # Ustawienie separatora na średnik
        return list(reader)
    
def modify_csv(data, changes):
    max_rows = len(data)
    max_cols = max(len(row) for row in data) if data else 0

    for change in changes:
        parts = change.split(',')
        if len(parts) != 3:
            print(f"Ostrzeżenie: Nieprawidłowy format zmiany: '{change}'. Pomijam tę zmianę.")
            continue
        
        x, y, value = map(str.strip, parts)
        x, y = int(x)+1, int(y)+1  # Zwiększ wartości współrzędnych o 1
        if 1 <= x <= max_cols and 1 <= y <= max_rows:
            data[y-1][x-1] = value  # Zmniejsz wartości współrzędnych o 1
        else:
            print(f"Ostrzeżenie: Zmiana '{change}' znajduje się poza zakresem pliku CSV.")

def write_csv(data, file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

input_file = sys.argv[1]
output_file = sys.argv[2]
changes = sys.argv[3:]

try:
    data = read_csv(input_file)
except FileNotFoundError:
    print(f"Plik '{input_file}' nie znaleziony!")
    sys.exit(1)

for change in changes:
    try:
        x, y, value = map(str.strip, change.split(','))
        int(x)
        int(y)
    except ValueError:
        print("Nieprawidłowy format zmiany. Format zmiany powinien być 'x,y,wartość'!")
        sys.exit(1)

modify_csv(data, changes)
write_csv(data, output_file)  

print(f"Pomyślnie zmodyfikowano i zapisano plik jako '{output_file}'!")

