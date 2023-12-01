def fair_sharer(values, num_iterations, share=0.1):

    if type(num_iterations) is int:
        
        for i in range(num_iterations):
            # Kopie der Liste
            new_values = values

            # Indexierung, höchster Wert
            idx = new_values.index(max(values))
            highest_value = new_values[idx]

            # Berechnungen
            new_values[idx - 1] = new_values[idx - 1] + highest_value*share
            new_values[idx + 1] = new_values[idx + 1] + highest_value*share
            new_values[idx] = new_values[idx] - highest_value*share*2
            return new_values
    else: 
        print(f" {num_iterations} muss eine Zahl sein!")

a = [0, 1000, 800, 0]

print(fair_sharer(a, 1))


