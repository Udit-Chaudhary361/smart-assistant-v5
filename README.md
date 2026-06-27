# Smart Assistant V5 🌐🤖

A Personal Assistant built with **Python, Flask, and SQLite**, transforming the previous terminal-based assistant into a web application while preserving its modular architecture.

## Features

* User Management (Set Name, View Name)
* Task Management (CRUD)
* Notes Management (CRUD)
* Task Statistics
* Random Joke Generator
* Logging System
* Command History Tracking
* Persistent Storage using SQLite Database
* Web Interface built with Flask
* Modular Design using Packages

## What's New in V5

* Converted the terminal-based assistant into a Flask web application.
* Replaced command-line interaction with a browser-based interface.
* Integrated Flask routes with the existing business logic.
* Used Jinja templates to render dynamic pages.
* Preserved the existing SQLite database and modular architecture.
* Established a foundation for future AI and LLM integration.

## Tech Stack

* Python
* Flask
* SQLite
* SQL
* HTML
* Jinja Templates
* File Handling
* OOP Design

## Project Structure

```text
smart_assistant_v5/
│
├── app/
│   ├── database.py
│   ├── logger.py
│   └── tools/
│       └── joke_tool.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── notes.html
│   ├── tasks.html
│   ├── history.html
│   └── ...
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│
├── data/
│   ├── assistant.db
│   └── History.txt
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

> **Note:** Update the template names above if your actual project contains different HTML files.

## Database Tables

### User

Stores assistant user information.

### Notes

Stores user notes.

### Tasks

Stores tasks and their completion status.

## Purpose

This project is part of my journey toward building an AI Personal Assistant and Research Agent.

Smart Assistant V5 is an upgraded version of Smart Assistant V4, where the terminal-based interface was transformed into a Flask web application. The primary goal was to learn web application development while preserving the existing business logic and database architecture.

## Learning Outcomes

* Flask Fundamentals
* Flask Routing
* HTML Forms
* Jinja Templates
* Template Inheritance
* Flask + SQLite Integration
* Separation of UI and Business Logic
* Modular Web Application Development

## Future Roadmap

```text
Smart Assistant V5
↓
LLM Integration
↓
Prompt Engineering
↓
Tool Calling
↓
Embeddings
↓
Vector Databases
↓
RAG
↓
AI Personal Assistant
↓
Research Agent
```

## Author

Built by a B.Tech student learning Software Engineering, AI Systems, AI Engineering, and Agent Development through project-based learning.
