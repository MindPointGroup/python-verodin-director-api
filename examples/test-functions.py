# Author: Nolan B. Kennedy (https://github.com/nxkennedy)
#
# MIT License
#
# Copyright (c) 2019 Nolan B. Kennedy
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from verodin.api import DirectorAPI

url = ''
username = ''
password = ''


# instantiate and build session object
d = DirectorAPI(url=url, username=username, password=password, insecure=True)


# Retrieve list of actions
def get_actions():
	actions = d.actions()
	print('\nList of actions')
	print('========')
	for action in actions:
		print(action['id'], action['name'])

# Executes an action
def execute_action():
	action = d.actions_execute(id=1165, attack_node=38, target_node=39)
	print(action)


# Retrieve single action
def get_single_action():
	#action = d.actions(id=1) # invalid action number to test handling
	action = d.actions(id=1165) # valid action number
	print('\nSingle action')
	print('========')
	print(action['sim_action']['id'], action['sim_action']['name']) # comes back in a weird 'sim_action' blob

# retrieve list of jobs
def get_jobs():
	jobs = d.jobs()
	print('\nList of jobs')
	print('========')
	for job in jobs:
		print(job)

# retrieve single job
def get_single_job():
	job = d.jobs(id=1)
	print('\nSingle job')
	print('========')
	print(job['id'], job['name'], job['status'])

# retrieve list of jobs
def get_actors():
	actors = d.actors()
	registered = actors['registered']
	print('\nList of actors')
	print('========')
	for actor in registered:
		print('id: {id} | hostname: {hostname} | desc: {desc}'.format(id=actor['id'],hostname=actor['hostname'],desc=actor['desc']))

# retrieve single job
def get_single_actor():
	actor = d.actors(id=44)
	print('\nSingle actor')
	print('========')
	print('id: {id} | hostname: {hostname} | desc: {desc}'.format(id=actor['id'],hostname=actor['hostname'],desc=actor['desc']))

def register_actor():
	actor = d.actors_create(security_zone_id=10, name="ExampleNetworkActor", comm_mode="Push", node_type="network")
	print(actor)



# what to test
#get_actions() #PASS
#execute_action() #PASS
#get_single_action() #PASS
#get_jobs() #PASS
#get_single_job() #PASS
#get_actors() #PASS
#get_single_actor() #PASS
#register_actor() #PASS
