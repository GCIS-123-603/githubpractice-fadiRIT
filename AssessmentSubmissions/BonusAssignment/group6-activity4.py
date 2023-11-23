'''
GCIS-123.603
    Prof. Mehtab Khurshid.

Group 6 : 
    Mohamad Dakwar
    Aamna Fathima Manyar
    Abdullah Alblooshi


Starting work at Gostco as a senior developer on the Cineplexo Project. 
Our task is to set up an application that enables us to schedule task of the developers on our team, to complete development and minimize time.

For each task, we know what tasks have to be completed. So we need to schedule certain tasks before another.


Let's consider the following Scenarios :

-   Scenario 1
        Three tasks, with the following dependencies:
        T3 : T1, T2
        T2 : T1
        T1 : 

        To complete T3, T1 and T2 have to be completed, to complete T2, T1 has to be completed. To complete all the tasks, the application would schedule it in the following way:
        [T1,T2,T3] in order.

-   Scenario 2
        Now 3 more tasks, with the following dependancy.
        T3 : T2
        T2 : T1, T3
        T1 : 

        The application will be unable to schedule any tasks and should return an empty schedule, due to the incorrect dependency.

-   Scenario 3
        This one consists of 4 tasks rather than 3.
        T3 : T2
        T2 : T1
        T1 :
        T0 :

        The application can schedule to make it [T0,T1,T2,T3] or [T1,T0,T2,T3]

-   Scenario 4
        Consider 4 tasks with the following dependcies.
        T4 : T3
        T3 : T2, T1
        T2 : T1
        T1 :

After Careful considerations of the scenarios, we've decided to come up with the following functions as per the activity.

mirror()
    A function that will literally mirror the dictionary and swap certain values, as shown in teh output.

remove_value()
    A function that given certain parameters will be able to remove certain values and return a fixed list.

schedule()
    A function that can schedule the tasks after any values are removed, making everything possible.

define_dependencies()
    A function that we made to summarize all 4 scenarios in a unique way, it uses a for loop to loop through certain scenarios.

    
    Overall, all of these functions accomplish the main goals of the activity, and work successfully.

    
A summary of the program is that it essentially takes the dependencies from a certain scenarios, then it mirrors them, then removes any certain tasks that have to be removed, then uses the schedule function to schedule them.
We've successfully been able to implement them, firstly by using our define_dependencies function which contains all the dependencies.
Following that we have our mirror() function which we used to mirror it successfully. Following that, we used the remove to remove certain tasks, and then finally.
The Schedule function which we used to dictate how a certain tasks or task flow will go.



'''




# ?

# Left Empty On Purpose !

# ? 

'''
!   !   !

-   -   -   CORE FUNCTIONS FOR FUNCTIONALITY OF THE PROGRAM BELOW   -   -   - 

!   !   !
'''
def define_dependencies(i):# making of the dictionary , 4 scenarios 
        
        #This whole function works by a loop, it might seem a bit weird but it works perfectly.
        #It allows to keep track of any task dependeicies as well.
        
        if i==0: 
            tasks_dependencies = {'T3': ['T1', 'T2'],'T2': ['T1'],'T1': []} #scenario 1
            return tasks_dependencies
        elif i==1:
            tasks_dependencies = {'T3': ['T2'],'T2': ['T1','T3'],'T1': []} #scenario 2
            return tasks_dependencies
        elif i==2:
            tasks_dependencies = {'T3': ['T2'],'T2': ['T1'],'T1': [],'T0' :[]} #scenario 3
            return tasks_dependencies
        else:
            tasks_dependencies = {'T4': ['T3'],'T3': ['T1','T2'],'T2': ['T1'],'T1' :[]} #scenario 4
            return tasks_dependencies
        # so loop takes scenarios one by one and executes mirror,remove,schedule func. on them
def mirror(tasks_dependencies):
    dependency_tasks = {} # declaring a empty dict. to store swapped values and keys
    for key, value in tasks_dependencies.items():# going through every key-value pair in the original dict.
        for i in value:
            if i not in dependency_tasks:# just checking to see that task is not in the mirrored(swapped one) dict.
                #if it's not , we add it with the current key as the only dependency
                dependency_tasks[i] = [key]
            else:
                dependency_tasks[i].append(key)#so if the task is already in mirrored dict.
                #then append the current key to its list of dependencies

    return dependency_tasks # contains all mirrored(swapped) keys-values dict.
def remove_value(list_O_tasks,certain_task_ToBeRemoved,the_dictionary):
    
    #Initializing empty list with new tasks in it.
    new_tasks = []
    
    #Now we are going to loop through it
    for task in list_O_tasks:
        #more looping through the tasks in a dictionary
        if task in the_dictionary:
            #creating a new value list to be used for appending
            new_value = []
            #looping through values in the dictionary at a certain task
            for value in the_dictionary[task]:
                #if the value isnt equal to the specific task we want, we append it to our list of new values
                if value != certain_task_ToBeRemoved:
                    new_value.append(value)
                #allow a certain index to become new value
                the_dictionary[task]= new_value
                #if it isnt its appended to the new tasks list
                if not the_dictionary[task]:
                    new_tasks.append(task)
    #reutrning new tasks after completion
    return new_tasks
def schedule(dependencies):
    if not dependencies:#checking if the original dict. is empty
        #if it is , then we simply return an empty list
        return []

    scheduled_tasks = [] #initializing a list to store sorted tasks
    swapped_dict = mirror(dependencies)#creating a dict. of mirrored dependencies
    no_prereqs = []#just to check if you have a list of tasks with no prerequisites

    for task in no_prereqs:#going through tasks with no prerequisites
        scheduled_tasks.append(task)#adding the task to  scheduled tasks list
        
        del dependencies[task]#removing the task from the dependencies dictionary
        for mirror_task, mirror_dependencies in swapped_dict.items():#updating dependencies for other tasks based on the removal
            remove_value(mirror_dependencies, task, dependencies)

    remaining_tasks = list(dependencies.keys())
    remaining_tasks.sort()#just sorting the list
    scheduled_tasks.extend(remaining_tasks)#adding the remaining tasks to the scheduled tasks list
    return scheduled_tasks# finally returning a list of scheduled tasks ( its sorted btw )
'''
!   !   !

-   -   -   CORE FUNCTIONS FOR FUNCTIONALITY OF THE PROGRAM ABOVE   -   -   -

!   !   !
'''

# ?

# Left Empty On Purpose !

# ? 
'''
*       *   *       *       *   *       *       *   *       *

    *   M A I N     F U N C T I O N     B E L O W   *

*       *   *       *       *   *       *       *   *       *
'''
def main():
    for i in range(4):#4 scenarios 

        print("Scenario :",i+1,"\n") 
        dependencies = define_dependencies(i) # so original dict. is stored/returned in 'dependencies'
        print("Original:", dependencies,"\n") #just making the code more understandable/feasible to viewer

        swapped = mirror(dependencies) # using the swapping/mirroring func.
        print("After Application Of Mirroring Function:", swapped,"\n")
    
        remove = ['T3', 'T2'] # tasks to remove
        Tx = 'T1'
        updated_tasks_post_removal = remove_value(remove, Tx, dependencies) # running the remove func.

        print("After Application Of Removal Function",updated_tasks_post_removal,"\n")

        schedule_list_whichis_sorted_ofcourse=schedule(dependencies)

        print("After Application Of Schedule Function :" ,schedule_list_whichis_sorted_ofcourse,"\n") 
        print("*******************************************************************************")



if __name__ == "__main__":
    main()
