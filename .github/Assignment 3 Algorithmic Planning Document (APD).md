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
|                  Welcome to Gear Calculator\! Let us explore your bike and make calculating gear ratios easy. Select from the following options 1\.     Program overview 2\.     Enter your bike details 3\.     Close program Enter your response:                 Welcome to Gear Calculator\! Let us explore your bike and make calculating gear ratios easy. Select from the following options 1\.     Program overview 2\.     Enter your bike details 3\.     Close program Enter your response: 1         Gear Ratio \= Chainring teeth / Cog teeth         \# Gears \= count of chainring \+ count of cog A lower gear ratio will mean easier pedaling, ideal for climbing hills. While a higher gear ratio means harder pedaling but more speed, ideal for flat roads. (e.g) Enter a unique bike ID: mountain Enter the sprocket sizes for Chainring (enter 0 to exit):  Enter Sprocket: 24 Enter Sprocket: 35 Enter Sprocket: 0 Enter the sprocket sizes for Cog (enter 0 to exit):  Enter Sprocket: 12 Enter Sprocket: 22 Enter Sprocket: 40 Enter Sprocket: 54 Enter Sprocket: 0 Bike ID    | Chainring    | Cog          | Gear Ratio   | \# Gears mountain | 24-35          | 12-54       | 2.92              | 8 Thank you for using the bicycle gear ratio calculator\!                 Welcome to Gear Calculator\! Let us explore your bike and make calculating gear ratios easy. Select from the following options 1\.     Program overview 2\.     Enter your bike details 3\.     Close program Enter your response: 2 Enter a unique bike ID: bmx Enter the sprocket sizes for Chainring (enter 0 to exit):  Enter Sprocket: 56 Enter Sprocket: 0 Enter the sprocket sizes for Cog (enter 0 to exit):  Enter Sprocket: 16 Enter Sprocket: 0 Bike ID    | Chainring    | Cog          | Gear Ratio   | \# Gears bmx         | 56-56          | 16-16       | 3.50              | 1 Thank you for using the bicycle gear ratio calculator\!                 Welcome to Gear Calculator\! Let us explore your bike and make calculating gear ratios easy. Select from the following options 1\.     Program overview  2\.     Enter your bike details 3\.     Close program Enter your response: 3 Thank you for using the bicycle gear ratio calculator\! |

3. ## Algorithmic Design

Before you start coding, plan the logic and consider the test data you'll use to verify correctness. Planning before coding saves time and frustration—it's a key practice for all programmers\! Follow the steps below to identify the inputs, outputs, calculations, and steps needed to solve the problem.

| Algorithmic design: |
| :---- |
| Identify and list all of the user input and their data types. You must have at least **three inputs**, and one **must** be a string. I do not recommend having more than five inputs. |
| Options: Int Bike name: String Sprockets: Int |
| Identify and list all of the outputs and their data types. |
| chainring\_big: Int chainring\_small: Int cog\_big: Int cog\_small: Int gear\_ratio: Float num\_gear: Int |
| What calculations do you need to do to transform inputs into outputs?  List all formulas needed, if applicable. If no calculations are needed, state that there are no calculations for this algorithm.  |
| gear\_ratio \= chainring\_big / cog\_small num\_gear \= chainring\_count \+ cog\_count  |
| Write out the steps the program will perform (number each step 1., 2., etc.). Each step will be translated directly into Python code. **DO NOT use code syntax, think about the steps you would ask someone to follow to solve the problem in conversational words.** |
| `main()` function steps: Print introduction Print the menu Get option While option is not EXIT If option is 1 Print program details Print sample run If option is 2 Get Bike ID Get sprocket(return values in chainring\_max, chainring\_min, chainring\_count) While sprockets does not \= 0 If sprocket is less than 0  Print Invalid Get sprocket While sprocket is greater than 0 Calculate count \+ 1 Calculate compare(return values in compare\_large, compare\_small) Get sprocket Get sprocket(return values in cog\_max, cog\_min, cog\_count) While sprockets does not \= 0 If sprocket is less than 0  Print Invalid Get sprocket While sprocket is greater than 0 Calculate count \+ 1 Calculate compare(pass in return values in compare\_large, compare\_small) Get sprocket Calculate gear\_ratio(pass in chainring\_max, cog\_min returns gear\_ratio) Calculate num\_gear(pass in chainring\_count, cog\_count return num\_gear) Print(chainring\_max, chainring\_min, cog\_max, cog\_min, gear\_ratio, num\_gear) Print Exit  |
| Other functions (starting with Assignment 2): main(): print\_intro(): Print a welcome message Print menu options get\_option(): Get users input for option while option is not 3 If option is 1 Print a description of the calculations used  Print an explanation of gear ratio Print a sample run If option is 2 get\_bike\_id(): get\_sprocket(chainring): get\_sprocket(cog): calc\_gear\_ratio(chainring\_max, cog\_min): calc\_num\_gear(chainring\_count, cog\_count): print\_bike(bike\_id, chainring, cog, gear\_ratio): Print the bike id, chainring, cog, calculated gear\_ratio, calculated num\_gear print\_outro(): get\_bike\_id(): Prompt for and get the bike name or id. Return bike id get\_sprocket(prompt): Prompt for and get a value for sprocket While sprocket does not equal 0 If sprocket \< 0 Print invalid Prompt for and get a value for sprocket While sprocket is greater than 0 count \+= 1 Calc\_compare(compare\_large, compare\_small, count) Prompt for and get a value for sprocket Return compare\_large, compare\_small, count calc\_gear\_ratio(chainring\_max, cog\_min): gear\_ratio \= chainring\_max / cog\_min return gear\_ratio calc\_num\_gear(chainring\_count, cog\_count): num\_gear \= chainring\_count \* cog\_count return num\_gear print\_outro(): Print an exit message  |
|  |

