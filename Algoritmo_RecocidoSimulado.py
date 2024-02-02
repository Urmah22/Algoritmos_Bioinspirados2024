import numpy as np

def distancia_total(ordenes, distancias):
    # Calcula la distancia total de la ruta
    distancia = 0
    for i in range(len(ordenes) - 1):
        distancia += distancias[ordenes[i], ordenes[i + 1]]
    distancia += distancias[ordenes[-1], ordenes[0]]  # Regreso al punto de partida
    return distancia

def recocido_simulado(distancias, temperatura_inicial=1000, factor_enfriamiento=0.95, iteraciones_por_temperatura=1000):
    n_ciudades = len(distancias)
    
    # Inicialización: creamos una solución aleatoria
    ruta_actual = np.random.permutation(n_ciudades)
    mejor_ruta = np.copy(ruta_actual)
    
    temperatura = temperatura_inicial
    
    while temperatura > 1:
        for _ in range(iteraciones_por_temperatura):
            # Genera una nueva solución vecina intercambiando dos ciudades aleatorias
            i, j = np.random.randint(0, n_ciudades, size=2)
            vecino = np.copy(ruta_actual)
            vecino[i], vecino[j] = vecino[j], vecino[i]
            
            # Calcula las diferencias de distancia
            delta_distancia = distancia_total(vecino, distancias) - distancia_total(ruta_actual, distancias)
            
            # Si la nueva solución es mejor o se acepta según una probabilidad, actualiza la solución actual
            if delta_distancia < 0 or np.random.rand() < np.exp(-delta_distancia / temperatura):
                ruta_actual = np.copy(vecino)
                
                # Actualiza la mejor solución si es necesario
                if distancia_total(ruta_actual, distancias) < distancia_total(mejor_ruta, distancias):
                    mejor_ruta = np.copy(ruta_actual)
        
        # Enfría la temperatura
        temperatura *= factor_enfriamiento
    
    return mejor_ruta

# Ejemplo de uso
ciudades = 10
np.random.seed(42)
distancias = np.random.rand(ciudades, ciudades)

mejor_ruta = recocido_simulado(distancias)

print("Mejor ruta encontrada:", mejor_ruta)
print("Distancia total:", distancia_total(mejor_ruta, distancias))
