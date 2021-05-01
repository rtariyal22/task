# Interesting problem that I have solved.
## Product Overview: 
- Our team manages a proprietary command line tool which is used by developers at Synopsys 
for building an testing there system design. It takes several steps to release a final build and each step requires some input from
user which affects the outcome of the build. Wrong input at any given stage can affect build in later stages. Apart from user input there are 
multiple other factors that can cause build to crash. 
## Problem Statement: 
- Whenever a build crashes, developer raises a ticket and one of us in the team is assigned the task to resolve 
the issue. We now look into build logs and find possible resolution.
In almost all the cases the reason of build crash is due to wrong user input or wrong environment settings.
The reason for a failure also changes overtime as it depends on various dynamic factors.
On an average we were getting around 35-40 tickets per week. We needed a solution to automate this as it was consuming lot of our time.
## Solution: 
- Since, we had a database of all past tickeks that we had resolved which contained build crash logs and resolution 
provided by our team. I proposed and built a system which now provides developer with a list of possible solutions to every 
build crashe immediately on there console. In our Query Resolver system we use ELK stack (ElasticSearch, Logstach and Kibana) 
for parsing errors and identifying matching solutions for a given crash the developer has encountered. After deploying 
this feature tickets raised by developers regarding build crashes has reduced to single digit. Which meant less 
support time and more time to do actual development for our team.

# Program that print numbers from 1 to 100 
- python number.py

# Uk postal number
## PostCode API -> UKPostcode
- E.g
- from postcode import UKPostcode
- try:
-    postCodeObj = UKPostcode('B1 1HQ')
- except ValueError:
-    print('Invalid postcode')
- else:
-    printing out postcode various segments
-    postCodeObj.printDetails()

## Running postcode api tests
- python test_postcode.py