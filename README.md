# 🛡️ AI Laptop Guardian

### Voice-First AI Assistant for Laptop Health, Performance & Security

**AI Laptop Guardian** is a Python-based voice-first laptop monitoring assistant designed to continuously observe important system health parameters, detect potential performance issues, and communicate them to the user through natural voice-based alerts.

Instead of requiring users to constantly open Task Manager and interpret technical numbers, AI Laptop Guardian aims to make the laptop **proactively communicate when something needs attention**.

> **Monitor → Understand → Explain → Ask → Act**

---

## 🚀 Project Vision

Most laptop monitoring tools provide raw numbers such as CPU usage, RAM usage, storage usage, and running processes.

The user still has to understand:

* Is this usage normal?
* Why is my laptop slow?
* Which application is causing the problem?
* What should I do?
* Is this something I should be concerned about?

AI Laptop Guardian aims to add an intelligent voice-based layer on top of system monitoring.

For example:

> 🗣️ **AI Laptop Guardian:**
> "Your memory usage is currently very high. Would you like to know which application is using the most memory?"

The long-term vision is to evolve the project into a **privacy-first, on-device AI laptop companion** capable of monitoring, explaining, and assisting with laptop health, performance, and security.

---

# 🎯 Problem

Laptop users often discover system problems only after performance has already degraded.

Common situations include:

* High CPU usage
* High RAM usage
* Storage becoming full
* Applications consuming excessive resources
* Background processes affecting performance
* Potential security events
* Difficulty understanding technical system information

Traditional monitoring tools are primarily visual and require the user to actively check them.

**AI Laptop Guardian explores a more proactive approach:**

> Instead of the user constantly checking the laptop, the laptop can tell the user when something requires attention.

---

# 💡 Solution

AI Laptop Guardian combines:

**System Monitoring**
↓
**Problem Detection**
↓
**AI Interpretation**
↓
**Voice Alert**
↓
**User Voice Response**
↓
**Future Action with User Confirmation**

The system converts raw system information into understandable human language.

For example:

```text
RAM: 88%
Top memory-consuming process: Chrome
```

can become:

> "Your laptop is currently using a high amount of memory. Chrome is one of the applications consuming significant memory."

---

# ✨ Current Features

The current prototype includes:

* ✅ CPU usage monitoring
* ✅ Multiple CPU samples for more reliable detection
* ✅ High CPU usage detection
* ✅ CPU severity counting
* ✅ RAM usage monitoring
* ✅ Storage usage monitoring
* ✅ Highest CPU-consuming process detection
* ✅ Highest RAM-consuming process detection
* ✅ Filtering of misleading processes such as System Idle Process
* ✅ Python-based system monitoring
* ✅ Voice interaction development
* ✅ Whisper-based speech recognition setup
* ✅ Initial voice assistant workflow

---

# 🧠 Monitoring & Detection

The current monitoring engine uses **Python** and **psutil** to collect system information.

It monitors parameters such as:

| Parameter          | Purpose                                     |
| ------------------ | ------------------------------------------- |
| CPU Usage          | Detect unusually high processor utilization |
| RAM Usage          | Identify high memory consumption            |
| Storage            | Monitor disk-space usage                    |
| Processes          | Identify resource-heavy applications        |
| CPU Severity Count | Determine whether high CPU usage persists   |

### Example

```text
Highest CPU Usage:
SDXHelper.exe

RAM Usage:
~88%

Storage Usage:
~68.8%

CPU Severity:
Based on repeated high CPU readings
```

The CPU monitoring system uses multiple readings rather than relying only on a single instantaneous value.

This helps reduce misleading alerts caused by temporary CPU spikes.

---

# 🎙️ Voice Interaction

Voice is a major part of the project's long-term interaction model.

The goal is to allow users to interact with their laptop through natural speech.

### Voice Input

```text
User speaks
     ↓
Microphone
     ↓
Whisper Speech Recognition
     ↓
Text
     ↓
Intent / AI Processing
```

### Voice Output

```text
System Event
     ↓
Problem Detection
     ↓
AI Interpretation
     ↓
Natural Language Response
     ↓
Text-to-Speech
     ↓
User hears the alert
```

---

# 🏗️ System Architecture

```text
                    ┌───────────────┐
                    │     USER      │
                    └───────┬───────┘
                            │
                      Voice Input
                            │
                            ▼
                    ┌───────────────┐
                    │    Whisper    │
                    │ Speech-to-Text│
                    └───────┬───────┘
                            │
                            ▼
              ┌─────────────────────────┐
              │     AI / Decision       │
              │         Layer           │
              └────────────┬────────────┘
                           │
                 ┌─────────┴─────────┐
                 │                   │
                 ▼                   ▼
        ┌────────────────┐   ┌────────────────┐
        │ System Monitor │   │ Event Analysis │
        │     psutil     │   │  & Detection   │
        └───────┬────────┘   └───────┬────────┘
                │                    │
                └─────────┬──────────┘
                          ▼
                 ┌────────────────┐
                 │ Alert / Reply  │
                 └───────┬────────┘
                         │
                         ▼
                 ┌────────────────┐
                 │ Text-to-Speech │
                 └───────┬────────┘
                         │
                         ▼
                       USER
```

---

# 🔄 How It Works

### 1. Monitor

The system collects laptop health informati
