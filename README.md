# ⚖️ The Historical Court

## Multi-Agent System using Google ADK

---

## 👤 Author Information

**Name:** Khanatip Chimphu
**Student ID:** 66010095
**Project:** Multi-Agent System using Google Agent Development Kit (ADK)
**Assignment:** The Historical Court

---

# 📖 Project Description

**The Historical Court** is a Multi-Agent System built using the **Google Agent Development Kit (ADK)** that simulates a courtroom for historical analysis.

The system investigates a historical figure or event by assigning multiple AI agents to research **different perspectives from Wikipedia**.

Instead of providing a one-sided answer, the system produces a **balanced, neutral, and evidence-based verdict**.

The final result is saved as a `.txt` report file.

---

# 🎯 Project Objective

This project aims to demonstrate:

* Multi-Agent collaboration
* Parallel task execution
* Loop-based review process
* Session state management
* Tool-based loop exit control
* Balanced historical analysis

---

# 🧠 System Architecture Overview

The system consists of **4 main stages**

```

User Input → Investigation → Trial & Review → Final Verdict

```

---

# ⚙️ Step 1: The Inquiry (Sequential Agent)

## 🧑‍💼 Inquiry Agent

### Responsibility

Receive topic from user

### Example Input

````

Genghis Khan

```

### Store in Session State

```

topic

```

---

# 🔎 Step 2: The Investigation (Parallel Agents)

Two agents run in parallel

---

## 🟢 Agent A: The Admirer

### Role

Research positive aspects only

### Focus Keywords

```

achievements
accomplishments
contributions
legacy

```

### Example Search

```

Genghis Khan achievements

```

### Store in State

```

pos_data

```

---

## 🔴 Agent B: The Critic

### Role

Research negative aspects only

### Focus Keywords

```

controversy
criticism
failures
war crimes

```

### Example Search

```

Genghis Khan controversy

```

### Store in State

```

neg_data

```

---

# ⚖️ Step 3: The Trial & Review (Loop Agent)

## 👨‍⚖️ Agent C: The Judge

This agent reviews both sides

---

## Responsibilities

Check balance between:

```

pos_data
neg_data

```

---

## If information is NOT balanced

Judge requests more research

Example:

```

Admirer: Research more about economic contributions

Critic: Research more about military destruction

```

Loop continues

---

## If information IS balanced

Judge calls required tool:

```

exit_loop

```

This satisfies assignment requirement:

Prompt alone is NOT allowed to stop loop

---

# 🧾 Step 4: The Verdict (Final Agent)

Final report is generated

---

## Output includes:

- Summary
- Positive contributions
- Negative controversies
- Neutral final verdict

---

## Output File

```

output/verdict.txt

```

---

# 💾 Session State Management

The system uses structured state keys:

| State Key | Description |
|---------|-------------|
| topic | User topic |
| pos_data | Positive research |
| neg_data | Negative research |
| verdict | Final report |

---

# 🔁 Loop Control

Loop termination uses:

```

exit_loop tool

```

Required by assignment rules

---

# 🧰 Tools Used

## Google ADK

Used for:

- Agent creation
- Workflow management
- State management
- Loop control

---

## Wikipedia Tool

Used for:

- Research information
- Historical data retrieval

---

# 📁 Project Structure

```

historical-court/

│

├── main.py

│

├── agents/

│ ├── inquiry_agent.py

│ ├── admirer_agent.py

│ ├── critic_agent.py

│ ├── judge_agent.py

│ └── verdict_agent.py

│

├── tools/

│ ├── wiki_tool.py

│ └── exit_loop.py

│

├── output/

│ └── verdict.txt

│

└── README.md

```

---

# 🚀 Example Workflow

## User Input

```

Napoleon

```

---

## Admirer finds

```

Military genius
Napoleonic Code
Government reforms

```

---

## Critic finds

```

War casualties
Dictatorship
Exile

```

---

## Judge reviews

Loop continues if needed

---

## Final Verdict Generated

Saved to:

```

output/verdict.txt

```

---

# ⭐ Key Features

✅ Multi-Agent System  

✅ Parallel Processing  

✅ Loop with exit_loop tool  

✅ Wikipedia Integration  

✅ Session State Management  

✅ Automated Verdict Report  

✅ Google ADK Implementation  

---

# 📊 Assignment Requirements Fulfillment

| Requirement | Status |
|------------|--------|
| Multi-Agent Structure | ✅ |
| Parallel Agents | ✅ |
| Loop with exit_loop Tool | ✅ |
| Session State Management | ✅ |
| Wikipedia Research | ✅ |
| Final Output File | ✅ |
| Github Ready | ✅ |

---

# ▶️ How to Run

## Install Dependencies

```

pip install google-adk
pip install wikipedia

```

---

## Run Program

```

python main.py

```

---

## Enter Topic Example

```

Cold War

```

---

## Output File

```

output/verdict.txt

```

---

# 🧾 Example Verdict Output

```

THE HISTORICAL COURT VERDICT

Topic: Genghis Khan

Positive Contributions:
- United Mongol tribes
- Established trade routes

Negative Controversies:
- Mass destruction
- Civilian killings

Final Verdict:
Genghis Khan was both a powerful empire builder and a controversial conqueror.

```

---

# 🎓 Conclusion

This project demonstrates the power of Multi-Agent Systems in producing balanced analysis.

Using Google ADK, agents collaborate, review, and produce a neutral verdict through structured workflows.

This approach improves objectivity and reduces bias in AI-generated analysis.

---

# 🔗 Github Repository

Add your repository link here:

```

https://github.com/yourusername/historical-court

```

---

# ✅ Project Complete

Multi-Agent System using Google ADK  
The Historical Court

---
