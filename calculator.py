from __future__ import division

class Module:
    def __init__(self, module_level, module_code, module_credits, module_grade, module_required=False):
        self.level = module_level
        self.code = module_code
        self.credits = module_credits
        self.grade = module_grade
        self.required = module_required


def get_required_modules(modules):
    req_mods = []
    for mod in modules:
        if mod.required:
            req_mods.append(mod.code)
    return req_mods

def get_permutations(modules, required_modules, max_creds = 100, max_creds_three = 100 , max_creds_two = 0, max_creds_one = 0):
    perms = []
    perm_bt(perms, modules, required_modules, max_creds, max_creds_three, max_creds_two, max_creds_one)
    return perms
    # Send to BT

def perm_bt(perms, modules, required_modules, max_creds, max_creds_three, max_creds_two, max_creds_one, partial = []):
    creds_one = 0
    creds_two = 0
    creds_three = 0
    creds_total = 0

    for mod in partial:
        if mod.level == 1:
            creds_one += mod.credits
        elif mod.level == 2:
            creds_two += mod.credits
        elif mod.level == 3:
            creds_three += mod.credits
        else:
            print("ERROR: INVALID MODULE LEVEL SPECIFIED")
        creds_total = creds_one + creds_two + creds_three
    
    if creds_one > max_creds_one or creds_two > max_creds_two or creds_three > max_creds_three or creds_total > max_creds:
        return

    if creds_total == max_creds:
        for mod_code in required_modules:
            acceptable = False
            for mod in partial:
                if mod.code == mod_code:
                    acceptable = True
            if not acceptable:
                return
        perms.append(partial)
    
    for i in range(len(modules)):
        module = modules[i]
        remaining = modules[i+1:]
        perm_bt(perms, remaining, required_modules, max_creds, max_creds_three, max_creds_two, max_creds_one, partial + [module])

def get_perm_grade(perm):
    total_credits = 0
    grade = 0
    for mod in perm:
        total_credits += mod.credits
    for mod in perm:
        weight = mod.credits / total_credits
        grade += mod.grade * weight
    return grade

def classification(modules, max_creds, max_creds_three, max_creds_two, max_creds_one):
    required_mods = get_required_modules(modules)
    permutations = get_permutations(modules, required_mods, max_creds, max_creds_three, max_creds_two, max_creds_one)
    best_perm = []
    best_grade = 0
    for perm in permutations:
        grade = get_perm_grade(perm)
        if grade > best_grade:
            best_grade = grade
            best_perm = perm
    return best_perm, round(best_grade, 2)
    

def print_grade(perm, grade):
    for mod in perm:
        print("\tModule: " + str(mod.code) + "\t-\t Grade: " + str(mod.grade) + "\t-\t Credits: " + str(mod.credits))
    print("\n\tGRADE:\t" + str(grade))
    print("\tCLASSIFICAION:\t" + get_classification_name(grade))
    print("\n")

def get_classification_name(grade):
    if (grade >=0 and grade < 40):
        return "Fail"
    elif(grade >=40 and grade < 50):
        return "Third Class"
    elif(grade >=50 and grade < 60):
        return "2:2 (Second Class, Second Division)"
    elif(grade >=60 and grade < 70):
        return "2:1 (Second Class, First Division)"
    elif(grade >=70 and grade <=100):
        return "1st Class"
    else:
        return "Either you entered some information incorrectly, or you cheated..."


if __name__ == "__main__":

    ##################################
    # INSERT GRADE INFORMATION BELOW #
    ##################################

    year_one_modules = [
        ## Year, Code, Credits, Grade, Required
        Module(1, "4000CEM", 15, 83.33), # Programming and Algorithms
        Module(1, "4003CEM", 15, 61.40), # Object Oriented Programming
        Module(1, "4004CEM", 15, 60.91), # Computer Architecture and Networks
        Module(1, "4005CEM", 5, 61.05), # Database Systems
        Module(1, "4006CEM", 15, 70), # Computer Science Activity Led Learning Project 1
        Module(1, "4007CEM", 15, 58.33), # Computer Science Activity Led Learning Project 2
        Module(1, "4067CEM", 15, 75), # Software Design
        Module(1, "4068CEM", 15, 91.66), # Mathematics for Computer Science
        Module(1, "Add+1", 10, 68) # Add+Vantage
    ]

    year_two_modules = [
        ## Year, Code, Credits, Grade, Required
        Module(2, "5000CEM", 10, 56), # Introduction to Artificial Intelligence
        Module(2, "5001CEM", 20, 71), # Software Engineering
        Module(2, "5002CEM", 20, 49.38), # Theory of Computation
        Module(2, "5003CEM", 15, 64.66), # Advanced Algorithms
        Module(2, "5004CEM", 20, 57), # Operating Systems and Security
        Module(2, "5005CEM", 10, 53), # Data Science
        Module(2, "5011CEM", 15, 60.33), # Big Data Programming Project
        Module(2, "Add+2", 10, 72) # Add+Vantage
    ]

    year_three_modules = [
        ## Year, Code, Credits, Grade, Required
        Module(3, "6000CEM", 10, 78.40, True), # Individual Project Preparation
        Module(3, "6001CEM", 20, 76, True), # Individual Project
        Module(3, "6002CEM", 20, 62.50), # Mobile App Development
        Module(3, "6003CEM", 20, 54.80), # Web API Development
        Module(3, "6005CEM", 20, 61), # Security
        Module(3, "6006CEM", 20, 60), # Machine Learning and Related Applications
        Module(3, "Add+3", 10, 48) # Add+Vantage
    ]

    ## CLASSIFICATION ONE ##
    # The average mark of the 100 credits worth of modules with the highest mark 
    # at level 6 or above
    print("ALGORITHM 1:")
    c1_mods = year_three_modules
    c1_perm, c1_grade = classification(c1_mods, 100, 100, 0, 0)
    print_grade(c1_perm, c1_grade)

    ## CLASSIFICATION TWO ##
    # The average mark of the 220 credits worth of modules with the highest mark 
    # at level 5 and above (to include a maximum of 120 credits at Level 5)
    print("ALGORITHM 2:")
    c2_mods = year_three_modules + year_two_modules
    c2_perm, c2_grade = classification(c2_mods, 220, 120, 120, 0)
    print_grade(c2_perm, c2_grade)

    ## CLASSIFICATION THREE ##
    # The average mark of the 300 credits worth of modules with the highest mark 
    # at levels 4 and above (to include a maximum of 120 credits at each of Levels 4 and 5)
    print("ALGORITHM 3:")
    c3_mods = year_three_modules + year_two_modules + year_one_modules
    c3_perm, c3_grade = classification(c3_mods, 300, 120, 120, 120)
    print_grade(c3_perm, c3_grade)

    print("############################")
    print("#  HIGHEST CLASSIFICATION  #")
    print("############################\n")
    best_grade = max(c1_grade, c2_grade, c3_grade)
    print("\tGrade: " + str(best_grade))
    print("\tClassification: " + get_classification_name(best_grade))
    print("\n")
