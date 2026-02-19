# The Historical Court (Multi-Agent System with Google ADK)

## Overview

This project implements a Multi-Agent System using Google's Agent Development Kit (ADK) to analyze historical figures or events in a simulated court setting.

The system gathers conflicting perspectives from Wikipedia and produces a balanced and neutral historical report.

The process consists of:

- Inquiry
- Investigation
- Trial & Review
- Verdict

The final output is saved as a text file automatically.

---

## Objective

The objective of this project is to simulate a historical courtroom where multiple agents present different perspectives.

Each agent has a specific role:

- Admirer → Research positive aspects
- Critic → Research negative aspects
- Judge → Evaluate balance of evidence
- Verdict Writer → Generate final neutral report

This ensures objective and unbiased historical analysis.

---

## System Architecture

The system consists of four main stages:

---

### Step 1: Inquiry (Sequential Agent)

The user provides a historical topic.

Examples:

- Genghis Khan
- Napoleon Bonaparte
- Cold War

The topic is stored in Session State:

topic

---

### Step 2: Investigation (Parallel Agent)

Two agents perform research simultaneously.

Admirer Agent:

Research:

- achievements
- success
- legacy

Saved to:

pos_data

Critic Agent:

Research:

- controversy
- criticism
- failures

Saved to:

neg_data

---

### Step 3: Trial & Review (Loop Agent)

Judge evaluates the balance between positive and negative information.

If insufficient:

Research agents repeat investigation.

If sufficient:

Judge uses exit_loop tool to stop the loop.

This ensures proper loop control.

---

### Step 4: Verdict (Final Output)

Final agent generates balanced historical analysis.

File output:

outputs/verdict.txt

Contains:

- Positive analysis
- Negative analysis
- Neutral conclusion

---

## Agent Structure

Root Agent

Sequential Agent (Court)

Parallel Agent (Investigation)

- Admirer
- Critic

Loop Agent (Trial)

- Admirer
- Critic
- Judge

Verdict Writer

---

## Technologies Used

- Google ADK
- Gemini 2.5 Flash
- Vertex AI
- Wikipedia API
- LangChain Tool
- Python

---

## Session State Design

State Keys:

topic

pos_data

neg_data

Templating Used:

{ topic? }

{ pos_data? }

{ neg_data? }

---

## Loop Control

Loop termination uses:

exit_loop tool

This prevents infinite loops and ensures correct execution.

---

## How to Run

Install dependencies:

pip install -r requirements.txt

Run the system:

adk web --reload_agents

Enter topic example:

Genghis Khan

---

## Example Output

File location:

outputs/verdict.txt

Example content:

- Achievements
- Criticism
- Balanced historical conclusion

---

## Recommended Test Topics

Genghis Khan

Napoleon Bonaparte

Cold War

Julius Caesar

Alexander the Great

Adolf Hitler

---

## Assignment Requirements Fulfilled

This project successfully implements:

Sequential Agent

Parallel Agent

Loop Agent

exit_loop tool usage

Session State Management

Wikipedia Research Tool

File output system

Multi-Agent architecture

---

## Learning Outcomes

This project demonstrates:

Multi-Agent System Design

Google ADK usage

Loop Control using exit_loop tool

Parallel agent execution

Session state management

LLM orchestration

---

## Author

Khanatip Chimphu 66010095

Multi-Agent System using Google ADK
