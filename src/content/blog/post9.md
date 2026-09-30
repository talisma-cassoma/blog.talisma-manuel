---
title: "Bringing my emoji character to life"
description: "como criei meu emoji para o app mobile."
heroImage: "/ourmoneyapp_thumb.webp"
pubDate: "September 15 2026"
tags: [ "software architecture", "mobile app", "web", "fullstack"]
draft: true
---

eu eu li um blog do <a href="https://blog.duolingo.com/world-character-visemes/">DUOLINGO</a> a muito tempo atraz sobre como eles automaizaram a animaçao dos personagens, eles usam o conceito de state machine para transitar diferentes formas e assim simular uma animaçao, eles utilisam river para isso, mas meu use-case nao precisa usar do river por ser uma ser muito simples, usar river iria aumentar a complexidade apenas:

## meu use case: 

preciso automatizar a animacao de um emoji eu terei de animar a os olhos e a boca ja tenho os exemplares em animaçao(gif) posso resolver meu case com css e js apenas

<div class="flex w-full flex-wrap gap-4">
<img class="h-40 w-auto" src="/emoji-hero/emoji_correct.gif"    >
<img class="h-40 w-auto" src="/emoji-hero/emoji_defy_devil.gif" >
<img class="h-40 w-auto" src="/emoji-hero/emoji_defy.gif"       >
<img class="h-40 w-auto" src="/emoji-hero/emoji_wait.gif"       >
<img class="h-40 w-auto" src="/emoji-hero/emoji_wrong.gif"      >
</div>

ref:
<a href="https://www.youtube.com/watch?v=AqJKAJ0TKms">Criando um PWA com React Native & Expo Web | Code/Drops #34</a>
<a herf="https://johnywalves.com.br/entendo-tags-desenhando-formas-svg/">Entendendo tags e gerando formas em SVG</a>