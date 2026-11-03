# INFO-H420 Process Modeling, Data Pipelines, and Responsible AI 

Assignment 2: Business Process Analysis and Redesign (10 points) 

Consider the following business process. 

_An IT helpdesk handles requests from clients. The clients are employees of a company. There are about 500 employees in total. A request may be an IT-related problem of a client or an access request (e.g., requesting rights to access a system)._ 

_A client calls the help desk or sends an email in order to make a request. The help desk is staffed with 5 Level-1 support staff who, typically, are junior people with less than 12 months experience, but are capable of resolving known problems. The hourly cost of a Level-1 staff member is € 40._ 

_When the Level-1 employee does not know the resolution to a request, the request is forwarded to a more experienced Level-2 support staff. There are 3 Level-2 staff members and their hourly cost is € 60. When a Level-2 employee receives a new request, he or she evaluates it in order to assign a priority level._ 

_Once the request is assigned to a Level-2 staff member, the request is researched by the Level-2 employee and a resolution is developed and sent back to the Level-1 employee. Eventually, the Level-1 employee forwards the resolution to the client who tests the resolution. The client notifies the outcome of the test to the Level-1 employee via email. If the client states that the request is fixed, it is marked as complete and the process ends. If the request is not fixed, it is resent to Level-2 support for an further resolution action._ 

Assume the following. 

- _Requests spend on average 1 h waiting for a Level-1 staff member to check them._ 

- _Checking if a new request is known takes on average 10 min. In 20% of the cases, the request is known. In this case, it takes on average 5 min (st. dev 3 min) for the Level-1 staff member to communicate the resolution to the client. Once this is done, the request is marked as “closed”. On the other hand, if the request is not known, the request is automatically forwarded to Level-2._ 

- _New requests spend on average 2 h waiting for a Level-2 staff member to evaluate them. Level-2 staff take on average 20 min to evaluate a new request._ 

- _The time between the moment a request has been prioritized and the moment the request is picked up by a Level-2 staff member is 20 h._ 

- _The time required to research and resolve a request is on average 2 h._ 

- _The time to write the resolution to a request is on average 20 min._ 

- _Once a Level-2 staff member has written the resolution of a request, it takes on average 20 h before the request is fetched from the ticketing system by a Level-1 staff member._ 

- _It takes on average 20 min (st. dev. 5 min) for a Level-1 staff member to send to the client a problem resolution previously written by a Level-2 staff member._ 

- _It takes on average 20 h between the moment a resolution is sent by the Level-1 staff member and the moment the client emails the test results back to the Level-1 staff._ 

- _In 20% of the cases, the request is not resolved and it needs to be forwarded to Level2 again. In this latter case, it takes exactly 2 min for the Level-1 staff to forward the request to the Level-2 staff._ 

- _There are no other costs besides the resource costs._ 

## Exercise 1 _(2 points)_ 

Consider the BPMN diagram provided. Calculate the cycle time efficiency and the cost-perexecution of the as-is process. To calculate processing time and cost, only take into consideration time spent doing actual work, excluding waiting times and handoffs. 

## Exercise 2 _(2 points)_ 

Consider the Level-2 IT service desk, and assume that the number of requests reaching Level2 is one per hour. How many Level-2 staff members are required in order to ensure that the mean waiting time of a request is less than two working hours? 

## Exercise 3 _(2 points)_ 

Simulate the business process. When describing the simulation, ignore all internal waiting times, but model the waiting time for receiving the response from the client. Assume there are 4 requests submitted per hour. Experiment with different levels of resources, and discuss your findings. 

## Exercise 4 _(2 points)_ 

Identify issues in this process and organize them in an issue register. Then, propose a set of changes to improve this process. For each change, identify the Redesign Heuristics used and give a justification for the change (i.e., what issue(s) is it addressing?). 

## Exercise 5 _(2 points)_ 

Use these changes or a subset thereof to draw a possible “to be” process model. 

## Instructions 

The assignment contributes 10% to the overall grade (i.e., 2/20). 

This assignment is to be made in **groups of three** persons. You are asked to form the groups via “Groups for Assignment 2” on the Université Virtuelle (UV). If you cannot find a partner, 

please post a request in the “Discussion Forum” on UV. You should not form the same group as in the previous assignment. 

You are asked to submit a short **report** presenting your solution to the exercises, including justifications for the choices and assumptions made. 

The report has to be uploaded as a pdf file to “Assignment 2” on UV by **October 26** , 2026. 

