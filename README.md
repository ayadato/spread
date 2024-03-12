# spread
## Overview
This program simulates a network of interacting agents on a two-dimensional grid. Each agent exists in one of the states "Normal", "Doubt", or "True" and includes information diffusion and correction processes.

## Characteristics
Agent states:
- Normal: The agent starts in this state.
- Doubt: represents an agent that is suspicious of information.
- True: Represents an agent with accurate information.

## Information Diffusion

Based on the profile, an agent shares information with neighboring agents.
The profile affects the probability of an agent communicating information to its neighbors.
Information diffusion can cause an agent to move to the "Doubt" or "True" state.

## Program Structure
The program uses the Tkinter library for graphical representation.
Each agent is represented as an instance of the Agent class, which contains information about its state, position, profile, bonds (neighboring agents), and other attributes.
The simulation includes functions for moving, drawing, updating agent state, and checking agent information.

## Use
When the program is executed, it starts a simulation in which agents randomly move and exchange information.
After a certain number of steps, a correction process occurs to correct questionable or incorrect information.

## Customization
Various parameters in the code can be customized, including grid size (FIELD_X and FIELD_Y) and cell size (CELL_SIZE). You can tailor the initial agent state and information to suit specific scenarios.

## Notes
The output of the simulation contains information about the time taken for the correction process and the total number of steps.
Graphs are generated to visualize the cumulative information diffusion over time.

## Dependencies
The ```Matplotlib``` library is required for data visualization and  ```Tkinter``` is used for graphical representation.
