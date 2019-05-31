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

import requests


class DirectorAPI:
	'''
	Director API object
	'''

	def __init__(self, url='', username='', password='', insecure=False):
		self.url = url
		self.username = username
		self.password = password
		self.insecure = insecure
		self.session = False

		if self.insecure and hasattr(requests, 'packages'):
			requests.packages.urllib3.disable_warnings()

		# configure our session block
		if self.username and self.password:
			session = requests.Session()
			session.auth = (self.username, self.password)
			if self.insecure:
				session.verify = False
			else:
				session.verify = True
			session.timeout = 30
			session.allow_redirects = False
			self.session = session

# ACTIONS ----------------------------------------------------------------------------------
	'''
	# Retrieves list of all actions (simulations) or json/dict of single action
	# METHOD: GET
	# .actions()
	# .actions(id=100)
	'''
	def actions(self, id=None):

		if id:
			path = '{url}/manage_sims/actions/{id}.json'.format(url=self.url, id=id)
		else:
			path = '{url}/manage_sims/actions.json'.format(url=self.url)

		response = self.session.get(path)
		# this is because the response will be a 500 error if the action id does not exist
		try:
			return response.json()

		except:
			print('\nERROR: \'{id}\' is not a valid action id'.format(id=id))
			exit(0)

#----------------------------------------------------------------------------------
	'''
        # Executes an action
        # METHOD: POST
        # .actions_execute(id=733, attack_node=1, target_node=2)
        '''
	def actions_execute(self, id=None, attack_node=None, target_node=None):
		path = '{url}/manage_sims/actions/{id}/run.json'.format(url=self.url, id=id)
		params = {
				'attack_node_id_1': attack_node,
				'target_node_id_1': target_node
				}
		response = self.session.post(path, data=params) # for some reason 'json=params' doesn't work so we pass as data
		return response.json()

# JOBS ----------------------------------------------------------------------------------
	'''
        # Retrieves list of all jobs or json/dict of single job
        # METHOD: GET
        # .jobs()
        # .jobs(id=100)
        '''
	def jobs(self, id=None):

		if id:
			path = '{url}/jobs/{id}.json'.format(url=self.url, id=id)
		else:
			path = '{url}/jobs.json'.format(url=self.url)

		response = self.session.get(path)
		return response.json()

# ACTORS ----------------------------------------------------------------------------------
	'''
	# Retrieves list of all nodes (actors) or json/dict of single node
        # METHOD: GET
        # .actors()
        # .actors(id=100)
        '''
	def actors(self, id=None):

		if id:
			path = '{url}/topology/nodes/{id}.json'.format(url=self.url, id=id)
		else:
			path = '{url}/topology/nodes.json'.format(url=self.url)

		response = self.session.get(path)
                # this is because the response will be a 500 error if the action id does not exist
		try:
			return response.json()

		except:
			print('\nERROR: \'{id}\' is not a valid actor id'.format(id=id))
			exit(0)

#----------------------------------------------------------------------------------
	'''
	# creates a pending actor
	# METHOD: POST
	# .actors_create(security_zone_id=1, name="ExampleNetworkActor", comm_mode="Push", node_type="network")
	'''
	def actors_create(self, security_zone_id=True, name='', comm_mode='', node_type=''):
		path = '{url}/nodes.json'.format(url=self.url)
		params = {
				'node': {
						'security_zone_id': security_zone_id,
						'name': name,
						'comm_mode': comm_mode,
						'node_type': node_type
						}
				}
		response = self.session.post(path, json=params)
		return response.json()

#----------------------------------------------------------------------------------
	''' @TODO this method requires testing
	'''
	# register a pending actor
	# METHOD: POST
	# .actors_register(security_zone_id=1, name="ExampleNetworkActor", comm_mode="Push", node_type="network")
	'''
	def actors_register(self, id='', mgmt_ip=''):
		path = '{url}/nodes/connect_result.json'.format(url=self.url)
		params = {
				'pending_node_id': id,
				'node': {
						'mgmt_ip': '{ip}'.format(mgmt_ip)
						}
                                }
		response = self.session.post(path, json=params)
		return response.json()
	'''


# MAP ----------------------------------------------------------------------------------
	'''
	# Retrieves map
	# METHOD: GET
	# .map()
	'''
	def map(self):
		path = '{url}/topology/map.json'.format(url=self.url)
		response = self.session.get(path)
		return response.json()



if __name__ == "__main__":
	print("Import the module. Do not call directly.")
