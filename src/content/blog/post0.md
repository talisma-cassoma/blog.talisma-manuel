---
title: "Building My AI Plant Assistant: An E2E Journey"
description: "From initial training to automated deployment, discover my E2E strategy for developing and deploying AI models for plant disease detection. Learn about data labeling, model optimization, and mobile app integration."
heroImage: "/plant_disease_detection_proj_thumb.webp"
pubDate: "March 03 2025"
tags: ["machine learning", "devops", "mobile app development", "AI", "automation"]
---

Imagine being able to diagnose plant diseases instantly, right from your smartphone. That was my initial spark – to create a mobile app powered by AI that could identify plant ailments with a simple photo. The dream was clear, involving training effective models and developing a user-friendly mobile application. However, the reality of manually labeling countless images, painstakingly tweaking model parameters, and wrestling with app deployment proved far more time-consuming and complex than I initially anticipated.

My initial workflow felt chaotic: manually labeling images, training models using Google Colab, converting them to mobile-friendly formats, and then struggling to integrate them seamlessly into my React Native mobile app. This iterative process felt like a never-ending cycle, a true Sisyphean task.

That's why I embarked on a mission to build a fully automated, end-to-end(E2E) system.  The goal was to automate everything from data labeling and versioning to model training, optimization, and deployment. This would free me to focus on the core AI research and development, rather than getting bogged down in repetitive, manual tasks.

### The Vision: Why Automate Plant Disease Detection?

My core reasons for investing time into this automation:

<ul class="liste max-w-screen-lg grid gap-5 grid-cols-1 sm:grid-cols-[repeat(2,minmax(min-content,auto))] items-center">
    <div >
        <p class="flex gap-1 items-center">
            <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#00B37E"><path d="m424-408-86-86q-11-11-28-11t-28 11q-11 11-11 28t11 28l114 114q12 12 28 12t28-12l226-226q11-11 11-28t-11-28q-11-11-28-11t-28 11L424-408Zm56 328q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-80q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 134 93 227t227 93Zm0-320Z"/></svg> 
            <b>Faster Iteration</b>
        </p>
    </div>
    <span>: Experiment with new architectures and hyperparameters without the burden of manual deployment.</span>
    <div >
        <p class="flex gap-1 items-center">
            <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#00B37E"><path d="m424-408-86-86q-11-11-28-11t-28 11q-11 11-11 28t11 28l114 114q12 12 28 12t28-12l226-226q11-11 11-28t-11-28q-11-11-28-11t-28 11L424-408Zm56 328q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-80q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 134 93 227t227 93Zm0-320Z"/></svg> 
            <b>Improved Accuracy</b>
        </p>
    </div>
    <span>: By streamlining the process, I could focus on improving model accuracy and robustness.</span>
    <div >
        <p class="flex gap-1 items-center">
            <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#00B37E"><path d="m424-408-86-86q-11-11-28-11t-28 11q-11 11-11 28t11 28l114 114q12 12 28 12t28-12l226-226q11-11 11-28t-11-28q-11-11-28-11t-28 11L424-408Zm56 328q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-80q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 134 93 227t227 93Zm0-320Z"/></svg> 
            <b>Scalability</b>
        </p>
    </div>
    <span>: This automated system allows me to easily scale up my data and model development efforts.</span>
</ul>

Whether you're a seasoned researcher, a passionate hobbyist, or a budding developer, this E2E approach can empower you to build and deploy AI-powered solutions more efficiently and effectively. The principles I've applied here are broadly applicable to other AI-driven projects as well.

Here's a sneak peek at how the app currently looks:

<p align="center">  
<img src="/mobile_app.webp" align="center" alt="Screenshot of the mobile plant disease detection app">
<em>Screenshot of the AI-powered mobile app</em>
</p>


<h3 class="flex items-center gap-1">  The E2E Strategy
<svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#00B37E"><path d="M314-115q-104-48-169-145T80-479q0-26 2.5-51t8.5-49l-46 27-40-69 191-110 110 190-70 40-54-94q-11 27-16.5 56t-5.5 60q0 97 53 176.5T354-185l-40 70Zm306-485v-80h109q-46-57-111-88.5T480-800q-55 0-104 17t-90 48l-40-70q50-35 109-55t125-20q79 0 151 29.5T760-765v-55h80v220H620ZM594 0 403-110l110-190 69 40-57 98q118-17 196.5-107T800-480q0-11-.5-20.5T797-520h81q1 10 1.5 19.5t.5 20.5q0 135-80.5 241.5T590-95l44 26-40 69Z"/></svg>
</h3>
Here's a breakdown of the key building blocks that make up my automated AI plant assistant:

<!--img src="#" alt="Provide a diagram or visual representation of your entire workflow.This will help readers understand the big picture. Consider using a flow chart"/-->

Let's dive into the details of each component:

With this automation pipeline, I can simply label images using the annotation tool, and as soon as I save my work, a new version of my dataset is automatically uploaded to my Google Drive and store a reference of those artifacts in W&B. I'm employing a data persistence strategy, meaning only the modifications (newly labeled images, deletions, or replacements) are uploaded, which significantly saves time and bandwidth.

For monitoring my training progress, I've adapted the strategy used by Blue River Technology (now part of John Deere). You can find a detailed explanation of how I replicated their approach in [this article](/blog/rebuilding-products---blue-river-ml-stack). In short, I leverage **Weights & Biases (W&B)** for comprehensive experiment tracking and visualization.

The best-performing models, determined by an **F1 score** evaluation, are then prepared for production. This involves converting them to efficient, lite models optimized for mobile deployment and storing them as artifacts within W&B. Finally, the mobile app retrieves the selected model artifact to perform real-time inference on device.

**Alright, enough talk! SHOW ME THE CODE (and the specifics)!**

Yes, let's get into the code and the implementation details :D

<h3 class="flex items-center gap-1"> Data Labeling & versioning: 
<svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#00B37E"><path d="M680-80v-120H560v-80h120v-120h80v120h120v80H760v120h-80ZM200-200v-200h80v120h120v80H200Zm0-360v-200h200v80H280v120h-80Zm480 0v-120H560v-80h200v200h-80Z"/></svg>
</h3>

For image annotation, I'm using an open-source [sreeni image-annotator](https://github.com/sreeninet/image-annotator), a Qt-based GUI application (kudos to the developer for their great work!) under MIT licence. I've made some modifications to automatically upload every new version of the labeled dataset to my Google Drive integrated with W&B. This Google Drive integration serves as a central repository for the images, registries like segmented region or bounded box localization on the image are saved in database and yml file for each version.  I then use W&B Artifacts to version control these datasets.  Whenever a new set of annotations is uploaded to Google Drive, a script is triggered to create a new W&B Artifact, linking to the data in Google Drive.  This provides a robust, auditable history of my training data.

<h3 class="flex items-center gap-1"> Model Training & Monitoring: 
<svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#00B37E"><path d="M80-120v-80h800v80H80Zm40-120v-280h120v280H120Zm200 0v-480h120v480H320Zm200 0v-360h120v360H520Zm200 0v-600h120v600H720Z"/></svg>
</h3>


Fine-tuning models and experimenting with new techniques to achieve the best possible results is the core of the project.

My model training process is primarily executed within Google Colab for its accessibility and free GPU resources.  I use a variety of techniques including transfer learning, data augmentation, and custom loss functions, all with the goal of maximizing the accuracy and robustness of my plant disease detection models.

**W&B is indispensable for this phase.** I track every experiment meticulously, logging key metrics like **accuracy, precision, recall, F1-score, and loss curves**.  I also log visualizations of the model's predictions on a validation set, which helps me identify areas where the model is struggling.


<h3 class="flex items-center gap-1"> Challenges and Lessons Learned: <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#00B37E"><path d="M480-80q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q48 0 93.5 11t87.5 32q15 8 19.5 24t-5.5 30q-10 14-26.5 18t-32.5-4q-32-15-66.5-23t-69.5-8q-134 0-227 93t-93 227q0 134 93 227t227 93q26 0 51-4t50-12q17-5 33-.5t25 19.5q8 14 3.5 30T622-105q-34 13-70 19t-72 6Zm280-200h-80q-17 0-28.5-11.5T640-320q0-17 11.5-28.5T680-360h80v-80q0-17 11.5-28.5T800-480q17 0 28.5 11.5T840-440v80h80q17 0 28.5 11.5T960-320q0 17-11.5 28.5T920-280h-80v80q0 17-11.5 28.5T800-160q-17 0-28.5-11.5T760-200v-80ZM424-408l372-373q11-11 28-11t28 11q11 11 11 28t-11 28L452-324q-12 12-28 12t-28-12L282-438q-11-11-11-28t11-28q11-11 28-11t28 11l86 86Z"/></svg></h3>

As fulls-tack developper, I usualy develop software features, web apps, server API-based applications, Setting up all this asked me too much devops skills, it took me time to understand those different concepts and assemble the knowledge Ineed to build this solution.
it made me see datasets processing differently, like how to avoid and reduce data processing. i've spent too long exploring yolo repositories to take insights Ialso learn some react natives pratices and APIs.
Optimizing model size for mobile deployment was a major hurdle.  I had to experiment with different quantization techniques to reduce the model size without sacrificing too much accuracy, It was hard and complex but it's been a huge time-saver in the long run.