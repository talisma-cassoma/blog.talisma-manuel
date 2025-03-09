---
title: "Integrated finance control system"
description: "architecting a integrated system to save daily expenses anywhere offline or online"
pubDate: "March 09 2025"
heroImage: "/ourmoneyapp.webp"
badge: "fullstack"
tags: ["api","desktop", "web app"]
---

Hey everyone! I'm excited to finally share a project I've been working on in my spare time: OurMoney, a personal finance tracking app designed for simplicity, efficiency, and a little bit of offline functionality. Let me tell you about it!

### The Problem & My Solution:

Like many of you, I wanted a better way to track my expenses. Spreadsheets felt clunky, and a lot of existing apps were either overloaded with features I didn't need or just weren't flexible enough. I wanted something that could work seamlessly whether I was at my computer or on the go with just my phone, and that wouldn't leave me hanging if my internet connection decided to take a break.

So, I built OurMoney! It's designed to let you easily record your financial transactions, categorize them as income or expenses, and keep everything synchronized. But here's the cool part: it's not just one app. It's actually a project with many apps synchronized!

Two Flavors for Maximum Flexibility:

OurMoney is built as a microservices architecture. That means I have two main parts working together:

Web App (React + Node.js in Docker): This is the version you'd use on your phone or when you're away from your main computer. It runs in a Docker container (because Docker is awesome!), and uses React for the front-end interface and Node.js for the backend API. It's all neatly packaged and ready to run anywhere.
Desktop App (PyQt5 + SQLite): This is the app you'd use on your computer. It's built using PyQt5 (a Python binding for the Qt framework) for a native desktop experience, and SQLite for local data storage.
The beauty of this setup is that both apps talk to the same backend, ensuring that your data is always in sync, even when you're offline.

### Key Features Breakdown:

* Intuitive Interface (Desktop App and Web App): I really focused on making the apps simple and easy to use
* Data Management: For local storage i use SQLite database embedded in the desktop app. This is what allows you to record transactions even without an internet connection.
* Synchronization: A Node.js API that I've deployed on Render (a great platform!) serves as the central hub for your data. The app clearly shows whether a transaction is synced or pending.
* Consistent Timestamps: Ensures every transaction has a createdAt timestamp, avoiding any annoying None values.:
* Pull-and-Push: The core of how the two apps stay in sync. The desktop app pushes any new unsynced data to the server, and then pulls the newest data from the server to keep up to date. This method makes sure you get the new information from one device to the other.
* Manual & Automatic Sync: You can trigger synchronization manually, or it happens automatically in the background.
* Database Suspension Strategy: Includes a strategy to recover from a suspended state (because things happen!).

### Motivation & Future Plans:

My primary motivation was simply to have a better way to track my spending, especially when I'm traveling or just not at my desk. Looking ahead, I have a few ideas for future features:

Analytics and Reporting: Charts and graphs to visualize spending patterns.
Financial Reports: Automatically generated reports for budgeting.
Multi-User Support: Perhaps allowing multiple users on the same account (for families, roommates, etc.).
Why I Built It:

This project was a great opportunity to learn and experiment with different technologies. It was a learning experience with full stack development. Hopefully I'll be able to expand on it in the future and share some of my knowledge with you.

I hope you enjoyed hearing about OurMoney! I'm always open to suggestions, so feel free to leave a comment.