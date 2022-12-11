# Working Directory

main_directory = "C:/Users/dylan/..."

#####################################################################################################

# Packages
import re
import numpy as np
import pandas as pd
import itertools 
import operator 
import matplotlib
import matplotlib.pyplot as plt
from itertools import accumulate

#####################################################################################################

# For better oversight - a color class to add different print() possibilities
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print(color.BOLD + 'Hello World !' + color.END)

#####################################################################################################

# Combined Configurations 

# Primary Paramters of Interest

#####################################################################################################

# 1. Lambda - Probability of Receiving the Large Payoff

l_low = .5
l_medium = .5
l_high = .5

# 2. Gamma - Probability of a state switch

g_low = .5
g_medium = .5
g_high = .5

# 3. M - large payoff received if firm product variety matches state 

M_low = 1
M_medium = 10
M_high = 100

# 4. m - small payoff guaranteed regardless of state

m_low = 10
m_medium = 10
m_high = 10

# 5. Alpha - initial investment into agility 

a_low = 5
a_medium = 5
a_high = 5

# 6. Cost Function - a simple algebraic multiplier for the cost function

c_low = .5
c_medium = .5
c_high = .5

# 7. Time Period 

T_low = 100
T_medium = 100
T_high = 100

#####################################################################################################

# Combined Parameters

# Concrete Parameters

#####################################################################################################

## Creating the Initial Set Up Variables ##
## If a variable above is changed, this bloc must be run again ##

# 1. State of the environment 

D_low = [0,1]
D_medium = [0,1]
D_high = [0,1]

# 2. Product Variety by the Firm / Agent 

d_low = 0
d_medium = 0
d_high = 0

# 3. Initial Time Period  

t_low = 0
t_medium = 0
t_high = 0

# 4. Future Costs of Reorganization due to Initial Investment alpha

ca_low = a_low * c_low
ca_medium = a_medium * c_medium
ca_high = a_high * c_high

print("Future cost of reorganization in the low game is", ca_low)
print("Future cost of reorganization in the medium game is", ca_medium)
print("Future cost of reorganization in the high game is", ca_high)

# 5. Belief of Matching the State 

pb_low = ((1-l_low)*(1-g_low)) / (g_low+(1-l_low)*(1-g_low))
pb_medium = ((1-l_medium)*(1-g_medium)) / (g_medium+(1-l_medium)*(1-g_medium))
pb_high = ((1-l_high)*(1-g_high)) / (g_high+(1-l_high)*(1-g_high))

print("Your belief in matching the state in the low game is ", pb_low, "or", pb_low * 100,"%.")
print("Your belief in matching the state in the medium game is ", pb_medium, "or", pb_medium * 100,"%.")
print("Your belief in matching the state in the high game is ", pb_high, "or", pb_high * 100,"%.")

# 6. Configurations needed for the np.random outcome function

game_low = 1
game_medium = 1
game_high = 1

# 7. Configurations needed for np.random probability 

x_low = 1-g_low
y_low = 1-l_low

x_medium = 1-g_medium
y_medium = 1-l_medium

x_high = 1-g_high
y_high = 1-l_high

gamma_probabilities_low = [g_low, x_low]
lambda_probabilities_low = [l_low, y_low]

gamma_probabilities_medium = [g_medium, x_medium]
lambda_probabilities_medium = [l_medium, y_medium]

gamma_probabilities_high = [g_high, x_high]
lambda_probabilities_high = [l_high, y_high]

# 8. Configurations needed for np.random probability 

large_payoff_scheme_low = [M_low,0]
large_payoff_scheme_medium = [M_medium,0]
large_payoff_scheme_high = [M_high,0]

# 9. Configurations for the decision mechanism 

just_hit_payoff_low = M_low + m_low 
dont_hit_payoff_low = m_low
expected_reorganize_payoff_low = -ca_low + (1-g_low)*l_low*M_low + m_low
expected_no_reorganize_payoff_low = pb_low*(1-g_low)*l_low*M_low + m_low
general_equation_low = (1-g_low)*l_low*M_low + m_low
miss_low = m_low - ca_low

just_hit_payoff_medium = M_medium + m_medium 
dont_hit_payoff_medium = m_medium
expected_reorganize_payoff_medium = -ca_medium + (1-g_medium)*l_medium*M_medium + m_medium
expected_no_reorganize_payoff_medium = pb_medium*(1-g_medium)*l_medium*M_medium + m_medium
general_equation_medium = (1-g_medium)*l_medium*M_medium + m_medium
miss_medium = m_medium - ca_medium

just_hit_payoff_high = M_high + m_high 
dont_hit_payoff_high = m_high
expected_reorganize_payoff_high = -ca_high + (1-g_high)*l_high*M_high + m_high
expected_no_reorganize_payoff_high = pb_high*(1-g_high)*l_high*M_high + m_high
general_equation_high = (1-g_high)*l_high*M_high + m_high
miss_high = m_high- ca_high

# 10. Configurations to extract results 

hit_results_low = 0
miss_results_reorg_low = 0 
miss_results_noorg_low = 0
mechanism_counter_low = 0
assurance_low = 0

hit_results_medium = 0
miss_results_reorg_medium = 0 
miss_results_noorg_medium = 0
mechanism_counter_medium = 0
assurance_medium = 0

hit_results_high = 0
miss_results_reorg_high = 0 
miss_results_noorg_high = 0
mechanism_counter_high = 0
assurance_high = 0

# 11. Graphing Configurations 

GPR_low = []
GPN_low = []
Time_Periods_low = []
time_counter_low = 0

GPR_medium = []
GPN_medium = []
Time_Periods_medium = []
time_counter_medium = 0

GPR_high = []
GPN_high = []
Time_Periods_high = []
time_counter_high = 0

# 12. Further Graphing Configurations 

GPN_sum_low = 0
GPR_sum_low = 0
cumulative_payout_GPN_low = list(accumulate(GPN_low))
cumulative_payout_GPR_low = list(accumulate(GPR_low))

GPN_sum_medium = 0
GPR_sum_medium = 0
cumulative_payout_GPN_medium = list(accumulate(GPN_medium))
cumulative_payout_GPR_medium = list(accumulate(GPR_medium))


GPN_sum_high = 0
GPR_sum_high = 0
cumulative_payout_GPN_high = list(accumulate(GPN_high))
cumulative_payout_GPR_high = list(accumulate(GPR_high))

#####################################################################################################

# Decision Making Mechanism

#####################################################################################################

# 1. Overview of expected payoffs if large M is not received and the individual is compelled to reorganize or not. 
# 1. Low Game 

print("Low Game: Expected payoff of reorganization after t = 1:", expected_reorganize_payoff_low)
print("Low Game: Expected payoff of no reorganization after t = 1:", expected_no_reorganize_payoff_low)

decision_low = max(expected_reorganize_payoff_low, expected_no_reorganize_payoff_low)

print("Assuming rationality, the decision rule ensures the greatest expected payoff.")

if max(expected_reorganize_payoff_low, expected_no_reorganize_payoff_low) == expected_reorganize_payoff_low:
    print(color.BOLD + "Low Game: In this case, the firm will reorganize." + color.END)
else: 
    print(color.BOLD + "Low Game: In this case, the firm will not reorganize." + color.END)

##########################################################

# 2. Overview of expected payoffs if large M is not received and the individual is compelled to reorganize or not. 
# 2. Medium Game 

print("Medium Game: Expected payoff of reorganization after t = 1:", expected_reorganize_payoff_medium)
print("Medium Game: Expected payoff of no reorganization after t = 1:", expected_no_reorganize_payoff_medium)

decision = max(expected_reorganize_payoff_medium, expected_no_reorganize_payoff_medium)

print("Assuming rationality, the decision rule ensures the greatest expected payoff.")

if max(expected_reorganize_payoff_medium, expected_no_reorganize_payoff_medium) == expected_reorganize_payoff_medium:
    print(color.BOLD + "Medium Game: In this case, the firm will reorganize." + color.END)
else: 
    print(color.BOLD + "Medium Game: In this case, the firm will not reorganize." + color.END)

########################################################################

# 3. Overview of expected payoffs if large M is not received and the individual is compelled to reorganize or not. 
# 3. Large Game

print("High Game: Expected payoff of reorganization after t = 1:", expected_reorganize_payoff_high)
print("High Game: Expected payoff of no reorganization after t = 1:", expected_no_reorganize_payoff_high)

decision_high = max(expected_reorganize_payoff_high, expected_no_reorganize_payoff_high)

print("Assuming rationality, the decision rule ensures the greatest expected payoff.")

if max(expected_reorganize_payoff_high, expected_no_reorganize_payoff_high) == expected_reorganize_payoff_high:
    print(color.BOLD + "High Game: In this case, the firm will reorganize." + color.END)
else: 
    print(color.BOLD + "High Game: In this case, the firm will not reorganize." + color.END)
    
#####################################################################################################
 # Low Configuration -  Agility Game with Reorganization
#####################################################################################################

# Loop Attempt #  
def agility_game_with_reorganization_low():
    global t_low
    global miss_results_reorg_low 
    global hit_results_low
    global mechanism_counter_low
    global assurance_low
         
    while t_low < T_low:
        t_low = t_low + 1
        #sum = sum + t
        if mechanism_counter_low > assurance_low:
            state_change_check_low = np.random.choice(D_low, size=game_low, p=gamma_probabilities_low)
            z_low = state_change_low
            mechanism_counter_low = mechanism_counter_low - 1
            if z_low == state_change_check_low:
                outcome_low = np.random.choice(large_payoff_scheme_low,size=game_low, p=lambda_probabilities_low)
                if outcome_low == 0:
                    #print("Period",t_low,":")
                    #print("The large payoff has not been received.")
                    #print("You will reorganize at the cost", ca_low, "for a total payoff this period of", miss_low)
                    miss_results_reorg_low = miss_results_reorg_low + 1
                    hit_results_low = hit_results_low
                    mechanism_counter_low = mechanism_counter_low + 1
                    loser_1_low = float(miss_low)
                    GPR_low.append(loser_1_low)
                    Time_Periods_low.append(t_low)
                else:
                    #print("Period",t_low,":")
                    #print("The large payoff has been received.")
                    #print("Your payoff is:", just_hit_payoff_low)
                    hit_results_low = hit_results_low + 1
                    miss_results_reorg_low = miss_results_reorg_low
                    winner_1_low = float(just_hit_payoff_low)
                    GPR_low.append(winner_1_low)
                    Time_Periods_low.append(t_low)
            else: 
                #print("Period",t_low,":")
                #print("The large payoff has not been received.")
                #print("You will reorganize at the cost", ca_low, "for a total payoff this period of", miss_low)
                miss_results_reorg_low = miss_results_reorg_low + 1
                hit_results_low = hit_results_low
                mechanism_counter_low = mechanism_counter_low + 1
                loser_1_low = float(miss_low)
                GPR_low.append(loser_1_low)
                Time_Periods_low.append(t_low)
        # The below line instructs the game to engage in the state change. 
        # If the state does not change, the individual guarantees a large payoff in period 1.
        elif mechanism_counter_low == assurance_low: 
            state_change_low = np.random.choice(D_low, size=game_low, p=gamma_probabilities_low)
        # If the state change does not occur, D = d = 0 and the game proceeds to the next step.
        # The large payoff is thus not guaranteed. 
            if d_low == state_change_low:
                outcome_low = np.random.choice(large_payoff_scheme_low,size=game_low, p=lambda_probabilities_low)
                if outcome_low == 0:
                    #print("Period",t_low,":")
                    #print("The large payoff has not been received.")
                    #print("You will reorganize at the cost", ca_low, "for a total payoff this period of", miss_low)
                    miss_results_reorg_low = miss_results_reorg_low + 1
                    hit_results_low = hit_results_low 
                    mechanism_counter_low = mechanism_counter_low + 1
                    loser_1_low = float(miss_low)
                    GPR_low.append(loser_1_low)
                    Time_Periods_low.append(t_low)

                else:
                    #print("Period",t_low,":")
                    #print("The large payoff has been received.")
                    #print("Your payoff is:", just_hit_payoff_low)
                    hit_results_low = hit_results_low + 1
                    miss_results_reorg_low = miss_results_reorg_low 
                    winner_1_low = float(just_hit_payoff_low)
                    GPR_low.append(winner_1_low)
                    Time_Periods_low.append(t_low)
                
            else:
                #print("Period",t_low,":")
                #print("The large payoff has not been received.")
                #print("You will reorganize at the cost", ca_low, "for a total payoff this period of", miss_low)
                miss_results_reorg_low = miss_results_reorg_low + 1
                hit_results_low = hit_results_low
                mechanism_counter_low = mechanism_counter_low + 1
                loser_1_low = float(miss_low)
                GPR_low.append(loser_1_low)
                Time_Periods_low.append(t_low)
    
  
    print("You have missed", miss_results_reorg_low, "times and hit", hit_results_low, "times.")
    print("You have a individual payoffs of", GPR_low)
    print("You have cumulative payoffs of", list(accumulate(GPR_low)))
    print("Total Time Periods:", Time_Periods_low)

#####################################################################################################    

 # Low Configuration - Agility Game without Reorganization 

# Loop Attempt #
def agility_game_without_reorganization_low():
    global t_low
    global miss_results_noorg_low
    global hit_results_low
    global assurance_low
    global mechanism_counter_low 
    
    while t_low < T_low:
        t_low = t_low + 1
        # The below line instructs the game to engage in the state change. 
        # If the state does not change, the individual guarantees a large payoff in period 1. 
        state_change_low = np.random.choice(D_low, size=game_low, p=gamma_probabilities_low)
        # If the state change does not occur, D = d = 0 and the game proceeds to the next step.
        # The large payoff is thus not guaranteed. 
        if d_low == state_change_low:
            outcome_low = np.random.choice(large_payoff_scheme_low,size=game_low, p=lambda_probabilities_low)
            if outcome_low == 0:
                #print("Period",t_low,":")
                #print("The large payoff has not been received.")
                #print("Your payoff is", m_low)
                miss_results_noorg_low = miss_results_noorg_low + 1
                hit_results_low = hit_results_low
                loser_low = float(m_low)
                GPN_low.append(loser_low)
                Time_Periods_low.append(t_low)
                 
            else:
                #print("Period",t_low,":")
                #print("The large payoff has been received.")
                #print("Your payoff is:", just_hit_payoff_low)
                hit_results_low = hit_results_low + 1
                miss_results_noorg_low = miss_results_noorg_low
                winner_low = float(just_hit_payoff_low)
                GPN_low.append(winner_low)
                Time_Periods_low.append(t_low)
                
        else:
            #print("Period",t_low,":")
            #print("The large payoff has not been received.")
            #print("Your payoff is:", m_low)
            miss_results_noorg_low = miss_results_noorg_low + 1
            hit_results_low = hit_results_low
            loser_low = float(m_low)
            GPN_low.append(loser_low)
            Time_Periods_low.append(t_low)

    cumulative_payout_GPN_low = list(accumulate(GPN_low))   
    print("You have missed", miss_results_noorg_low, "times and hit", hit_results_low, "times.")
    print("You have a individual payoffs of", GPN_low)
    print("You have cumulative payoffs of", list(accumulate(GPN_low)))
    print("Total Time Periods:", Time_Periods_low)
    
#####################################################################################################
# Medium Configuration - Agility Game with Reorganization
#####################################################################################################

"""
Medium Configuration - Agility Game with Reorganization
"""

# Loop Attempt #  
def agility_game_with_reorganization_medium():
    global t_medium
    global miss_results_reorg_medium 
    global hit_results_medium
    global mechanism_counter_medium
    global assurance_medium
        
    while t_medium < T_medium:
        t_medium = t_medium + 1
        #sum = sum + t
        if mechanism_counter_medium > assurance_medium:
            state_change_check_medium = np.random.choice(D_medium, size=game_medium, p=gamma_probabilities_medium)
            z_medium = state_change_medium
            mechanism_counter_medium = mechanism_counter_medium - 1
            if z_medium == state_change_check_medium:
                outcome_medium = np.random.choice(large_payoff_scheme_medium,size=game_medium, p=lambda_probabilities_medium)
                if outcome_medium == 0:
                    #print("Period",t_medium,":")
                    #print("The large payoff has not been received.")
                    #print("You will reorganize at the cost", ca_medium, "for a total payoff this period of", miss_medium)
                    miss_results_reorg_medium = miss_results_reorg_medium + 1
                    hit_results_medium = hit_results_medium
                    mechanism_counter_medium = mechanism_counter_medium + 1
                    loser_1_medium = float(miss_medium)
                    GPR_medium.append(loser_1_medium)
                    Time_Periods_medium.append(t_medium)
                else:
                    #print("Period",t_medium,":")
                    #print("The large payoff has been received.")
                    #print("Your payoff is:", just_hit_payoff_medium)
                    hit_results_medium = hit_results_medium + 1
                    miss_results_reorg_medium = miss_results_reorg_medium
                    winner_1_medium = float(just_hit_payoff_medium)
                    GPR_medium.append(winner_1_medium)
                    Time_Periods_medium.append(t_medium)
            else: 
                #print("Period",t_medium,":")
                #print("The large payoff has not been received.")
                #print("You will reorganize at the cost", ca_medium, "for a total payoff this period of", miss_medium)
                miss_results_reorg_medium = miss_results_reorg_medium + 1
                hit_results_medium = hit_results_medium
                mechanism_counter_medium = mechanism_counter_medium + 1
                loser_1_medium = float(miss_medium)
                GPR_medium.append(loser_1_medium)
                Time_Periods_medium.append(t_medium)
        # The below line instructs the game to engage in the state change. 
        # If the state does not change, the individual guarantees a large payoff in period 1.
        elif mechanism_counter_medium == assurance_medium: 
            state_change_medium = np.random.choice(D_medium, size=game_medium, p=gamma_probabilities_medium)
        # If the state change does not occur, D = d = 0 and the game proceeds to the next step.
        # The large payoff is thus not guaranteed. 
            if d_medium == state_change_medium:
                outcome_medium = np.random.choice(large_payoff_scheme_medium,size=game_medium, p=lambda_probabilities_medium)
                if outcome_medium == 0:
                    #print("Period",t_medium,":")
                    #print("The large payoff has not been received.")
                    #print("You will reorganize at the cost", ca_medium, "for a total payoff this period of", miss_medium)
                    miss_results_reorg_medium = miss_results_reorg_medium + 1
                    hit_results_medium = hit_results_medium 
                    mechanism_counter_medium = mechanism_counter_medium + 1
                    loser_1_medium = float(miss_medium)
                    GPR_medium.append(loser_1_medium)
                    Time_Periods_medium.append(t_medium)

                else:
                    #print("Period",t_medium,":")
                    #print("The large payoff has been received.")
                    #print("Your payoff is:", just_hit_payoff_medium)
                    hit_results_medium = hit_results_medium + 1
                    miss_results_reorg_medium = miss_results_reorg_medium 
                    winner_1_medium = float(just_hit_payoff_medium)
                    GPR_medium.append(winner_1_medium)
                    Time_Periods_medium.append(t_medium)
                
            else:
                #print("Period",t_medium,":")
                #print("The large payoff has not been received.")
                #print("You will reorganize at the cost", ca_medium, "for a total payoff this period of", miss_medium)
                miss_results_reorg_medium = miss_results_reorg_medium + 1
                hit_results_medium = hit_results_medium
                mechanism_counter_medium = mechanism_counter_medium + 1
                loser_1_medium = float(miss_medium)
                GPR_medium.append(loser_1_medium)
                Time_Periods_medium.append(t_medium)
                     
    print("You have missed", miss_results_reorg_medium, "times and hit", hit_results_medium, "times.")
    print("You have a individual payoffs of", GPR_medium)
    print("You have cumulative payoffs of", list(accumulate(GPR_medium)))
    print("Total Time Periods:", Time_Periods_medium)
        
#####################################################################################################

"""
Medium Configuration - Agility Game without Reorganization
"""

# Loop Attempt #
def agility_game_without_reorganization_medium():
    global t_medium
    global miss_results_noorg_medium
    global hit_results_medium
    global assurance_medium
    global mechanism_counter_medium 
    
    while t_medium < T_medium:
        t_medium = t_medium + 1
        # The below line instructs the game to engage in the state change. 
        # If the state does not change, the individual guarantees a large payoff in period 1. 
        state_change_medium = np.random.choice(D_medium, size=game_medium, p=gamma_probabilities_medium)
        # If the state change does not occur, D = d = 0 and the game proceeds to the next step.
        # The large payoff is thus not guaranteed. 
        if d_medium == state_change_medium:
            outcome_medium = np.random.choice(large_payoff_scheme_medium,size=game_medium, p=lambda_probabilities_medium)
            if outcome_medium == 0:
                #print("Period",t_medium,":")
                #print("The large payoff has not been received.")
                #print("Your payoff is", m_medium)
                miss_results_noorg_medium = miss_results_noorg_medium + 1
                hit_results_medium = hit_results_medium
                loser_medium = float(m_medium)
                GPN_medium.append(loser_medium)
                Time_Periods_medium.append(t_medium)
                 
            else:
                #print("Period",t_medium,":")
                #print("The large payoff has been received.")
                #print("Your payoff is:", just_hit_payoff_medium)
                hit_results_medium = hit_results_medium + 1
                miss_results_noorg_medium = miss_results_noorg_medium
                winner_medium = float(just_hit_payoff_medium)
                GPN_medium.append(winner_medium)
                Time_Periods_medium.append(t_medium)
                
        else:
            #print("Period",t_medium,":")
            #print("The large payoff has not been received.")
            #print("Your payoff is:", m_medium)
            miss_results_noorg_medium = miss_results_noorg_medium + 1
            hit_results_medium = hit_results_medium
            loser_medium = float(m_medium)
            GPN_medium.append(loser_medium)
            Time_Periods_medium.append(t_medium)
       
    print("You have missed", miss_results_noorg_medium, "times and hit", hit_results_medium, "times.")
    print("You have a individual payoffs of", GPN_medium)
    print("You have cumulative payoffs of", list(accumulate(GPN_medium)))
    print("Total Time Periods:", Time_Periods_medium)
    
#####################################################################################################
"""
High Configuration - Agility Game with Reorganization
"""
#####################################################################################################

# Loop Attempt #  
def agility_game_with_reorganization_high():
    global t_high
    global miss_results_reorg_high
    global hit_results_high
    global mechanism_counter_high
    global assurance_high
        
    while t_high < T_high:
        t_high = t_high + 1
        #sum = sum + t
        if mechanism_counter_high > assurance_high:
            state_change_check_high = np.random.choice(D_high, size=game_high, p=gamma_probabilities_high)
            z_high = state_change_high
            mechanism_counter_high = mechanism_counter_high - 1
            if z_high == state_change_check_high:
                outcome_high = np.random.choice(large_payoff_scheme_high,size=game_high, p=lambda_probabilities_high)
                if outcome_high == 0:
                    #print("Period",t_high,":")
                    #print("The large payoff has not been received.")
                    #print("You will reorganize at the cost", ca_high, "for a total payoff this period of", miss_high)
                    miss_results_reorg_high = miss_results_reorg_high + 1
                    hit_results_high = hit_results_high
                    mechanism_counter_high = mechanism_counter_high + 1
                    loser_1_high = float(miss_high)
                    GPR_high.append(loser_1_high)
                    Time_Periods_high.append(t_high)
                else:
                    #print("Period",t_high,":")
                    #print("The large payoff has been received.")
                    #print("Your payoff is:", just_hit_payoff_high)
                    hit_results_high = hit_results_high + 1
                    miss_results_reorg_high = miss_results_reorg_high
                    winner_1_high = float(just_hit_payoff_high)
                    GPR_high.append(winner_1_high)
                    Time_Periods_high.append(t_high)
            else: 
                #print("Period",t_high,":")
                #print("The large payoff has not been received.")
                #print("You will reorganize at the cost", ca_high, "for a total payoff this period of", miss_high)
                miss_results_reorg_high = miss_results_reorg_high + 1
                hit_results_high = hit_results_high
                mechanism_counter_high = mechanism_counter_high + 1
                loser_1_high = float(miss_high)
                GPR_high.append(loser_1_high)
                Time_Periods_high.append(t_high)
        # The below line instructs the game to engage in the state change. 
        # If the state does not change, the individual guarantees a large payoff in period 1.
        elif mechanism_counter_high == assurance_high: 
            state_change_high = np.random.choice(D_high, size=game_high, p=gamma_probabilities_high)
        # If the state change does not occur, D = d = 0 and the game proceeds to the next step.
        # The large payoff is thus not guaranteed. 
            if d_high == state_change_high:
                outcome_high = np.random.choice(large_payoff_scheme_high,size=game_high, p=lambda_probabilities_high)
                if outcome_high == 0:
                    #print("Period",t_high,":")
                    #print("The large payoff has not been received.")
                    #print("You will reorganize at the cost", ca_high, "for a total payoff this period of", miss_high)
                    miss_results_reorg_high = miss_results_reorg_high + 1
                    hit_results_high = hit_results_high
                    mechanism_counter_high = mechanism_counter_high + 1
                    loser_1_high = float(miss_high)
                    GPR_high.append(loser_1_high)
                    Time_Periods_high.append(t_high)

                else:
                    #print("Period",t_high,":")
                    #print("The large payoff has been received.")
                    #print("Your payoff is:", just_hit_payoff_high)
                    hit_results_high = hit_results_high + 1
                    miss_results_reorg_high = miss_results_reorg_high 
                    winner_1_high = float(just_hit_payoff_high)
                    GPR_high.append(winner_1_high)
                    Time_Periods_high.append(t_high)
                
            else:
                #print("Period",t_high,":")
                #print("The large payoff has not been received.")
                #print("You will reorganize at the cost", ca_high, "for a total payoff this period of", miss_high)
                miss_results_reorg_high = miss_results_reorg_high + 1
                hit_results_high = hit_results_high
                mechanism_counter_high = mechanism_counter_high + 1
                loser_1_high = float(miss_high)
                GPR_high.append(loser_1_high)
                Time_Periods_high.append(t_high)
    
  
    print("You have missed", miss_results_reorg_high, "times and hit", hit_results_high, "times.")
    print("You have a individual payoffs of", GPR_high)
    print("You have cumulative payoffs of", list(accumulate(GPR_high)))
    print("Total Time Periods:", Time_Periods_high)
        
#####################################################################################################

"""
High Configuration - Agility Game without Reorganization
"""
 
# Loop Attempt #
def agility_game_without_reorganization_high():
    global t_high
    global miss_results_noorg_high
    global hit_results_high
    global assurance_high
    global mechanism_counter_high 
    
    while t_high < T_high:
        t_high = t_high + 1
        # The below line instructs the game to engage in the state change. 
        # If the state does not change, the individual guarantees a large payoff in period 1. 
        state_change_high = np.random.choice(D_high, size=game_high, p=gamma_probabilities_high)
        # If the state change does not occur, D = d = 0 and the game proceeds to the next step.
        # The large payoff is thus not guaranteed. 
        if d_high == state_change_high:
            outcome_high = np.random.choice(large_payoff_scheme_high,size=game_high, p=lambda_probabilities_high)
            if outcome_high == 0:
                #print("Period",t_high,":")
                #print("The large payoff has not been received.")
                #print("Your payoff is", m_high)
                miss_results_noorg_high = miss_results_noorg_high + 1
                hit_results_high = hit_results_high
                loser_high = float(m_high)
                GPN_high.append(loser_high)
                Time_Periods_high.append(t_high)
                 
            else:
                #print("Period",t_high,":")
                #print("The large payoff has been received.")
                #print("Your payoff is:", just_hit_payoff_high)
                hit_results_high = hit_results_high + 1
                miss_results_noorg_high = miss_results_noorg_high
                winner_high = float(just_hit_payoff_high)
                GPN_high.append(winner_high)
                Time_Periods_high.append(t_high)
                
        else:
            #print("Period",t_high,":")
            #print("The large payoff has not been received.")
            #print("Your payoff is:", m_high)
            miss_results_noorg_high = miss_results_noorg_high + 1
            hit_results_high = hit_results_high
            loser_high = float(m_high)
            GPN_high.append(loser_high)
            Time_Periods_high.append(t_high)

    cumulative_payout_GPN_high = list(accumulate(GPN_high))   
    print("You have missed", miss_results_noorg_high, "times and hit", hit_results_high, "times.")
    print("You have a individual payoffs of", GPN_high)
    print("You have cumulative payoffs of", list(accumulate(GPN_high)))
    print("Total Time Periods:", Time_Periods_high)
      
#####################################################################################################
"""
Combined Configuration Reset

Run this code to perform additional iterations of the simulation
"""
#####################################################################################################

## Hard Reset ##

t_low = t_low + 1
miss_results_reorg_low = miss_results_reorg_low + 1
miss_results_noorg_low = miss_results_noorg_low + 1
hit_results_low = hit_results_low + 1
mechanism_counter_low = mechanism_counter_low + 1

t_medium = t_medium + 1
miss_results_reorg_medium = miss_results_reorg_medium + 1
miss_results_noorg_medium = miss_results_noorg_medium + 1
hit_results_medium = hit_results_medium + 1
mechanism_counter_medium = mechanism_counter_medium + 1

t_high = t_high + 1
miss_results_reorg_high = miss_results_reorg_high + 1
miss_results_noorg_high = miss_results_noorg_high + 1
hit_results_high = hit_results_high + 1
mechanism_counter_high = mechanism_counter_high + 1

if input() =="r":
    t_low = 0
    miss_results_reorg_low = 0
    miss_results_noorg_low = 0
    hit_results_low = 0
    mechanism_counter_low = 0
    GPN_low = []
    GPR_low = []
    Time_Periods_low = []
    
    t_medium = 0
    miss_results_reorg_medium = 0
    miss_results_noorg_medium = 0
    hit_results_medium = 0
    mechanism_counter_medium = 0
    GPN_medium = []
    GPR_medium = []
    Time_Periods_medium = []
    
    t_high = 0
    miss_results_reorg_high = 0
    miss_results_noorg_high = 0
    hit_results_high = 0
    mechanism_counter_high = 0
    GPN_high = []
    GPR_high = []
    Time_Periods_high = []
   
#####################################################################################################
"""
Low Configuration
"""
#####################################################################################################

# Starting the Game: 

if expected_reorganize_payoff_low > expected_no_reorganize_payoff_low:
    print(color.BOLD + "Low Game: Agility Game with reorganization." + color.END)
    agility_game_with_reorganization_low()
else:
    print(color.BOLD + "Low Game: Agility Game without reorganization." + color.END)
    agility_game_without_reorganization_low()
    
#####################################################################################################
"""
Medium Configuration
"""
#####################################################################################################

# Starting the Game: 

if expected_reorganize_payoff_medium > expected_no_reorganize_payoff_medium:
    print(color.BOLD + "Medium Game: Agility Game with reorganization." + color.END)
    agility_game_with_reorganization_medium()
else:
    print(color.BOLD + "Medium Game: Agility Game without reorganization." + color.END)
    agility_game_without_reorganization_medium()
    
#####################################################################################################
"""
High Configuration
"""
#####################################################################################################

# Starting the Game: 

if expected_reorganize_payoff_high > expected_no_reorganize_payoff_high:
    print(color.BOLD + "High Game: Agility Game with reorganization." + color.END)
    agility_game_with_reorganization_high()
else:
    print(color.BOLD + "High Game: Agility Game without reorganization." + color.END)
    agility_game_without_reorganization_high()

#####################################################################################################

# Graphing Configurations 
"""
Combined Configuration
"""

# Graph for Cumulative Payoffs - Lambda  

plt.plot(Time_Periods_low, list(accumulate(GPN_low)))
plt.plot(Time_Periods_medium, list(accumulate(GPN_medium)))
plt.plot(Time_Periods_high, list(accumulate(GPR_high)))
plt.ylabel("Cumulative Payoff")
plt.xlabel("Number of Time Periods")
plt.legend(['Low Lambda: 10%', 'Medium Lambda: 50%', 'High Lambda: 90%'])
#plt.zlabel("Lambda")
plt.show()

#####################################################################################################

"""
Combined Configuration
"""

# Graph for Cumulative Payoffs - Gamma

plt.plot(Time_Periods_low, list(accumulate(GPN_low)))
plt.plot(Time_Periods_medium, list(accumulate(GPN_medium)))
plt.plot(Time_Periods_high, list(accumulate(GPN_high)))
plt.ylabel("Cumulative Payoff")
plt.xlabel("Number of Time Periods")
plt.legend(['Low Gamma: 10%', 'Medium Gamma: 50%', 'High Gamma: 90%'])
#plt.zlabel("Lambda")
plt.show()

#####################################################################################################

"""
Combined Configuration
"""

# Graph for Cumulative Payoffs - Alpha

plt.plot(Time_Periods_low, list(accumulate(GPR_low)))
plt.plot(Time_Periods_medium, list(accumulate(GPN_medium)))
plt.plot(Time_Periods_high, list(accumulate(GPN_high)))
plt.ylabel("Cumulative Payoff")
plt.xlabel("Number of Time Periods")
plt.legend(['Low Alpha: 10%', 'Medium Alpha: 50%', 'High Alpha: 90%'])
#plt.zlabel("Lambda")
plt.show()

#####################################################################################################
"""
Combined Configuration
"""

# Graph for Cumulative Payoffs - small payout m 

plt.plot(Time_Periods_low, list(accumulate(GPN_low)))
plt.plot(Time_Periods_medium, list(accumulate(GPN_medium)))
plt.plot(Time_Periods_high, list(accumulate(GPN_high)))
plt.ylabel("Cumulative Payoff")
plt.xlabel("Number of Time Periods")
plt.legend(['Small Payout m: 1', 'Medium Payout m: 10', 'High Payout m: 20'])
#plt.zlabel("Lambda")
plt.show()

#####################################################################################################

"""
Combined Configuration
"""

# Graph for Cumulative Payoffs - Large Payoff M

plt.plot(Time_Periods_low, list(accumulate(GPN_low)))
plt.plot(Time_Periods_medium, list(accumulate(GPN_medium)))
plt.plot(Time_Periods_high, list(accumulate(GPR_high)))
plt.ylabel("Cumulative Payoff")
plt.xlabel("Number of Time Periods")
plt.legend(['Large Payoff M - Low Game: 1', 'Large Payoff M - Medium Game: 10', 'Large Payoff M - High Game: 100'])
#plt.zlabel("Lambda")
plt.show()
