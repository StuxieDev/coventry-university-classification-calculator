# Classification Calculator for Coventry University

## Credits 
Originally Made by [Matthew Chivers](https://github.com/matthewchivers)
Modified & Updated by [StuxieDev](https://stuxie.dev)

### Pre-amble
This calculator has not been officially verified as accurate against Coventry University's internal systems. However, it does follow the algorithms correctly (to the best of our knowledge). 

The calculator did make correct calculations for the cohort graduating in Summer 2020 (for those students kind enough to test it, anyway).

### Classifications

At the time of writing (Summer 2023), there are three methods of classification:
1) The average mark of the 100 credits worth of modules with the highest mark at level 6 or above
2) The average mark of the 220 credits worth of modules with the highest mark at level 5 and above (to include a maximum of 120 credits at Level 5)
3) The average mark of the 300 credits worth of modules with the highest mark at levels 4 and above (to include a maximum of 120 credits at each of Levels 4 and 5)

This calculator currently assumes a classic three year degree plus industrial placement. Roughly corresponding with:

* Year One = Level 4
* Year Two = Level 5
* Industrial Placement Year = Level 5
* Year Three = Level 6

## Instructions

> #### Note
> The input functionality ideally needs changing to be more robust. Either to take (CLI) input at runtime or else from a (CSV/JSON) file. Hard-coding inputs should be avoided, but this was hashed together alongside final-year deadlines and revision.

#### Insert grade information into the code directly:

There is a code-block similar to:
``` python
if __name__ == "__main__":

    ##################################
    # INSERT GRADE INFORMATION BELOW #
    ################################## 
```

The modules displayed under this comment block should be fairly self-explanatory. Use them as a template for your own grades/modules.

**Important**
The structure of the arguments taken by "Module" is `Year, Code, Credits, Grade, Required`. For example: `Module(3, "5004CEM", 30, 40, True)` corresponds with: Year 3, Module code 5004CEM, 30 Credits, Grade 40, and "True" indicates that the module **is** required as part of the classification. Currently only one module is populated as required: the dissertation/final-year-project. It is only necessary to declare a value in this argument for required modules, all others default to "False".

> The current information is pre-populated for Computer Science Students Graduating in 2020, including a placement year.

#### Run the script
Once the grades (modules) are populated, run the script! Something like:
``` bash
$ python calculator.py
```
The output will inform you of the classification you should be awarded, and lists the calculations from all algorithms for information purposes.

The calculations employ backtracking to gain all grade/module permutations. For this reason, the third classification algorithm can take a considerable amount of time to calculate (though it has never taken longer than a few seconds in my own tests).
