# ReAct-Based Test Case Generation Agent

## Overview

This project implements a simple AI agent system using the **ReAct (Reason + Act)** design pattern with **CrewAI**.

The system takes a software requirement as input and automatically generates structured test cases.

It demonstrates how an AI agent can:

* Think step-by-step (reasoning)
* Use tools when needed (acting)
* Produce structured, machine-readable output

---

## How It Works

The workflow consists of two agents:

### 1. Requirement Analyst

Analyzes the input requirement and identifies:

* Actor
* Action
* Object
* Conditions
* Constraints

The output is converted into structured JSON using a deterministic tool.

### 2. Test Designer

Uses the structured requirement to generate up to 5 test cases.
Each test case includes:

* Title
* Preconditions
* Steps
* Expected Result

The final output is formatted into structured JSON.

---

## Purpose

This project is designed as a training exercise to understand:

* The ReAct agent design pattern
* Tool-calling workflows
* Multi-agent orchestration using CrewAI
* Structured output generation from natural language requirements

---

## Example Input

> The registered user should be able to log in using a valid email and password. The account must be locked after 5 failed attempts.

---

## Example Output

Structured JSON test cases generated from the requirement.

---

This project focuses on clarity, deterministic tooling, and demonstrating reasoning + action loops in an agent system.
