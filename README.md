# ⚖️ The Historical Court

## Multi-Agent System using Google Agent Development Kit (ADK)

---

## 👤 Author Information

**Name:** Khanatip Chimphu
**Student ID:** 66010095
**Course Assignment:** Multi-Agent System using Google ADK
**Project Title:** The Historical Court

---

# 📖 Overview

**The Historical Court** is a Multi-Agent System developed using Google's **Agent Development Kit (ADK)** that simulates a courtroom environment to analyze historical figures or events.

The system assigns multiple AI agents to research **conflicting perspectives from Wikipedia**, evaluate the balance of information, and produce a **neutral, evidence-based historical verdict**.

Instead of generating a one-sided answer, the system ensures fairness by using:

* Parallel research agents
* Loop-based review process
* Tool-controlled loop termination
* Structured session state management

The final verdict is automatically saved as a `.txt` file.

---

# 🎯 Project Objectives

This project demonstrates key concepts in modern AI system design:

* Multi-Agent Architecture
* Parallel Task Execution
* Loop-based Decision Workflow
* Session State Management
* Tool-based Loop Control using `exit_loop`
* Automated Report Generation
* Integration with External Knowledge Source (Wikipedia)

---

# 🧠 System Architecture

The system follows a courtroom-inspired workflow:

```
User Input
    │
    ▼
Inquiry Agent
    │
    ▼
Parallel Investigation
 ┌───────────────┬───────────────┐
 │               │               │
 ▼               ▼               │
Admirer Agent   Critic Agent    │
 │               │               │
 └──────► Session State ◄───────┘
               │
               ▼
           Judge Agent
        (Loop until balanced)
               │
               ▼
         Verdict Writer
               │
               ▼
        Output Verdict File
```

---

# ⚙️ Agent Workflow Explanation

---

# Step 1 — Inquiry Phase

## Inquiry Agent

### Responsibility

* Receive historical topic from user
* Store topic in Session State

### Session State Key

```
topic
```

### Example Input

```
Napoleon Bonaparte
Cold War
Genghis Khan
```

---

# Step 2 — Investigation Phase (Parallel Execution)

Two research agents run simultaneously.

---

## 🟢 Admirer Agent

### Role

Research ONLY positive aspects.

### Research Focus

* Achievements
* Contributions
* Legacy
* Success

### Example Search Queries

```
Napoleon achievements
Genghis Khan legacy
```

### Store in Session State

```
pos_data
```

---

## 🔴 Critic Agent

### Role

Research ONLY negative aspects.

### Research Focus

* Controversies
* Criticism
* Failures
* War crimes

### Example Search Queries

```
Napoleon controversy
Cold War criticism
```

### Store in Session State

```
neg_data
```

---

# Step 3 — Trial & Review Phase (Loop Control)

## 👨‍⚖️ Judge Agent

The Judge Agent evaluates whether the information is balanced.

---

## Evaluation Criteria

The Judge reviews:

```
pos_data
neg_data
```

---

## If information is insufficient:

The Judge allows the loop to continue.

Research agents will collect more data.

---

## If information is balanced:

The Judge calls the required tool:

```
exit_loop
```

---

## Important Assignment Requirement

Loop termination is controlled using a Tool.

NOT using prompt alone.

This ensures:

* Proper loop control
* Assignment compliance
* No infinite loops

---

# Step 4 — Verdict Phase

## Verdict Writer Agent

This agent generates the final historical report.

---

## Report Includes

* Topic name
* Positive contributions
* Negative controversies
* Neutral balanced verdict

---

## Output Location

```
historical_output/
```

Example:

```
historical_output/Napoleon Bonaparte.txt
```

---

# 💾 Session State Design

The system uses structured Session State:

| State Key | Description                |
| --------- | -------------------------- |
| topic     | User input topic           |
| pos_data  | Positive research findings |
| neg_data  | Negative research findings |

---

# 🔁 Loop Control Logic

Loop termination uses:

```
exit_loop tool
```

This ensures:

* Correct loop logic
* Assignment requirement compliance
* Safe execution

---

# 🧰 Technologies Used

| Technology       | Purpose                   |
| ---------------- | ------------------------- |
| Google ADK       | Multi-Agent orchestration |
| Gemini 2.5 Flash | Language Model            |
| Vertex AI        | Model Infrastructure      |
| Wikipedia API    | Knowledge source          |
| LangChain Tool   | Tool integration          |
| Python           | Programming Language      |

---

# 📁 Project Structure

```
Historical-Agent/

│
├── agent.py
├── README.md
├── .env.example
│
└── historical_output/
      └── verdict files
```

---

# 🚀 How to Run

---

## 1. Install dependencies

```
pip install -r requirements.txt
```

or

```
pip install google-adk langchain wikipedia python-dotenv
```

---

## 2. Set Environment Variables

Create `.env`

Example:

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=global
MODEL=gemini-2.5-flash
```

---

## 3. Run ADK Web Interface

```
adk web --reload_agents
```

---

## 4. Enter Topic

Example:

```
Alexander the Great
```

---

## 5. Output Generated

Saved in:

```
historical_output/
```

---

# 📄 Example Output

```
THE HISTORICAL COURT VERDICT

Topic: Napoleon Bonaparte

Positive Contributions:
- Legal reforms (Napoleonic Code)
- Military leadership

Negative Controversies:
- War casualties
- Authoritarian rule

Final Verdict:
Napoleon was both a brilliant reformer and a controversial ruler.
```

---

# ⭐ Key Features

* Multi-Agent System Architecture
* Parallel Research Execution
* Loop Control using exit_loop Tool
* Wikipedia Knowledge Integration
* Session State Management
* Automated Report Generation
* Google ADK Implementation

---

# 📊 Assignment Requirements Fulfillment

| Requirement              | Status |
| ------------------------ | ------ |
| Sequential Agent         | ✅      |
| Parallel Agents          | ✅      |
| Loop Agent               | ✅      |
| exit_loop Tool           | ✅      |
| Session State Management | ✅      |
| Wikipedia Research       | ✅      |
| File Output              | ✅      |
| Github Repository        | ✅      |

---

# 🎓 Learning Outcomes

This project demonstrates practical implementation of:

* Multi-Agent Systems
* Agent orchestration using Google ADK
* Loop-based decision workflows
* AI-based historical analysis
* Tool-controlled execution

---

# ✅ Project Status

✔ Assignment Complete
✔ Fully Functional
✔ Ready for Submission
✔ Portfolio Ready

---

# ⚖️ The Historical Court

Multi-Agent System using Google ADK
