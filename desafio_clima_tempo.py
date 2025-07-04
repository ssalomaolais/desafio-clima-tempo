# Desafio ClimaTempo - GS de Pensamento Computacional
# Este script modela, plota e analisa duas funções de fenômenos naturais.

import numpy as np
import matplotlib.pyplot as plt

# --- 1. Implementação das Funções Matemáticas ---
# Implementação correta das funções matemáticas modeladas 

def onda_de_calor(t):
    """
    Calcula a temperatura T(t) para a onda de calor.
    t: tempo em meses
    """
    T = 35 + (1 - np.exp(-t / 27)) + t * np.exp(-34.33 * t)
    return T

def movimentos_terra(x):
    """
    Calcula a escala Richter e(x) para movimentos anômalos da terra.
    x: velocidade em m/s
    """
    e = 5.47 + 1.85 * np.exp(-x) * np.cos(np.sqrt(8) * x - 19.47) + (x - 1.365) * np.exp(-34.33 * x)
    return e

# --- 2. Geração de Dados para os Gráficos ---
# Intervalo de tempo de 0 a 36 meses para T(t) 
t_valores = np.linspace(0, 36, 1000)
temperatura_valores = onda_de_calor(t_valores)

# Intervalo de velocidade de 0 a 5 m/s para e(x) 
x_valores = np.linspace(0, 5, 1000)
richter_valores = movimentos_terra(x_valores)

# --- 3. Identificação dos Pontos Máximos e Mínimos ---
# Identificação correta dos pontos máximos e mínimos 

# Para a Onda de Calor T(t)
t_min = t_valores[np.argmin(temperatura_valores)]
t_max = t_valores[np.argmax(temperatura_valores)]
temp_min = np.min(temperatura_valores)
temp_max = np.max(temperatura_valores)

# Para os Movimentos da Terra e(x)
x_min = x_valores[np.argmin(richter_valores)]
x_max = x_valores[np.argmax(richter_valores)]
richter_min = np.min(richter_valores)
richter_max = np.max(richter_valores)


# --- 4. Plotagem dos Gráficos ---
# Plotagem precisa e legível dos gráficos para os dois fenômenos 
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))
fig.suptitle('Análise de Fenômenos Naturais - Desafio ClimaTempo', fontsize=16)

# Gráfico 1: Onda de Calor
ax1.plot(t_valores, temperatura_valores, label='T(t)')
ax1.plot(t_max, temp_max, 'ro', label=f'Máximo: ({t_max:.2f}, {temp_max:.2f})')
ax1.plot(t_min, temp_min, 'bo', label=f'Mínimo: ({t_min:.2f}, {temp_min:.2f})')
ax1.set_title('Onda de Calor: T(t)')
ax1.set_xlabel('Tempo (meses)')
ax1.set_ylabel('Temperatura (°C)')
ax1.legend()
ax1.grid(True)

# Gráfico 2: Movimentos da Terra
ax2.plot(x_valores, richter_valores, label='e(x)', color='orange')
ax2.plot(x_max, richter_max, 'ro', label=f'Máximo: ({x_max:.2f}, {richter_max:.2f})')
ax2.plot(x_min, richter_min, 'bo', label=f'Mínimo: ({x_min:.2f}, {richter_min:.2f})')
ax2.set_title('Movimentos Anômalos da Terra: e(x)')
ax2.set_xlabel('Velocidade (m/s)')
ax2.set_ylabel('Escala Richter')
ax2.legend()
ax2.grid(True)

# Ajusta o layout, salva e exibe os gráficos
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('graficos_clima_tempo.png')
plt.show()


# --- 5. Apresentação dos Resultados ---
# Organização e clareza do código e dos resultados 
print("--- Resultados da Análise ---")
print("\n1. Onda de Calor T(t):")
print(f"  - Ponto Máximo: Temperatura de {temp_max:.2f}°C ocorre no mês t = {t_max:.2f}")
print(f"  - Ponto Mínimo: Temperatura de {temp_min:.2f}°C ocorre no mês t = {t_min:.2f}")
print("\n2. Movimentos da Terra e(x):")
print(f"  - Ponto Máximo: Escala de {richter_max:.2f} ocorre na velocidade x = {x_max:.2f} m/s")
print(f"  - Ponto Mínimo: Escala de {richter_min:.2f} ocorre na velocidade x = {x_min:.2f} m/s")