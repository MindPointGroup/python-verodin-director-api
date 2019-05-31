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
from time import sleep, time

## User Story ##
# login
# execute an action
# view the status of the job
# retrieve the results
####

start = time()
url = ''
username = ''
password = ''
src_actor = 38
dest_actor = 39
action_id = 1165

# build and instantiate Director object
verodin = DirectorAPI(url=url, username=username, password=password, insecure=True) # insecure is true because of busted SSL cert

# Get action name by id
action_name = verodin.actions(id=action_id)['sim_action']['name']
action_title = ' ({id}) - "{name}"'.format(id=action_id, name=action_name)

# execute action and store job id
print('\n[+] EXECUTING ACTION')
print('-----')
print('{title}'.format(title=action_title))
job = verodin.actions_execute(id=action_id, attack_node=src_actor, target_node=dest_actor)
job_id = job['id']

# monitor the status of the job
print('\n[+] ACTION STATUS MONITOR')
print('-----')
status = None
while status != 'completed':
	check_status = verodin.jobs(id=job_id)['status']
	print('\r STATUS: {update}   '.format(update=check_status), end='')
	status = check_status
	sleep(5)

# give the director 15s to correlate logs and results
seconds = 15
print('\n\n[+] WAITING FOR DIRECTOR TO CORRELATE LOGS & RESULTS')
print('-----')
while seconds >= 0:
	print('\r TIME: {seconds}s   '.format(seconds=seconds), end='')
	seconds -= 1
	sleep(1)

# View Results of Each Action in Job
results = verodin.jobs(id=job_id)['job_actions'][0] # Actions only have one job action indice, unlike Sequences or Evaluations
detected = results['detected']
blocked = results['blocked']
print('\n\n[+] RESULTS: {title}'.format(title=action_title))
print('-----')
print(' Detected? {x}'.format(x=detected))
print(' Blocked?  {x}'.format(x=blocked))

# If action was detected or blocked, show events
if detected or blocked:
	events = results['ja_events']
	print('---EVENTS---')
	for event in events:
		print(event)

end = time()
print('\n[+] Script Finished in {time}s'.format(time=round(end-start, 2)))
