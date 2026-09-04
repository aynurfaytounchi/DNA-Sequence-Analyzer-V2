# DNA Sequence Analyzer | V2 🧬

A simple Python project for analyzing DNA sequences version 2.

I created this project while learning Python and used biological examples to practice basic Python concepts. The program allows the user to enter multiple DNA sequences and performs some basic analysis on each sequence.

## What does this program do?

For each DNA sequence, the program:

* Checks whether the sequence contains only valid DNA bases (`A`, `T`, `G`, `C`)
* Counts the number of `A`, `T`, `G`, and `C`
* Calculates the DNA sequence length
* Calculates GC content
* Generates the complementary DNA sequence
* Stores the results in dictionaries inside a list
* Displays the analysis results for each sample

## Example

Example input:

```text
How many DNA samples do you want to enter? 2

Enter your DNA sample 1: ATGC
Enter your DNA sample 2: GGCC
```

Example output:

```text
------|DNA ANALYSIS RESULTS|------

Sample 1
DNA: ATGC
Length: 4
A: 1
T: 1
G: 1
C: 1
GC Content: 50.00%
Complement: TACG

Sample 2
DNA: GGCC
Length: 4
A: 0
T: 0
G: 2
C: 2
GC Content: 100.00%
Complement: CCGG
