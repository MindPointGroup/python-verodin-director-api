# Verodin Director API
A simple Python wrapper for the Verodin Director API
<br>
https://www.verodin.com/technology/platform

Author
--------
Nolan B. Kennedy (https://github.com/nxkennedy)

Features
--------

* An object oriented interface to the Verodin Director API
* Supports Action lookup, execution and results retrieval
* Supports job monitoring

Dependencies
--------------
Before you get started, make sure you have:

* Python >= 3.6 
* Installed requests (`pip3 install requests` or from this directory `pip3 install -r requirements.txt`)
* A Verodin Director account (Power User or System Admin privileges for best results)

Installation
-------------
     git clone https://github.com/nxkennedy/python-verodin-director-api.git

change directories to the newly cloned folder
     
Usage
-----
There is a sample script in the examples folder which will execute an action, monitor the job status, and retrieve the results. See below for specific examples.


### Getting started
First create a Verodin DirectorAPI object:
```python
from verodin.api import DirectorAPI
verodin = DirectorAPI(url='<https://director-url>', username='<username>', password='<password>')
```

If the Director's SSL cert is broken, the insecure flag can be set to override the errors (obviously not best practice):
```python
verodin = DirectorAPI(url='<https://director-url>', username='<username>', password='<password>', insecure=True)
```

### Get action name by id
We can retrieve the name of an action by calling the actions method
```python
action = verodin.actions(id=1165)
action_name = action['sim_action']['name']
```

### Execute an action and store job id
We can execute an action by using the actions_execute method
```python 
job = verodin.actions_execute(id=1165, attack_node=38, target_node=39)
job_id = job['id']
```

### Check the status of a job
Monitor the current status of a job by calling the jobs method
```python
monitor = verodin.jobs(id=11222)
status = monitor['status']
```

### Retieve the results of each action in the job
Retrieve the results of a job by calling the jobs method
```python
monitor = verodin.jobs(id=11222)
results = monitor['job_actions'][0]
detected = results['detected']
blocked = results['blocked']
if detected or blocked:
     events = results['ja_events']
     print('---EVENTS---')
     for event in events:
          print(event)
```

TODO
-----
* Add check to determine if job is currently running and that requested job is in queue
* Document additional module methods

