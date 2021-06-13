# theory-of-computation
## Homework 1
### Problem 2
#### **ABOUT**
Program simulates NFA on given a expression. 
Parameters of NFA are defined/passed by user input.
Program outputs same length string as given expression. While simulating expression, if any current state of machine is in accept state program outputs Y or else N on relevant index. \
The Last index shows if machine accepts whole string.

### **Input Format**

**first line** - expression \
**second line** - space separated parameters, **n** - number of states, **a** - number of accept states, **t** - number of transition pairs. \
**third line** - space separated state indexes \
followed by **n** lines of transition function definition, first integer represents how many pairs of transactions are followed. i-th line denotes i-th state. \
```
expression
n a t
accept states
Ki symbol state
```
Examples are provided.

#### **USAGE**

You must be in **Homework1** directory to run program using command:
```
python3 main.py
```
The program takes test files as an input from directory: 
```
Public_Tests/P2/In 
```
 Input/Output file name format must be:
```
inXXX.txt outXXX.txt
```
where XXX is any decimal number