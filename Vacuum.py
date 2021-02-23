import numpy as np
import Environs
import Agency


def f_scoring(scores, agents, state):
    for i, agent in enumerate(agents):
        if agent.action != 'powerdown':
            scores[i] -= 1
        if agent.action == 'suck' and state[agent.loc[0], agent.loc[1]] == 1:
            scores[i] += 100
        if agent.action == 'powerdown' and (agent.loc-agent.home_loc).sum()!=0:
            scores[i] -= 1000

    #print("Score at the end of this episode is: ", scores)
    return scores


def f_homeless(scores, agents, state):
    for i, agent in enumerate(agents):
        if agent.action != 'powerdown':
            scores[i] -= 1
        if agent.action == 'suck' and state[agent.loc[0], agent.loc[1]] == 1:
            scores[i] += 100
    return scores

def f_action(agents, state):
    for agent in agents:
        if agent.action == 'suck':
            print("suck")
            state[agent.loc[0], agent.loc[1]] = 0
        elif (agent.action == 'move'
                and min(agent.loc + agent.bearing) >= 0
                and min(state.shape - agent.loc - agent.bearing) > 0
                and state[agent.loc[0] + agent.bearing[0],
                            agent.loc[1] + agent.bearing[1]] != 2):
            agent.loc += agent.bearing
        elif agent.action == 'rturn':
            # print("R")
            agent.bearing = [agent.bearing[1], -agent.bearing[0]]
        elif agent.action == 'lturn':
            #print("L")
            agent.bearing = [-agent.bearing[1], agent.bearing[0]]
    return state

def run_eval_environment(state, update, agents, performance):
    scores = [0 for _ in range(len(agents))]
    while any([agent.action != 'powerdown' for agent in agents]):
        for agent in agents:
            agent.get_percept(state)
            agent.program()
        scores = performance(scores, agents, state)
        state = update(agents, state)
    print("The average score of this episode is: ")
    #print("------------------------------------------------------------------------", scores)
    return scores


#agents = [Agency.EmptyRoomInternalStateReflexAgent(np.array([0,0]), np.array([0,0]), 'E')]
#agents = [Agency.BasicReflexAgent(np.array([0,0]), np.array([0,0]), 'E')]
#agents = [Agency.TrivialTableLookupAgent(np.array([0,0]), np.array([0,0]), 'E')]
#agents = [Agency.EmptyRoomInternalStateReflexAgent(np.array([0,0]), np.array([0,0]), 'E')]


my_list = [1,2,3,4,5,6,7,8,9,10]
print("\nEpisode 1: \n")
agents = [Agency.BasicReflexAgent(np.array([0,0]), np.array([0,0]), 'E')]
#print (run_eval_environment(Environs.LimitedRandom().grid, f_action, agents, f_scoring))
a1 = run_eval_environment(Environs.LimitedRandom().grid, f_action, agents, f_scoring)
print(a1)
my_list[0] = a1
print("-----------------------------------------------------------------------------------------------------")

print("\nEpisode 2: \n")
agents = [Agency.BasicReflexAgent(np.array([0,0]), np.array([0,0]), 'S')]
#print (run_eval_environment(Environs.LimitedRandom().grid, f_action, agents, f_scoring))
a2 = run_eval_environment(Environs.LimitedRandom().grid, f_action, agents, f_scoring)
print(a2)
my_list[1] = a2
print("-----------------------------------------------------------------------------------------------------")


print("\nEpisode 3: \n")
agents = [Agency.BasicReflexAgent(np.array([0,0]), np.array([0,0]), 'N')]
#print (run_eval_environment(Environs.LimitedRandom().grid, f_action, agents, f_scoring))
a3 = run_eval_environment(Environs.LimitedRandom().grid, f_action, agents, f_scoring)
print(a3)
my_list[2] = a3
print("-----------------------------------------------------------------------------------------------------")


print("\nEpisode 4: \n")
agents = [Agency.BasicReflexAgent(np.array([1,1]), np.array([1,1]), 'N')]
#print (run_eval_environment(Environs.LimitedRandom().grid, f_action, agents, f_scoring))
a4 = run_eval_environment(Environs.LimitedRandom().grid, f_action, agents, f_scoring)
print(a4)
my_list[3] = a4
print("-----------------------------------------------------------------------------------------------------")

print("\nEpisode 5: \n")
agents = [Agency.BasicReflexAgent(np.array([1,1]), np.array([1,1]), 'N')]
#print (run_eval_environment(Environs.LimitedRandom().grid, f_action, agents, f_scoring))
a5 = run_eval_environment(Environs.LimitedRandom().grid, f_action, agents, f_scoring)
print(a5)
my_list[4] = a5
print("-----------------------------------------------------------------------------------------------------")

print("\nEpisode 6: \n")
agents = [Agency.BasicReflexAgent(np.array([1,1]), np.array([1,1]), 'N')]
#print (run_eval_environment(Environs.LimitedRandom().grid, f_action, agents, f_scoring))
a6 = run_eval_environment(Environs.LimitedRandom().grid, f_action, agents, f_scoring)
print(a6)
my_list[5] = a6
print("-----------------------------------------------------------------------------------------------------")

print("\nEpisode 7: \n")
agents = [Agency.BasicReflexAgent(np.array([1,1]), np.array([1,1]), 'N')]
#print (run_eval_environment(Environs.LimitedRandom().grid, f_action, agents, f_scoring))
a7 = run_eval_environment(Environs.LimitedRandom().grid, f_action, agents, f_scoring)
print(a7)
my_list[6] = a7
print("-----------------------------------------------------------------------------------------------------")

print("\nEpisode 8: \n")
agents = [Agency.BasicReflexAgent(np.array([1,1]), np.array([1,1]), 'N')]
#print (run_eval_environment(Environs.LimitedRandom().grid, f_action, agents, f_scoring))
a8 = run_eval_environment(Environs.LimitedRandom().grid, f_action, agents, f_scoring)
print(a8)
my_list[7] = a8
print("-----------------------------------------------------------------------------------------------------")

print("\nEpisode 9: \n")
agents = [Agency.BasicReflexAgent(np.array([1,1]), np.array([1,1]), 'N')]
print (run_eval_environment(Environs.LimitedRandom().grid, f_action, agents, f_scoring))
a9 = run_eval_environment(Environs.LimitedRandom().grid, f_action, agents, f_scoring)
print(a9)
my_list[8] = a9
print("-----------------------------------------------------------------------------------------------------")

print("\nEpisode 10: \n")
agents = [Agency.BasicReflexAgent(np.array([1,1]), np.array([1,1]), 'N')]
#print (run_eval_environment(Environs.LimitedRandom().grid, f_action, agents, f_scoring))
a10 = run_eval_environment(Environs.LimitedRandom().grid, f_action, agents, f_scoring)
print(a10)
my_list[9] = a10
print("-----------------------------------------------------------------------------------------------------")

# Print the average
total = 0
#for r in my_list:
    #total = total + my_list[r]

#print("Average score across ten episodes: ",(a1+a2+a3+a4+a5+a6+a7+a8+a9+a10)/10)
#print("Average score across ten episodes: ", total)