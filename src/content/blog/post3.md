---
title: "building my AI plant assistent"
description: "From train to autameted deploy, An E2E strategy for training and deploying plant disease detection AI models."
heroImage: "/plant_disease_detection_proj_preview.webp"
pubDate: "March 03 2025"
tags: ["machine learning", "devops", "data analysis"]
---



Imagine a world where you could instantly identify plant diseases with your phone. That was my vision, and i started training effective models and devoloping a mobile app for it. But the reality of manually labeling images, tweaking models, and deploying apps was much more time-consuming than I anticipated.

My workflow was a scattered mess: labeling images, training models in Colab, converting them, and then struggling to integrate them into my mobile app.  The constant iteration felt like a Sisyphean task.

That's why I set out to build an end-to-end automated system that would handle everything from data labeling to model deployment, freeing me to focus on the core AI research.

## The Vision: Why Automate?

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

Whether you're a researcher, hobbyist, or developer, this approach can help you build and deploy AI-powered solutions more efficiently.
<img src="/mobile_app.webp" align="center">
<!-- 
## The E2E Strategy: Building Blocks of the AI Plant Assistant

*   **High-Level Overview:** 
<img src="#" alt="Provide a diagram or visual representation of your entire workflow.This will help readers understand the big picture. Consider using a flow chart"/>

### Data Labeling & Management:
anotation app -> google drive

### Model Training & Monitoring:
Google Colab -> Weights & Biases (W&B)

### Build Automation: EAS (Expo Application Services)
mobile app 
CI/CD pipeline with GitHub Actions

## Challenges and Lessons Learned

*   **Be honest about the difficulties you encountered:**  What were the biggest roadblocks in your journey?
*   **Share your solutions and lessons learned:**  What did you learn from these challenges?  What would you do differently next time?
*   **Examples:**
    *   "Optimizing model size for mobile deployment was a major hurdle.  I had to experiment with different quantization techniques to reduce the model size without sacrificing too much accuracy."
    *   "Setting up the CI/CD pipeline with GitHub Actions was initially complex, but it's been a huge time-saver in the long run.  I learned the importance of thoroughly testing my workflows before relying on them." -->
