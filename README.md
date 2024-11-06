# Modulação de Sinais Analógicos

Neste documento, abordamos as técnicas de modulação em amplitude e modulação em frequência, que são amplamente utilizadas em sistemas de comunicação analógica. A modulação é o processo de variação de uma característica de uma onda portadora (como amplitude, frequência ou fase) em função de um sinal modulante, que contém a informação a ser transmitida. Três técnicas principais são exploradas: Modulação em Amplitude (AMDSB), Modulação em Amplitude com Suprimido de Portadora (AMDSB-SC) e Modulação em Frequência (FM). Cada técnica é descrita com suas respectivas equações e uma análise espectral do sinal modulado.

## 1. Modulação em Amplitude com Banda Dupla (AMDSB)

A técnica de modulação AMDSB, ou Amplitude Modulation Double Sideband, consiste na multiplicação de um sinal modulante pela onda portadora. O sinal resultante carrega informações nas frequências superiores e inferiores em torno da frequência da portadora.

### Equações Utilizadas

No código, as seguintes equações matemáticas descrevem o processo de modulação:

1. **Sinal Modulante**: 
   $$
   e_m(t) = M_0 + E_m \cdot \sin(w_m t)
   $$
   onde:
   - $M_0$ é a amplitude constante do sinal modulante,
   - $E_m$ é a amplitude ajustada pelo índice de modulação $m$,
   - $w_m = 2\pi f_m$, com $f_m$ sendo a frequência do sinal modulante.

2. **Onda Portadora**:
   $$
   e_c(t) = E_0 \cdot \sin(w_c t)
   $$
   onde:
   - $E_0$ é a amplitude da portadora,
   - $w_c = 2\pi f_c$, com $f_c$ sendo a frequência da portadora.

3. **Sinal Modulado (AMDSB)**:
   $$
   e(t) = e_m(t) \cdot e_c(t)
   $$
   O sinal modulado em AMDSB é obtido pela multiplicação do sinal modulante pela portadora, gerando componentes de frequência em torno da portadora.

![Sobreposição dos Sinais](Resultados/Gráficos%20AMDSB/AMDSB_Sobreposição_Sinais.png)

**Figura 1**: Sobreposição dos Sinais Modulante, Portadora e Modulado.

### Análise Espectral

A Transformada de Fourier (FFT) é utilizada para realizar uma análise espectral do sinal modulado, destacando as componentes de frequência em torno da portadora, caracterizando o espectro AMDSB.

![Análise Espectral](Resultados/Gráficos%20AMDSB/AMDSB_Analise_espectral.png)

**Figura 2**: Análise Espectral do Sinal Modulado.

## 2. Modulação em Amplitude com Banda Dupla e Suprimido de Portadora (AMDSB-SC)

A modulação AMDSB-SC, ou Amplitude Modulation Double Sideband Suppressed Carrier, é semelhante à AMDSB, com a diferença de que a portadora é suprimida, deixando apenas as bandas laterais para a transmissão do sinal. Essa técnica economiza energia e largura de banda, pois não transmite a portadora que, no caso da AMDSB convencional, consome uma parte significativa da potência do sinal transmitido.

### Equações Utilizadas

No código, as seguintes equações descrevem o processo de modulação AMDSB-SC:

1. **Sinal Modulante**:
   $$
   e_m(t) = E_m \cdot \sin(w_m t)
   $$
   onde:
   - $E_m$ é a amplitude ajustada pelo índice de modulação $m$,
   - $w_m = 2\pi f_m$, com $f_m$ sendo a frequência do sinal modulante.

2. **Onda Portadora**:
   $$
   e_c(t) = E_0 \cdot \sin(w_c t)
   $$
   onde:
   - $E_0$ é a amplitude da portadora,
   - $w_c = 2\pi f_c$, com $f_c$ sendo a frequência da portadora.

3. **Sinal Modulado (AMDSB-SC)**:
   $$
   e(t) = e_m(t) \cdot e_c(t)
   $$
   A multiplicação do sinal modulante pela portadora gera um sinal modulado onde a portadora é suprimida, deixando somente as bandas laterais.

![Sobreposição dos Sinais AMDSB-SC](Resultados/Gráficos%20AMDSB-SC/AMDSB-SC_Sobreposição_Sinais.png)

**Figura 3**: Sobreposição dos Sinais Modulante, Portadora e Modulado para o AMDSB-SC.

### Análise Espectral

A Transformada de Fourier (FFT) é utilizada para realizar a análise espectral do sinal modulado, evidenciando as bandas laterais ao redor da frequência da portadora. Esse espectro caracteriza a modulação AMDSB-SC, mostrando que a portadora foi suprimida.

![Análise Espectral AMDSB-SC](resultados/Gráficos%20AMDSB-SC/AMDSB-SC_Analise_espectral.png)

**Figura 4**: Análise Espectral do Sinal Modulado em AMDSB-SC.

## 3. Modulação em Frequência (FM)

A modulação em frequência, ou Frequency Modulation (FM), é uma técnica onde a frequência da portadora é variada em função do sinal modulante. A vantagem da FM sobre a AM é a sua maior imunidade a ruídos, já que o sinal é codificado na frequência em vez de na amplitude. O desvio de frequência é diretamente proporcional ao valor do sinal modulante, fazendo com que o espectro do sinal FM seja caracterizado por um conjunto de frequências laterais ao redor da portadora.

### Equações Utilizadas

No código, as seguintes equações descrevem o processo de modulação FM:

1. **Sinal Modulante**:
   $$
   e_m(t) = E_m \cdot \sin(w_m t) + M_0
   $$
   onde:
   - $E_m$ é a amplitude do sinal modulante,
   - $w_m = 2\pi f_m$, com $f_m$ sendo a frequência do sinal modulante,
   - $M_0$ é um valor médio, ajustado para centralizar o sinal em torno de um valor fixo.

2. **Onda Portadora**:
   $$
   e_c(t) = E_0 \cdot \sin(w_c t)
   $$
   onde:
   - $E_0$ é a amplitude da portadora,
   - $w_c = 2\pi f_c$, com $f_c$ sendo a frequência da portadora.

3. **Sinal Modulado (FM)**:
   $$
   e(t) = \sin(2\pi f_c t + m \cdot \sin(2\pi f_m t))
   $$
   onde $m$ é o índice de modulação que define o desvio de frequência em função da amplitude do sinal modulante.

![Sobreposição dos Sinais FM](Resultados/Gráficos%20FM/FM_Sobreposição_Sinais.png)

**Figura 5**: Sobreposição dos Sinais Modulante e Modulado para a Modulação FM.

### Análise Espectral

A Transformada de Fourier (FFT) é utilizada para realizar a análise espectral do sinal modulado, mostrando a distribuição de frequências laterais ao redor da frequência central. Esse espectro caracteriza a modulação em frequência, onde o sinal ocupa uma largura de banda maior que a modulação em amplitude.

![Análise Espectral FM](Resultados/Gráficos%20FM/FM_Analise_espectral.png)

**Figura 6**: Análise Espectral do Sinal Modulado em FM.

## Conclusão

As técnicas de modulação AMDSB, AMDSB-SC e FM possuem características e aplicações distintas. A AMDSB transmite tanto a portadora quanto as bandas laterais, ocupando maior largura de banda, enquanto a AMDSB-SC elimina a portadora, economizando energia e largura de banda. Por outro lado, a modulação FM varia a frequência da portadora de acordo com o sinal modulante, resultando em maior imunidade a ruídos, sendo especialmente útil em transmissões de áudio e rádio. Essas técnicas continuam a ser de extrema importância em sistemas de comunicação, cada uma com vantagens e desvantagens dependendo do tipo de aplicação e do ambiente de transmissão.
