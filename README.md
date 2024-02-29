# Shelf Inventory Robot/Agent

This project focuses on solving the shelf inventory problem using robotic agents. The objective is to efficiently store boxes on inventory shelves while minimizing cost. The agents collaborate and coordinate with each other to achieve the goal state.

## Table of Contents

1. [Introduction](#introduction)
2. [Phase 1](#phase-1)
    - [Problem Definition](#problem-definition)
    - [Environment Type](#environment-type)
    - [Agent Type](#agent-type)
    - [PEAS](#peas-performance-measure-environment-actuators-sensors)
3. [Phase 2](#phase-2)
    - [Stage 1](#stage-1)
4. [Design](#design)
    - [Problem State Space](#problem-state-space)
    - [Assumptions](#assumptions)
    - [Algorithm](#algorithm-bfs)

## Introduction

The shelf inventory problem involves storing boxes on shelves while minimizing cost. The project utilizes robotic agents to perform the task. The agents collaborate and coordinate their actions to achieve efficient box placement.

## Phase 1

### Problem Definition

The problem is defined as storing boxes on shelves, where the objective is to minimize cost. Assumptions and simplifications are made to simplify the problem, such as treating all levels of a shelf equally and using a general "put" action to find an empty place for a box.

### Environment Type

The environment consists of two shelves stacked vertically, with two agents operating within it. The environment is accessible, deterministic, fully observable, discrete, and static. Agents can perform actions such as moving and putting boxes.

### Agent Type

The agents follow a logic-based architecture that enables collaboration and coordination. They work together as a team to accomplish the goal state, with a focus on how to accomplish the objective and organizing each agent's effort within the team.

### PEAS (Performance measure, Environment, Actuators, Sensors)

- Performance measure: The performance is measured based on the minimum cost and time required to put an item in an empty slot closest to an agent.
- Environment: The shelves serve as the environment for the agents.
- Actuators: The agents utilize three-level lifters for carrying items and four wheels for movement.
- Sensors: The agents use a camera to detect empty slots and radar for other purposes.

## Phase 2

### Stage 1

The details of Stage 1 are provided in the Phase 2 document.

## Design

This section focuses on the design aspects of the project.

### Problem State Space

The problem state space is the collection of all possible states that the system can be in at any given time. It includes the system's internal state and its interactions with the environment. The problem state space in this project is calculated based on the dimensions of the shelves and the number of agents.

### Assumptions

Additional assumptions are made to simplify the problem and handle agent coordination, including the capacity of agents, priority selection, and the ability to carry only one box at a time.

### Algorithm

The algorithm used in the project is the Breadth-First Search (BFS) algorithm. It is employed to find the shortest paths for the agents to reach their respective goals.
