---
title: "Rebuilding produts - Blue River ML stack"
description: "in this article we will try to rebuild Blue river machine learning stack based on the info they share online."
pubDate: "Sep 10 2022"
heroImage: "/bllue_river_stack.webp"
tags: ["ML", "devOps"]
---

Hey everyone! I recently stumbled across some info about how Blue River Technology, a company focused on precision agriculture, handles their machine learning, and I was seriously impressed. They've built a really smart setup for training, deploying, and monitoring their models, all aimed at maximizing performance, reproducibility, and efficiency out there in the fields. Let's dive in!

Building Blocks: Training the Models

Blue River isn't playing around when it comes to training their ML models. They've essentially got two powerhouses running, each with its own purpose:

The Research Lab (On-Premise Muscle): For the initial experimentation and development, they use an on-premise cluster (basically, their own in-house supercomputer). This is managed by something called Slurm, which helps schedule and run all those complex training jobs.
Why On-Premise? Control! They want complete control over their compute resources and the ability to launch thousands of experiments without being limited. Plus, it's more cost-effective in the long run and keeps them independent from relying solely on cloud services. Think of it as their own private playground for AI innovation.
Production Power (Cloud-Based Scalability): When it's time to scale things up and move towards deploying models, they shift to a Kubernetes (K8s) cluster on AWS (Amazon Web Services). This is orchestrated by Argo Workflows, which automates the entire ML pipeline.
Why Kubernetes & Argo? Scalability and automation are the name of the game here. They package their training code using Docker containers and store them in a container registry. This makes it easy to spin up new training instances, manage dependencies, and integrate seamlessly with their CI/CD (Continuous Integration/Continuous Deployment) pipelines. It's all about speed and efficiency!
Getting the Models to the Field: Deployment and Edge Inference

Here's where things get really interesting. Blue River's models aren't just living in the cloud. They need to run on robots out in the fields, in real-time! This means super-low latency is critical.

NVIDIA Jetson AGX Xavier is the hero! The robots leverage NVIDIA Jetson AGX Xavier for optimized performance.
Model Optimization: They optimize their models for these edge devices using TensorRT. This involves a multi-step conversion process: PyTorch JIT (Just-In-Time compilation) → ONNX (Open Neural Network Exchange) → TensorRT Engine.
Why the Conversion? TensorRT, a high-performance deep learning inference optimizer and runtime, doesn't directly support PyTorch JIT models, hence the need for conversion to ONNX format first.
Distribution: These optimized models are stored in Artifactory (a repository manager) and then pushed to the robots using Jenkins CI/CD. Think of it as a continuous delivery pipeline for AI brains to power the machines in the fields.
Keeping an Eye on Things: Monitoring and Reproducibility

Training and deploying models is only half the battle. You also need to know what's going on! Blue River uses Weights & Biases (W&B) for this.

Real-Time Monitoring: W&B gives them real-time insights into training progress, tracking metrics like loss, accuracy, and more.
Experiment Tracking: They use W&B Artifacts to track everything related to their experiments: datasets, trained models, evaluation results. This makes it super easy to reproduce experiments and compare different models.
Pipeline Visualization: W&B also helps them visualize their ML pipelines as DAGs (Directed Acyclic Graphs), making it easier to understand the flow of data and identify bottlenecks.
Why W&B? It's all about reproducibility, organization, and a complete history of their ML pipelines. This ensures they can always understand exactly how a model was trained and deployed.
The Big Picture: Key Benefits

So, what's the bottom line? This stack allows Blue River Technology to:

Achieve High Performance: Train efficiently on-premise and infer quickly on the edge.
Scale Easily: Kubernetes and Argo Workflows automate and scale their workloads.
Automate Deployment: CI/CD with Jenkins and Docker streamlines model deployment.
Maintain Traceability: W&B Artifacts simplify experiment tracking and reproducibility.
Boost Operational Efficiency: TensorRT accelerates inference on the robots.
Final Thoughts

Blue River Technology's ML stack is a great example of how to build a robust and efficient system for deploying AI in the real world. By combining on-premise resources with cloud scalability, optimizing for edge devices, and focusing on traceability, they're able to develop, train, and deploy machine learning models that are truly making a difference in precision agriculture.

What do you think? Any parts of this stack that you're particularly interested in? Let me know in the comments!
