---
title: "myKIDS a mobile for kids to have fun"
description: ""
heroImage: "/post10/mykidsapp_thumb.png"
pubDate: "April 15 2026"
tags: [ "software architecture", "mobile app", "web", "fullstack"]
draft: false
---

My son was having some difficulties learning the Arabic language. After analyzing the situation, my wife and I realized that his limited vocabulary was the primary obstacle. To guide and support him effectively, we started designing Duolingo-style exercises tailored specifically to his needs.

That inspired me to build a dedicated mobile application where I could create new lessons, customize learning games through an admin account, and leverage local data storage so the app works completely offline. I successfully developed the app and installed the <b>.apk</b> onto our tablet for him to use. Just click <a target="_blank" href="https://drive.google.com/file/d/1RLquKIayRkqOMZZz9fpWtUgVXrweF2jM/view?usp=sharing">here</a> to download. If you're a developer, check out the <a target="_blank" href="https://github.com/talisma-cassoma/mykids">GitHub repo of the project</a>—don't forget to star the project, please, it would help a lot! 😉

We liked the idea so much that I started building the app for both of my children: my little princess and my big boy, Dino. 

---

## Character Design & Art Style

I drew the characters myself because I wanted something unique. I tried to create them with AI, but it couldn't capture the exact look I was aiming for. 

The characters are constructed primarily from **geometric shapes** (rectangles, triangles, and circles) with soft, rounded corners. To maximize their childish and friendly appeal, I gave them oversized features paired with expressive cartoon emotions. 

To mimic the charm of a real hand-drawn illustration on physical paper, the characters use a warm colored pencil aesthetic layered with subtle grainy textures.

<div class="content-split" style="display: flex; flex-wrap: wrap; gap: 2rem; margin: 2rem 0;">
  <!-- Left Column / Image 1 -->
  <div style="flex: 1 1 300px; display: flex; justify-content: center;">
    <img src="/post10/ref1.png" style="width: 100%; max-width: 450px; height: auto;" alt="Character design concept sketch" />
  </div>

  <!-- Right Column (Text + Image 2) - Forced Side-by-Side -->
  <div style="flex: 1 1 300px; display: flex; flex-direction: column; flex-wrap: nowrap; gap: 1.5rem; align-items: center;">
    <div style="flex: 1;">
      <p style="margin: 0;">For navigation, I wanted <b>Gamified UI map paths</b>—similar to the node-based progression tree famously used in the <a target="_blank" href="https://www.duolingo.com">Duolingo</a> app. To bring this to life, I integrated isometric UI assets inspired by designs like <b><a target="_blank" href="https://tylereldridgedesigns.com/betterfly">betterfly</a></b>.</p>
    </div>
    <div style="flex: 1;">
      <img src="/post10/ref2.png" alt="Duolingo style path UI reference" style="width: 16rem; height: auto; border-radius: 8px;" />
    </div>
  </div>
</div>

---

## Meet the Characters

<img src="/post10/characters.png" alt="Princess character references" style="width: 4rem%; height: auto; border-radius: 8px;">

<p>It took some time to find the right references to bring my vision to life. During the process, you often know what you want in your head, but struggle to represent it graphically. I feel like I've finally caught a glimpse of it even if I'm still tweaking a few details to get it exactly where I want it but I'm really proud of what I've created so far.</p> 

<div style="display: flex; justify-content: space-between; align-items: center; margin: 2rem 0;">
    <h3 style="margin: 0;">The Princess Girl</h3>
    <p style="margin: 0; color: #666;">References</p>
</div>
<img src="/post10/ref3.png" alt="Princess character references" style="width: 100%; height: auto; border-radius: 8px;">

<div style="display: flex; align-items: center; gap: 1.5rem; margin: 1rem 0; flex-wrap: wrap;">
  <div style="display: flex; align-items: center; gap: 0.5rem;">
    <div style="width: 24px; height: 24px; border-radius: 50%; background-color: #B76B47; border: 1px solid rgba(0,0,0,0.1);"></div>
    <span style="font-size: 0.9rem;">Skin: #B76B47</span>
  </div>
  <div style="display: flex; align-items: center; gap: 0.5rem;">
    <div style="width: 24px; height: 24px; border-radius: 50%; background-color: #F8B041; border: 1px solid rgba(0,0,0,0.1);"></div>
    <span style="font-size: 0.9rem;">Crown: #F8B041</span>
  </div>
  <div style="display: flex; align-items: center; gap: 0.5rem;">
    <div style="width: 24px; height: 24px; border-radius: 50%; background-color: #773AB3; border: 1px solid rgba(0,0,0,0.1);"></div>
    <span style="font-size: 0.9rem;">Dress: #773AB3</span>
  </div>
</div>

<div style="display: flex; justify-content: space-between; align-items: center; margin: 2rem 0;">
    <h3 style="margin: 0;">The Boy in Dino Suit</h3>
    <p style="margin: 0; color: #666;">References</p>
</div>
<img src="/post10/ref4.png" alt="Dino boy character references" style="width: 100%; height: auto; border-radius: 8px;">

<div style="display: flex; align-items: center; gap: 1.5rem; margin: 1rem 0; flex-wrap: wrap;">
  <div style="display: flex; align-items: center; gap: 0.5rem;">
    <div style="width: 24px; height: 24px; border-radius: 50%; background-color: #B76B47; border: 1px solid rgba(0,0,0,0.1);"></div>
    <span style="font-size: 0.9rem;">Boy Skin: #B76B47</span>
  </div>
  <div style="display: flex; align-items: center; gap: 0.5rem;">
    <div style="width: 24px; height: 24px; border-radius: 50%; background-color: #168773; border: 1px solid rgba(0,0,0,0.1);"></div>
    <span style="font-size: 0.9rem;">Main Dino: #168773</span>
  </div>
  <div style="display: flex; align-items: center; gap: 0.5rem;">
    <div style="width: 24px; height: 24px; border-radius: 50%; background-color: #13574A; border: 1px solid rgba(0,0,0,0.1);"></div>
    <span style="font-size: 0.9rem;">Skin Spots: #13574A</span>
  </div>
  <div style="display: flex; align-items: center; gap: 0.5rem;">
    <div style="width: 24px; height: 24px; border-radius: 50%; background-color: #13574A; border: 1px solid rgba(0,0,0,0.1);"></div>
    <span style="font-size: 0.9rem;">Belly & Nails: #13574A</span>
  </div>
</div>


---

## How Are Lessons Schematized?

To keep learning structured yet engaging, I organize lessons around **4 core pillars** that represent a complete learning module:

1. **Learn:** Core lesson delivery through introductory videos or explanatory text cards.
2. **Try:** Guided practice exercises to reinforce new vocabulary.
3. **Test:** Evaluation checkpoints where performance results are recorded for progress statistics.
4. **Play:** Mini runner-style games designed to keep the child motivated.

<div style="display: flex; align-items: center; justify-content: center; gap: 1.5rem; margin: 1rem 0; flex-wrap: wrap;">
<img src="/post10/4pillars.png" alt="The 4 learning pillars schema" style="width: 100%; height: auto; border-radius: 8px; margin: 1rem 0;">

<img src="/post10/module.png" alt="Module structure overview" style="width: 60%; height: auto; border-radius: 8px; margin: 1rem 0;">
</div>


The frist version of the app:

<div style="display: flex; justify-content: center; align-items: center; margin: 2rem auto; width: 100%;">
  <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7458532723020914689?compact=1" height="399" width="504" frameborder="0" allowfullscreen="" title="Post intégré"></iframe>
</div>

---

### References & Further Reading:
* <a target="_blank" href="https://github.com/talisma-cassoma/mykids">GitHub repo of the project</a> — don't forget to star the project please, it would help a lot! 😉
* <a target="_blank" href="https://blog.duolingo.com/learning-other-writing-systems/">Tools for learning to read other writing systems</a>
* <a target="_blank" href="https://tylereldridgedesigns.com/betterfly">Tyler Eldridge betterfly UI design</a>