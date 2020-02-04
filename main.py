from random import randint
import matplotlib.pyplot as plt

def GenProcess(np) :
	processes = []
	i = 1
	while i <= np:
		processes.append(i)
		i+=1
	return processes

def GenBurst(nb, x, y, z):
	
	print("------------------------------------------------------------------------------------------")
	print("Process["+str(nb)+"] = ")
	
	burst = []
	rburst = []
	Fper = nb*(x/100)
	Sper = nb*(y/100)
	Lper = nb*(z/100)
	i = 0
	j = 0

	while i < Fper :
		burst.append(randint(2,8))
		i+=1
	
	while i < Sper+Fper :
		burst.append(randint(20,30))
		i+=1
	
	while i < Lper+Sper+Fper :
		burst.append(randint(35,40))
		i+=1
	
	while j < nb :
		# a is index of process
		a = randint(0,nb-1)
		rburst.append(burst[a])
		burst.remove(burst[a])
		nb-=1
	print(rburst)
	print("------------------------------------------------------------------------------------------")

	return rburst 

def findWaitingTime(processes, n, bt, wt): 	
	wt[0] = 0
	# calculating waiting time 
	for i in range(1, n ): 
		wt[i] = bt[i - 1] + wt[i - 1] 

def findWaitingTimeRR(processes, n, bt, wt, quantum):
	
    rem_bt = [0] * n 
    for i in range(n):  
        rem_bt[i] = bt[i]
    t = 0 # Current time  
  
    while(1): 
        done = True

        for i in range(n): 
            
			#burst_time > 0 
            if (rem_bt[i] > 0) : 
                done = False # There is a pending process  
                  
                if (rem_bt[i] > quantum) : 
                    t += quantum  #total time to process 
                    rem_bt[i] -= quantum  # burst_time - quantum

                else: 
					#burst_time <= quantum
                    t += rem_bt[i]  
                    # time used by this process  
                    wt[i] = t - bt[i]  
                    # As the process gets fully executed  
                    rem_bt[i] = 0
                  
        # If all processes are done  
        if (done == True): 
            break

def findTurnAroundTime(processes, n,bt, wt, tat): 
	# calculating turnaround 
	for i in range(n): 
		tat[i] = bt[i] + wt[i] 

def findavgTimeFcfs(processes, n, bt): 
	# calculating average time
	wt = [0] * n 
	tat = [0] * n 
	total_wt = 0
	total_tat = 0
	
	# call function 
	findWaitingTime(processes, n, bt, wt) 				
	findTurnAroundTime(processes, n, bt, wt, tat) 

	# Display processes 
	print("----------------------------------First Come First Served---------------------------------")
	print("------------------------------------------------------------------------------------------")
	print( "Processes\t\tBurst time\t\tWaiting time\t\tTurn around time") 

	# Calculate total waiting time 
	# and total turn around time 
	for i in range(n): 
	
		total_wt = total_wt + wt[i] 
		total_tat = total_tat + tat[i] 
		print(" " + str(i + 1) + "\t\t\t\t" +
					str(bt[i]) + "\t\t\t\t" +
					str(wt[i]) + "\t\t\t\t\t " +
					str(tat[i])) 

	print( "Average waiting time = "+str(total_wt / n)) 
	print("Average turn around time = "+str(total_tat / n)) 
	print("\n")
	return total_wt / n

def findavgTimeSjf(processes, n, bt): 
	# calculating average time
	wt = [0] * n 
	tat = [0] * n 
	total_wt = 0
	total_tat = 0
	
	# call function 
	bt.sort()  #Shortest First
	findWaitingTime(processes, n, bt, wt) 				
	findTurnAroundTime(processes, n, bt, wt, tat) 

	# Display processes 
	print("------------------------------------------------------------------------------------------")
	print("----------------------------------Shortest Job First -------------------------------------")
	print("------------------------------------------------------------------------------------------")
	print( "Processes\t\tBurst time\t\tWaiting time\t\tTurn around time") 

	# Calculate total waiting time 
	# and total turn around time 
	for i in range(n): 
	
		total_wt = total_wt + wt[i] 
		total_tat = total_tat + tat[i] 
		print(" " + str(i + 1) + "\t\t\t\t" +
					str(bt[i]) + "\t\t\t\t" +
					str(wt[i]) + "\t\t\t\t\t " +
					str(tat[i])) 

	print( "Average waiting time = "+str(total_wt / n)) 
	print("Average turn around time = "+str(total_tat / n)) 
	print("\n")
	return total_wt / n

def findavgTimeRR(processes, n, bt, quantum) :

	# calculating average time
	wt = [0] * n 
	tat = [0] * n 

	# call function 
	findWaitingTimeRR(processes, n, bt, wt, quantum) 				
	findTurnAroundTime(processes, n, bt, wt, tat) 

	# Display processes
	print("------------------------------------------------------------------------------------------")
	print("------------------------------------- Round Robin ----------------------------------------")
	print("------------------------------------------------------------------------------------------")
	print( "Processes\t\tBurst time\t\tWaiting time\t\tTurn around time") 

	# Calculate total waiting time 
	# and total turn around time 
	total_wt = 0
	total_tat = 0
	for i in range(n): 
	
		total_wt = total_wt + wt[i] 
		total_tat = total_tat + tat[i] 
		print(" " + str(i + 1) + "\t\t\t\t" +
					str(bt[i]) + "\t\t\t\t" +
					str(wt[i]) + "\t\t\t\t\t " +
					str(tat[i])) 

	print( "Average waiting time = "+str(total_wt / n)) 
	print("Average turn around time = "+str(total_tat / n)) 
	print("\n")
	return total_wt / n

if __name__ =="__main__": 
# n is Number of processes
# quantum is time for each process (RR)
# processes is [1,2,3,...,n]
# burst_time is [random from Assumption]	
	n = 60
	quantum = 5
	processes  = GenProcess(n)
	burst_time = GenBurst(n, 70, 20, 10)
#find results
	# findavgTimeFcfs(processes, n, burst_time)
	# findavgTimeSjf(processes, n, burst_time)
	# findavgTimeRR(processes, n, burst_time, quantum)

#run for plotgraph	

	num = 10
	i = 0
	y = []
	f = []
	s = []
	r = []

#Assumtion1
	for i in range(num):
		y.append(i)
		f.append(findavgTimeFcfs(processes, n, GenBurst(n, 70, 20, 10)))
		s.append(findavgTimeSjf(processes, n, GenBurst(n, 70, 20, 10)))
		r.append(findavgTimeRR(processes, n, GenBurst(n, 70, 20, 10), quantum))

# #Assumtion2
# 	for i in range(num):
# 		y.append(i)
# 		f.append(findavgTimeFcfs(processes, n, GenBurst(n, 50, 30, 20)))
# 		s.append(findavgTimeSjf(processes, n, GenBurst(n, 50, 30, 20)))
# 		r.append(findavgTimeRR(processes, n, GenBurst(n, 50, 30, 20), quantum))

# #Assumtion2
# 	for i in range(num):
# 		y.append(i)
# 		f.append(findavgTimeFcfs(processes, n, GenBurst(n, 40, 40, 20)))
# 		s.append(findavgTimeSjf(processes, n, GenBurst(n, 40, 40, 20)))
# 		r.append(findavgTimeRR(processes, n, GenBurst(n, 40, 40, 20), quantum))

#plotgraph
	plt.plot(y, f)
	plt.plot(y, s)
	plt.plot(y, r)
	
	plt.title('Assumption ? Processes [?]')
	plt.xlabel('Number_Experiment')
	plt.ylabel('AverageWaitting_time')
	plt.show()