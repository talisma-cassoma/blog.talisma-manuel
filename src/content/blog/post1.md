---
title: "Rebuilding produts - Blue River ML stack"
description: "in this article we will try to rebuild Blue river machine learning stack based on the info they share online."
pubDate: "March 09 2025"
heroImage: "/bllue_river_stack.webp"
tags: ["Machine Learning", "DevOps", "Data Analysis"]
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
  <img src="/WandB_models_training_infos.png" alt="yolov5 tainning monitoring dashboard">
  <em>Caption: monitoring dashboard</em> 
</p>  

In Blue River, they also use **W&B Artifacts** to track the datasets used in training, trained model configurations, and evaluation results. This makes **experiment reproducibility much easier** and **ensures that teams always know how a model was trained and deployed, allowing for seamless sharing across teams**, all within one software. as you can see here:

<p align="center">  
  <img src="/WandB_models_registry.png" alt=" saved models in W&B">  
  <em>Caption: saved models</em> 
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
  <img src="/deploy_pipeline.png" alt="the deploy workflow">  
  <em>Caption: my deploy workflow</em> 
</p>
Lets explain i what i did:

I set up a **Continuous Integration (CI) pipeline** using **GitHub Actions**. You know, a generic setup, on each commit in the main brunch the pipeline automatically builds the Flask API into a Docker container. It then pushes the container to **Docker Hub**, where it can be accessed by other environments. This automation ensures that the API is always up-to-date, with no manual intervention needed.

Finally, to deploy the API at scale, I turned to Kubernetes. On my local Kubernetes cluster, I configured it to pull the latest Docker container from Docker Hub and deploy it as a scalable service. Kubernetes handles scaling, load balancing, and managing the service, making sure the inference API is always available and ready to serve predictions. The code lays in [repository](https://github.com/talisma-cassoma/Rebuilding-ML-Stack).

## **Final Thoughts 💡**  

**Blue River Technology’s ML stack is an excellent example** of how to **efficiently train, deploy, and monitor AI models for real-world applications**. Their setup ensures:  

✅ **Scalability** – Combining on-premise resources with cloud infrastructure.  
✅ **Optimization** – Using ONNX & TensorRT for edge AI performance.  
✅ **Reproducibility** – Keeping a full history of every experiment with W&B.  
✅ **Automation** – Streamlining deployment with Kubernetes and Argo Workflows.  

By following a similar approach, I was able to **rebuild this stack using free and local resources** a great way to **experiment with real-world ML deployment**.  

**What do you think?**  Any part of this stack that interests you the most?  

### sources: 

Blue river posts:

* https://medium.com/pytorch/ai-for-ag-production-machine-learning-for-agriculture-e8cfdb9849a1
* https://developer.nvidia.com/blog/how-ai-and-robotics-are-driving-agricultural-productivity-and-sustainability/

Dataset:
* https://universe.roboflow.com/crop-detection-uq1hb/crop-and-weed-detection-xer8u