# **Algorithmic Planning Document**

*Click the share settings button and change the permissions to “Anyone with link can **comment**” and submit the Website URL to the assignment in Canvas.* 

Planning your program before you start coding is part of the development process. In this document, you will:

- [ ] Step 1: Write a detailed description of your program  
- [ ] Step 2: Design a sample run with test input and output  
- [ ] Step 3: Algorithm design  
      - [ ] Identify the program inputs and their data types  
      - [ ] Identify the program outputs and their data types  
      - [ ] Identify any calculations or formulas needed  
      - [ ] Identify input/process/output functions and write the algorithmic steps 

1. ## Program Description

In the box below, describe the purpose of the program. You must include a detailed description with at least two complete sentences.

| Program description: |
| :---- |
| In bicycle parts and maintenance the chainring and cog are among the most important componentants along with the seat and pedals. Using the number of teeth on the chainring and cog the gear ratio can be determined. A gear ratio helps identify the rate a rider’s pedaling will match a revolution on the rear wheel. By changing and selecting the appropriate gear cyclists find ease on a multitude of terrain. This program calculates the gear ratio by dividing the number of teeth on the front chainring by the number of teeth on the rear cog. |

2. ## Sample Run

When designing your program, start with a sample run. Imagine a user running your program. What will they see? Identify the expected inputs and the corresponding outputs. Choose test data to validate your program and calculate the expected outputs. Use your sample run to test your program.

| Sample run: |
| :---- |
| Type of bike: "road" Size of the chainring: 56 Size of the cog: 16     Gear ratio for road bike: 3.5  \*\*\* When you submit the APD for Assignment 1, I want you to think about how your list of entries will look for Assignment 4\. In the space below, write a list of at least two entries in table format with column headers. Look at the APD linked in the Assignment 1 instructions for an example. Bike                       Chainring Size               Cog size                Gear Ratio \_\_\_\_\_                    \_\_\_\_\_\_\_\_\_\_\_\_               \_\_\_\_\_\_\_\_              \_\_\_\_\_\_\_\_\_\_ Mountain Bike       56                                   16                           3.5 BMX Bike              36                                   20                           1.8  |

3. ## Algorithmic Design

Before you start coding, plan the logic and consider the test data you'll use to verify correctness. Planning before coding saves time and frustration—it's a key practice for all programmers\! Follow the steps below to identify the inputs, outputs, calculations, and steps needed to solve the problem.

| Algorithmic design: |
| :---- |
| Identify and list all of the user input and their data types. You must have at least **three inputs**, and one **must** be a string. I do not recommend having more than five inputs. |
| Bike name: String Chainring Size: Int Cog Size: Int |
| Identify and list all of the outputs and their data types. |
| Gear Ratio: Float |
| What calculations do you need to do to transform inputs into outputs?  List all formulas needed, if applicable. If no calculations are needed, state that there are no calculations for this algorithm.  |
| Gear Ratio \= Chainring / Cog |
| Write out the steps the program will perform (number each step 1., 2., etc.). Each step will be translated directly into Python code. **DO NOT use code syntax, think about the steps you would ask someone to follow to solve the problem in conversational words.** |
| `main()` function steps: Print introduction Get Bike Name Get Chainring Size Get Cog Size Calculate Gear Ratio Print Bike, Chainring, Cog and Gear Ratio Print goodbye  |
| Other functions (starting with Assignment 2):  |

