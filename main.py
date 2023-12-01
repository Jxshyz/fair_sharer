import ruff
import pytest

def fair_sharer(values, num_iterations, share=0.1):
    if not isinstance(values, list):
        raise ValueError(f"{values} muss eine Liste sein")
    
    num_iterations = int(num_iterations)
    new_values = values.copy()

    for _ in range(num_iterations):
        idx = new_values.index(max(new_values))
        highest_value = new_values[idx]

        # Berechnung der Indizes für linke und rechte Nachbarn
        left = (idx - 1) % len(new_values)
        right = (idx + 1) % len(new_values)

        # Verteilung des Anteils
        new_values[left] += highest_value * share
        new_values[right] += highest_value * share
        new_values[idx] -= highest_value * share * 2

    return new_values

# Test der Funktion
if __name__ == "__main__":
    a = [0, 1000, 800, 0]
    print(fair_sharer(a, 1))