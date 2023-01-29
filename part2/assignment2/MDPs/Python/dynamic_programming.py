mdp=open("mdp-10-5.txt","r")
mdp_data=mdp.readlines()
# print(len(mdp1_data))

n_states=int((mdp_data[0].split())[1])
# print(n_states)
n_actions=int((mdp_data[1].split())[1])
# print(n_actions)
gamma=float((mdp_data[-1].split())[-1])
# print(gamma)


transitions=[]
for i in range(2, len(mdp1_data)-1):
	line=mdp_data[i]
	line=line.split()
	tr_data={}
	tr_data["initial_state"]=int(line[1])
	tr_data["action_taken"]=int(line[2])
	tr_data["final_state"]=int(line[3])
	tr_data["reward"]=float(line[4])
	tr_data["transition_probability"]=float(line[5])
	
	transitions.append(tr_data)

# print(transitions)


vts=[0]*n_states
opt_action=[0]*n_states
end_flag=[0]*n_states
end_flag_check=[1]*n_states
# ite=0

while end_flag!=end_flag_check:
	# ite+=1
	
	for curr_state in range(n_states):

		# print(vt)
		val_action=[0]*n_actions
		act=[0]*n_actions
		for action in range(n_actions):
			
			for dic in transitions:				
				if (dic["initial_state"]==curr_state and dic["action_taken"]==action):
					val_action[action]+=dic["transition_probability"]*(dic["reward"]+gamma*vts[dic["final_state"]])
					act[action]=dic["action_taken"]
			
		vt1=max(val_action)
		opt_action[curr_state]=act[val_action.index(vt1)]
		if (vts[curr_state]==vt1):
			end_flag[curr_state]=1
		vts[curr_state]=vt1
# print(ite)
for i in range(n_states):
	print(vts[i], opt_action[i])
