""" 
    Autor: Bruno Rovea 
    Universidade Estadual do Oeste do Paraná - UNIOESTE
    Disciplina: Comunicação Analógica e Digital, 5° ano de Engenharia Elétrica
    Professor Maurício Menon
    Foz do Iguaçú, 28/Abril/2022
    V1.0
    Referências:
        - Principles of Eletronic Communication System, by Louis E. Frenzel Jr., Fourth Editi
"""


# Importação de bibliotecas
import numpy as np
from scipy.fft import fft, fftfreq, fftshift
import matplotlib.pyplot as plt
import os

# Cria a pasta onde serão salvos os gráficos
script_dir = os.path.dirname(__file__)
results_dir = os.path.join(script_dir, 'Resultados/Gráficos FM/')

if not os.path.isdir(results_dir):
    os.makedirs(results_dir)


# Número de pontos no qual o sinal será amostrado
N = 50000
# Tempo de simulação
T = 1/(2*N)
# Vetor tempo
t = np.linspace(0, N*T, N, endpoint=False)
m = 10

# Frequência do sinal modulador [Hz]
fm = 200

# Frequência da portadora [Hz]
fc = 4000


# Definição do sinal modulante
M0 = 0
Em = 1
wm = 2*np.pi*fm
em = Em*np.sin(wm*t)+M0

# Definição dda portadora
E0 = 1
wc = 2*np.pi*fc
ec = E0*np.sin(wc*t)

# Sinal modulado (beiond the scope of this book)
e = np.sin( 2*np.pi*fc*t + (m*np.sin(2*np.pi*fm*t)) )

# Definição da FFT (Análise espectral)
yf = fft(e[:N])
xf = fftfreq(N, T)
xf = fftshift(xf)
yplot = fftshift(yf)


# Curvas no tempo
plt.figure(figsize = (10, 5))         
plt.title('Sinal modulante ($fm=%d$ Hz)' %fm)   
plt.xlabel('Tempo [s]')              
plt.ylabel('Sinal modulante [V]')
plt.plot(t, em,'r')
plt.xlim(0, 3*(1/fm))
plt.grid(True, axis = 'both')        
plt.tight_layout(pad=4.0)
plt.savefig('Resultados/Gráficos FM/FM_Sinal_Modulante.png', dpi=300)

plt.figure(figsize = (10, 5))         
plt.title('Sinal da onda portadora ($fc=%d$ Hz)' %fc)   
plt.xlabel('Tempo [s]')              
plt.ylabel('Portadora [V]')
plt.plot(t, ec,'b')
plt.xlim(0, 3*(1/fc))           
plt.grid(True, axis = 'both')        
plt.tight_layout(pad=4.0)
plt.savefig('Resultados/Gráficos FM/FM_Portadora.png', dpi=300)

plt.figure(figsize = (10, 5))         
plt.title('Sinal modulado ($m=%f$)' %m)   
plt.xlabel('Tempo [s]')              
plt.ylabel('Sinal modulado [V]')         
plt.plot(t, e,'y')
plt.xlim(0, 3*(1/fm)/2)
plt.grid(True, axis = 'both')        
plt.tight_layout(pad=4.0)
plt.savefig('Resultados/Gráficos FM/FM_Sinal_Modulado.png', dpi=300)

plt.figure(figsize = (10, 5))         
plt.title('FM - Sinais Modulante, Portadora e Modulado')  
plt.xlabel('Tempo [s]')              
plt.ylabel('Sinal modulado [V]')       
plt.plot(t, em,'r', label='Sinal Modulante')
# plt.plot(t, ec,'b', label='Portadora')   
plt.plot(t, e,'y', label='Sinal Modulado')
plt.legend(loc='upper right', shadow=True)
plt.xlim(0, 3*(1/fm))
plt.grid(True, axis = 'both')        
plt.tight_layout(pad=4.0)
plt.savefig('Resultados/Gráficos FM/FM_Sobreposição_Sinais.png', dpi=300)


# Análise espectral do sinal modulado
plt.figure(figsize=(12,4))
plt.title('Análise espectral do sinal modulado')   
plt.xlabel('Frequência [Hz]')              
plt.ylabel('sinal modulado [V]')
plt.plot(xf, 1.0/N * np.abs(yplot))
plt.xlim(0, 7500)
plt.savefig('Resultados/Gráficos FM/FM_Analise_espectral.png', dpi=300)
plt.grid()
