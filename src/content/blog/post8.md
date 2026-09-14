---
title: "resolvendo o problema de registro de dados"
description: "criando um app para iphone sem publicar na apple store."
heroImage: "/ourmoneyapp_thumb.webp"
pubDate: "September 08 2026"
tags: ["PWA", "software architecture", "mobile app", "web", "fullstack"]
draft: true
---

eu ja criei um app pra desktop para gestao das minhas finanças(<a href="/blog/integrated-finance-control-system">mais detalhes aqui</a>) incluse desenvolivi um web app com o backend hospdado no render mas eu sou o unico que usa app desktop e a API no hospedada no render está quase sempre offline devido o could refresh do free tier

entao deixe apresentar a problematica aqui:
preciso que a minha mulher possa registrar dados de consumo financeiro a partir do seu iphone:
ela nao tem muita paciencia, entao pra isso so audio ou foto vai resultar como input porque escrever ela vai se aborrecer
eu preciso de uma soluçao em que ela pode anotar mesmo offiline e que ela possa ter acesso logo pela na sua tela inicial senao ela vai esquecer 

contrantes:
o iphone nao permite intalçao de app fora da apple store( é necssario pagar um conta dev apple para poder publicar um app na apple store)

solucoes possiveis:

- [ ] criar um bot pra coleta de dados via whatsapp(ou telegram) 
- [x] criar pwa para instalar no seu iphone 

eu escolhi o pwa como expo, e aqui vai um adendo eu poderia apenas criar um pwa com nextjs(seria a soluçao menos trabalhosa)  mas preferi usar expo mesmo ja que ele tambem oferece os mesmo recursos e para ganhar experiencia nesse tipo de soluçao pois nao petendo pagar para pubicar meus projetos apple store por um bom tempo :D


ref:
<a href="https://www.youtube.com/watch?v=AqJKAJ0TKms">Criando um PWA com React Native & Expo Web | Code/Drops #34</a>