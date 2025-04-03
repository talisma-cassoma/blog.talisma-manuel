---
title: "Rebuilding produts - Blue River ML stack"
description: "in this article we will try to rebuild Blue River machine learning stack based on the info they share online."
pubDate: "March 18 2025"
heroImage: "/bllue_river_stack.webp"
tags: ["machine learning", "devops", "data analysis"]
---

I recently came across some fascinating insights into how **Blue River**, a company specializing in **precision agriculture**, approaches **machine learning(ML)** and I was seriously impressed. They've built a highly efficient system for **training, deploying, and monitoring ML models**, all designed to **maximize performance, reproducibility, and efficiency in the field**. Let’s dive in!  

**But how they train and deploy AI Models?** 

Their mission is to **train and deploy AI models that detect (locate in real-time camera frames) crops and weeds**. 
For an agricultural system that needs to spray only the weeds, it needs to do it in Real time and as precise as possible to spray only the weeds and nothing else!

Since these models need to be both **accurate and lightweight**, they’ve **divided their workflow into two key parts**:  
    

1. **Research Workflow** – Focused on developing and experimenting with new ML models. They run experiments on their **on-premise cluster**, using **Slurm** to manage multiple jobs efficiently.  
2. **Production Workflow** – Dedicated to optimizing the best research models for **real-time inference** on their farming machines. This involves converting models to **efficient formats (ONNX, TensorRT)** and deploying them on the **NVIDIA Jetson AGX Xavier** inside their **AutoTrac** system.  

Let’s take a deeper look at both workflows.  

### Research Workflow  

Blue River’s **Research Lab** operates an **on-premise computing cluster** (essentially their own supercomputer) to train models. They use **Slurm** for scheduling and managing complex training jobs, think of it as Kubernetes for High-Performance Computing (HPC).  

Here’s a breakdown of their **machine learning stack**:  

- **PyTorch**: They develop their custom models using PyTorch (which is a great choice YOLOv5 was also built using PyTorch ! spoiler alert: i'll be using this architecture for demo).  
- **Weights & Biases (W&B)**: For experiment tracking, monitoring, and collaboration.  
- **ONNX & TensorRT**: For model optimization and deployment on edge devices(the NVIDIA Jetson AGX Xavier).  

I got so excited reading about their system that I **rebuilt their ML stack** in a project! Check out my repo **[here](https://github.com/talisma-cassoma/Rebuilding-ML-Stack)**.  

### How I recreated this without a Supercomputer? 

Since I **don’t have access to an HPC cluster** and **don’t want to pay for cloud GPUs**, I came up with this approach:  

1. **Train different YOLO models** on Google Colab using the free GPUs.  
2. **Monitor training** with **W&B**.  
3. **Save the trained PyTorch model(.pt)** in **W&B Artifacts**.  
4. **Download the model (.pt) locally** and convert it to **ONNX** on my PC.  
5. **Package the ONNX model into an inference API (Flask) inside a Docker container**.  
6. **Deploy the Docker container on a local Kubernetes cluster**.  

### Data Analysis & Model Training Monitoring 

In my repo **[here](https://github.com/talisma-cassoma/Rebuilding-ML-Stack)**, I trained various models using the **[Crop and Weed Detection dataset](https://universe.roboflow.com/crop-detection-uq1hb/crop-and-weed-detection-xer8u)** from **Roboflow**.  

However, **training and deploying models is only half the battle**, you also need to monitor their performance. **Blue River Technology uses W&B for this**, and I found it incredibly useful.  

Let’s be honest **developing a custom web app from scratch just to monitor training runs** would be **painful, time-consuming, and expensive**. W&B **solves this problem effortlessly** by providing:  

- **Real-time tracking** of metrics like loss, accuracy, and mAP.  
- **Experiment logging** for easy model comparison.  
- **Pipeline visualization** (DAGs) to track the entire ML workflow.  

I used W&B in my project, and it helped me understand why so many **machine learning teams** and **data science teams** rely on it. I chose to use YOLOv5 instead of building a PyTorch model from scratch for a faster setup and to get straight to the point. Additionally, its native integration with W&B saved me time. 

Take look here to my **W&B monitoring dashboard** below      
<p align="center">  
  <img src="/WandB_models_training_infos.webp" alt="yolov5 tainning monitoring dashboard">
  <em>monitoring dashboard</em> 
</p>  

In Blue River, they also use **W&B Artifacts** to track the datasets used in training, trained model configurations, and evaluation results. This makes **experiment reproducibility much easier** and **ensures that teams always know how a model was trained and deployed, allowing for seamless sharing across teams**, all within one software. as you can see here:

<p align="center">  
  <img src="/WandB_models_registry.webp" alt=" saved models in W&B">  
  <em>saved models in W&B</em> 
</p>  

Check out the training **Colab notebook** **[here](https://github.com/talisma-cassoma/Rebuilding-ML-Stack/blob/main/plant_detection_train_and_monitoring.ipynb)** to see how I replicated this setup.  

### Inference Pipeline: Deploying Models on AutoTrac 

So, how do these models actually get deployed on **AutoTrac** (their AI-driven farming robot)?  

Here’s the **Blue River deployment pipeline**:  

The **PyTorch JIT** (Just-In-Time compilation ) trained models(the best i think) are converted to **ONNX format**, and from there they use **TensorRT** to convert to a TensorRT engine file, those models should be saved on **Artifactory** using a **Jenkins CI/CD pipeline**. For containers they use **Docker** and **kubernetes clusters**.They also utilize an Argo workflow on top of a **Kubernetes (K8s) cluster** hosted in **AWS**. For example, the PyTorch training services are deployed to the cloud using Docker.

In my case, I recreated this pipeline locally:  

- **All trained models (yolov5) on colab are stored in W&B Artifacts**.  
- **I built a microservice that automatically converts these models from W&B Artifacts into ONNX format**.  
- **I also built other micro service, a Flask API designed to serve the models and handle inference requests, it runs inside a Docker container managed by Kubernetes**.

<p align="center">  
  <img src="/deploy_pipeline.webp" alt="the deploy workflow">  
  <em>my deploy workflow</em> 
</p>
Lets explain i what i did:

I set up a **Continuous Integration (CI) pipeline** using **GitHub Actions**. You know, a generic setup, on each commit in the main brunch the pipeline automatically builds the Flask API into a Docker container. It then pushes the container to **Docker Hub**, where it can be accessed by other environments. This automation ensures that the API is always up-to-date, with no manual intervention needed.

Finally, to deploy the API at scale, I turned to Kubernetes. On my local Kubernetes cluster, I configured it to pull the latest Docker container from Docker Hub and deploy it as a scalable service. Kubernetes handles scaling, load balancing, and managing the service, making sure the inference API is always available and ready to serve predictions. The code lays in [repository](https://github.com/talisma-cassoma/Rebuilding-ML-Stack).

<h3 class="flex items-center gap-1"> Final Thoughts: <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#00B37E"><path d="M480-80q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q48 0 93.5 11t87.5 32q15 8 19.5 24t-5.5 30q-10 14-26.5 18t-32.5-4q-32-15-66.5-23t-69.5-8q-134 0-227 93t-93 227q0 134 93 227t227 93q26 0 51-4t50-12q17-5 33-.5t25 19.5q8 14 3.5 30T622-105q-34 13-70 19t-72 6Zm280-200h-80q-17 0-28.5-11.5T640-320q0-17 11.5-28.5T680-360h80v-80q0-17 11.5-28.5T800-480q17 0 28.5 11.5T840-440v80h80q17 0 28.5 11.5T960-320q0 17-11.5 28.5T920-280h-80v80q0 17-11.5 28.5T800-160q-17 0-28.5-11.5T760-200v-80ZM424-408l372-373q11-11 28-11t28 11q11 11 11 28t-11 28L452-324q-12 12-28 12t-28-12L282-438q-11-11-11-28t11-28q11-11 28-11t28 11l86 86Z"/></svg>
</h3> 

**Blue River Technology’s ML stack is an excellent example** of how to **efficiently train, deploy, and monitor AI models for real-world applications**. Their setup ensures:  

<ul class="liste max-w-screen-lg grid grid-cols-1 sm:grid-cols-[repeat(2,minmax(min-content,auto))] items-center">
    <div>
       <p class="flex gap-1 items-center">
            <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#00B37E">
                <path
                    d="m424-408-86-86q-11-11-28-11t-28 11q-11 11-11 28t11 28l114 114q12 12 28 12t28-12l226-226q11-11 11-28t-11-28q-11-11-28-11t-28 11L424-408Zm56 328q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-80q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 134 93 227t227 93Zm0-320Z" />
            </svg>
            <b>Scalability</b>
        </p>
    </div>
    <span>: Combining on-premise resources with cloud infrastructure.</span>
    <div>
       <p class="flex gap-1 items-center">
            <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#00B37E">
                <path
                    d="m424-408-86-86q-11-11-28-11t-28 11q-11 11-11 28t11 28l114 114q12 12 28 12t28-12l226-226q11-11 11-28t-11-28q-11-11-28-11t-28 11L424-408Zm56 328q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-80q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 134 93 227t227 93Zm0-320Z" />
            </svg>
            <b>Optimization</b>
        </p>
    </div>
    <span>: Using ONNX & TensorRT for edge AI performance.</span>
    <div>
       <p class="flex gap-1 items-center">
            <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#00B37E">
                <path
                    d="m424-408-86-86q-11-11-28-11t-28 11q-11 11-11 28t11 28l114 114q12 12 28 12t28-12l226-226q11-11 11-28t-11-28q-11-11-28-11t-28 11L424-408Zm56 328q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-80q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 134 93 227t227 93Zm0-320Z" />
            </svg>
            <b>Reproducibility</b>
        </p>
    </div>
    <span>: Keeping a full history of every experiment with W&B.</span>
    <div>
       <p class="flex gap-1 items-center">
            <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#00B37E">
                <path
                    d="m424-408-86-86q-11-11-28-11t-28 11q-11 11-11 28t11 28l114 114q12 12 28 12t28-12l226-226q11-11 11-28t-11-28q-11-11-28-11t-28 11L424-408Zm56 328q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-80q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 134 93 227t227 93Zm0-320Z" />
            </svg>
            <b>Automation</b>
        </p>
    </div>
    <span>: Streamlining deployment with Kubernetes and Argo Workflows.</span>
</ul>


By following a similar approach, I was able to **rebuild this stack using free and local resources** a great way to **experiment with real-world ML deployment**.  

**What do you think?**  Any part of this stack that interests you the most?  

<h3 class="flex items-center gap-1"> sources <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#00B37E"><path d="M200-800v241-1 400-640 200-200Zm0 720q-33 0-56.5-23.5T120-160v-640q0-33 23.5-56.5T200-880h287q16 0 30.5 6t25.5 17l194 194q11 11 17 25.5t6 30.5v28q0 17-11.5 28T720-540q-17 0-28.5-11.5T680-580v-20H520q-17 0-28.5-11.5T480-640v-160H200v640h220q17 0 28.5 11.5T460-120q0 17-11.5 28.5T420-80H200Zm460-120q42 0 71-29t29-71q0-42-29-71t-71-29q-42 0-71 29t-29 71q0 42 29 71t71 29ZM892-68q-11 11-28 11t-28-11l-80-80q-21 14-45.5 21t-50.5 7q-75 0-127.5-52.5T480-300q0-75 52.5-127.5T660-480q75 0 127.5 52.5T840-300q0 26-7 50.5T812-204l80 80q11 11 11 28t-11 28Z"/></svg>
</h3>

Blue River posts:

* https://medium.com/pytorch/ai-for-ag-production-machine-learning-for-agriculture-e8cfdb9849a1
* https://developer.nvidia.com/blog/how-ai-and-robotics-are-driving-agricultural-productivity-and-sustainability/

Dataset:
* https://universe.roboflow.com/crop-detection-uq1hb/crop-and-weed-detection-xer8u