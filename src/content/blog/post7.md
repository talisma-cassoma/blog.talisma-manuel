---
title: "Meus achados do 5-Day Edgeneer Challenge da Think Autonomous"
description: "A jornada prática e os aprendizados de engenharia ao projetar um drone de entrega autônomo durante o evento 5-Day Edgeneer Challenge."
heroImage: "/5-day-challenge/thinkautonomous-5-days-challenge.jpeg"
pubDate: "September 02 2026"
tags: ["robotics", "software architecture", "computer vision", "drone"]
draft: false
---

Entre os dias 31 de agosto e 5 de setembro de 2026, participei do **5-Day Edgeneer Challenge**, um evento imersivo promovido pela *Think Autonomous*. O objetivo do desafio era direto e exigente: projetar a arquitetura completa de um robô autônomo em apenas 5 dias, justificando escolhas de hardware, limitações físicas, orçamento e algoritmos de controle diante de críticas da comunidade e de um revisor técnico fictício ("The Prosecutor").

Abaixo, compartilho os bastidores dessa jornada, os erros de premissa que cometi e a evolução do meu pensamento de engenharia.

---

## O Desafio e as Regras do Jogo

O evento propôs três cenários com orçamentos e restrições bem definidos:

**Option A: Autonomous Shuttle for School Campus (15,000$ budget)**

Context: This is what I worked on first when I became self-driving car engineer. In your case, it's a 12-passenger shuttle running a fixed loop on a school campus. Most passengers are standing while the vehicle goes up to 30 km/h in service.

Pros: The route is always the same, and contains known elements (signs, traffic lights cyclists, …). GPS works 90% of the road, but one tunnel section.

Cons: Standing passengers mean a phantom brake injures the people inside, so false positives cost as much as false negatives. The map isn't updated when parked cars, constructions, or other objects show up. GPS doesn't work in a tunnel.

Do you like this option? Let's see the other ones…

**Option B: Military UGV (30,000$ budget)**

Context: One of my first job interview was for a French contractor who built autonomous tanks and UGV (Unmanned Ground Vehicle) robots. I was sweating when they were asking me questions like "Would you DIE for your country, right now???". Today, dozens of my Edgeneers and B2B clients work in the defense space, which is extremely fast growing.

Pros: It drives at low speed for the most part, and if you hit a rock, nobody gets hurt. You have a high budget and high compute.

Cons: It's an off-road vehicle driving, there are no roads, no signs, cyclist, or pedestrians. GPS/GNSS is jammed for the most part and weather is terrible (dust, sand, fog, rain, mud, …).

What do you think of this one? The last one will definitely elevate you…

**Option C: A delivery drone (5,000$ budget)**

Context: You may not know this, but in places like China, it's perfectly normal to get your food delivered by a drone. This is coming to the U.S too, and at some point, it'll be in Europe. Want to work on it?

Pros: You fly in 3D, and drones are exciting. You can drive above most obstacles, and can map the region too.

Cons: When getting low, objects are buildings, telephone lines, or even pedestrians and cars. Your drone cannot carry heavy rotating LiDARs.

Escolhi a **Opção C (Delivery Drone)** pelo alto nível de desafio e complexidade: operações em espaço aéreo tridimensional, severa restrição de peso, limitações energéticas da bateria e necessidade de navegar em ambientes urbanos densos com obstáculos finos (cabos, linhas telefônicas e galhos).

<p align="center">  
  <img src="/5-day-challenge/Screenshot_2026-08-31_at_14.05.36.avif" alt="Painel de seleção do caso de uso">
</p>

---

## Day 1: O Sensor Stack e as Primeiras Armadilhas

A missão do primeiro dia era selecionar a suíte de sensores utilizando uma tabela fechada de componentes com preços pré-definidos:

<p align="center">  
  <img src="/5-day-challenge/ef9a4aee-64e4-42bc-8222-17d9f8b95b0d.avif" alt="Catálogo de sensores disponíveis no desafio">
</p>

### Minha Primeira Proposta
Inicialmente, sugerir montar um kit *off-the-shelf* baseado em um frame Holybro X500 V2 com ArduPilot, utilizando uma única câmera estéreo frontal, GPS, IMU e um computador de bordo (Jetson/Raspberry Pi) para focar na visão computacional dentro do limite de $5.000.

### O Ataque do "Prosecutor"
O revisor técnico apontou falhas críticas de percepção:
> *"Como seu drone pretende pousar sem um sensor voltado para baixo? Ele pode pousar em cima de um carro ou pedestre. Onde está a cobertura lateral para evitar colisão? Como você detecta fios finos e cabos elétricos só com uma câmera frontal?"*

### O Segundo Erro (Over-Engineering)
Para cobrir os pontos cegos, tentei ajustar a proposta adicionando **8 câmeras estéreo** para fechar uma cobertura omnidirecional. O "Prosecutor" atacou novamente, desta vez focando na física e computação:
> *"Processar 16 fluxos de imagem simultâneos (8 pares estéreo) vai queimar seu Jetson antes mesmo da decolagem. Câmeras estéreo possuem alcance curto (12m) e falham ao detectar fiação fina. Além disso, o peso extra desses sensores e cabos vai esgotar sua bateria em um minuto!"*

### A Mudança de Mentalidade
Percebi que não deveria tentar "inventar a roda" com configurações aleatórias nem sobrecarregar o hardware. Passei a analisar o estado da arte do mercado industrial — especificamente o **Meituan Keeta M-Drone Gen 4** e o **Zipline**.

<p align="center">  
  <img src="/5-day-challenge/76468f88301f3ac7.avif" alt="Comparativo de percepção sob nevoeiro: Câmera vs LiDAR">
</p>

### O Aprendizado do Dia 1
* **LiDARs** fornecem medição de distância e geometria 3D precisas (úteis para fios e galhos).
* **Câmeras** oferecem contexto semântico e cor (mas exigem alto custo de processamento de imagem).
* **RADARs** são insubstituíveis para medir velocidades relativas e operar em clima adverso (chuva, neblina).

mas acima tudo eu entendi que no fundo eu estava refletindo mal e até overthinking essa questao de criar um drone e posicionar os sensores, a ideia mais generica é que vision stack faz parte da automaçao, ela so é pensada depois do drone existir, ou seja é necessario de base ter um drone que pode carregar um certo peso e que funciona manualmente(pilotado) e porque os pilotos precisam pilotar o drone alguns sensores ja vao estar ai desde o principio como cameras por exemplo, talvez so os radares e lidars serao acrestando mas desses so os lidars têm peso preocupante, o que num caso real seria caso de somente trocar por um outro modelo de drone mais potente, entao dito isso eu so precisava dar uma olhada nos drones modelos atuais(DJI, Skydio, Holybro, Autel) saber suas missoes e escolher o modelo carregaria facilemnte a minha vision stack e para delivery
o que devria fazer era ter escolhido um modelo com muito mais embasamento sobre sua pontecia e modo operacional 

Mas e quanto a estrategia de entender um produto fini como M-drone 4L? essa estrategia nao funciona porque se modelo ja é otimizado com computadores e sensores especializados o maximo a estrair daqui é o funcionamento da sua Stack para preception e naviagtion 

nesse sentido como escolher sabiamente o melhor modelo sem saber nada sobre do assunto? 
eu trabalhei muitos anos em callcenters e as formacoes de um produtos duravam entre 2 a 3 dias 
a tecnica consistia em conhecer o catalogo de produtos isso daria uma ideia de como a empresa caloga seus produtos
entao escolhi estudar o catologo de drone da DJI 


#### Configuração Final Escolhida ($4,700)
* **1x GPS ($500):** Posicionado no mastro superior.
* **2x IMUs 6-DoF ($1,000):** Redundância no barramento principal e secundário.
* **1x RADAR ($500 | 150m):** Virado para a frente para tráfego e longo alcance.
* **1x 360° 3D LiDAR Solid-State ($1,000 | 40m):** Inclinado a ~45° para baixo/frente para mapeamento de fiação fina e vegetação.
* **3x Stereo Cameras ($1,800):** 1 voltada para baixo (alinhamento de guincho/winch, altimetria e *Visual Odometry*) e 2 laterais/traseira para navegação em baixa altitude em áreas sem sinal de GPS.
* **1x Monaural Camera ($500):** FPV/telepresença frontal.

---

## Day 2: Escolha do Stack de Algoritmos (Rule-Based vs. End-to-End)

No segundo dia, o desafio foi escolher a arquitetura de controle e software: **Rule-Based (Baseada em Regras/Sistemas Clássicos)** ou **AI-Based / End-to-End**.

<p align="center">  
  <img src="/5-day-challenge/1704e3f929d38dc1.avif" alt="Dilema de algoritmos: Rule-Based vs AI-Based">
</p>

### Minha Escolha: Arquitetura Baseada em Regras (Rule-Based)
Optei pela abordagem determinística (*Rule-Based*) para o MVP do drone de entrega pelos seguintes motivos:

1. **Segurança e Determinismo:** Em logística urbana com guincho (*winch*), falhas de predição de redes neurais ponta-a-ponta (*End-to-End*) são difíceis de auditar. Lógicas determinísticas baseadas em **Máquinas de Estados Finitas (FSM)** garantem comportamento previsível.
2. **Referência da Indústria:** Plataformas de alta confiabilidade física como Boston Dynamics (Spot) e sistemas subaquáticos utilizam pipelines em camadas e controle baseado em estados.

### Algoritmos Propostos no Pipeline
* **Percepção e Fusão:** *Extended Kalman Filter (EKF)* para fusão do GPS, IMUs, Radar e LiDAR; *Visual-Inertial Odometry (VIO)* para navegação redundante sem GPS; e *OctoMap* para conversão da nuvem de pontos do LiDAR em grade de ocupação 3D.
* **Planejamento:** *3D A** para rotas globais e *Vector Field Histogram 3D (VFH3D)* para desvio reativo de obstáculos locais.
* **Regras de Segurança:** Verificação de vento na IMU durante a descida da carga; pausa imediata da entrega se a câmera estéreo inferior detectar movimento na zona de *drop*.

---

## Day 3: Mapeamento de Skills e Mercado de Trabalho

O terceiro dia focou na transição do projeto teórico para as habilidades práticas exigidas pela indústria de Robótica e Visão Computacional.

Analisando ofertas de emprego em robótica autônoma, mapeei as habilidades necessárias para suportar o projeto:

* **Habilidades que eu já possuía/praticava:** Linguagens C++ e Python, visão computacional básica com OpenCV, fundamentos de PyTorch/TensorFlow, integração com microcontroladores (Arduino/ESP32) e ROS/ROS2.
* **Keywords e Conceitos Aprendidos:**
  * **VIO (Visual-Inertial Odometry):** Fusão direta de dados de câmera com IMU de alta taxa.
  * **Sensor Fusion com EKF/UKF:** Algoritmos de estimação de estado em tempo real.
  * **Edge AI Acceleration:** Otimização de modelos para inferência local em hardware embarcado (Jetson Orin/TensorRT) visando baixo consumo energético.

---

## Day 4: Desenhando a Arquitetura do Sistema (System Diagrams)

No quarto dia, integramos todos os aprendizados na construção do diagrama de nós da arquitetura do drone, inspirado nos frameworks open-source de veículos autônomos **Autoware** e **Apollo Auto**.

<p align="center">  
  <img src="/5-day-challenge/architecture1.avif" alt="Exemplo de Diagrama End-To-End">
</p>

<p align="center">  
  <img src="/5-day-challenge/architecture2.avif" alt="Exemplo de Diagrama Rule-Based com múltiplos sensores">
</p>

### Diagrama Conceitual do Drone de Entrega
A arquitetura completa foi dividida em 4 pilares bem definidos: