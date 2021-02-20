import paramiko

#   creating an ssh client object
ssh_client = paramiko.SSHClient()
# print(type(ssh_client))

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print('Connecting to 10.1.1.10')
ssh_client.connect(hostname='10.1.1.10', port='22', username='u1', password='cisco',
                   look_for_keys=False, allow_agent=False)
# Search for the options 'look_for_keys' and 'allow_agent' in paramiko documentation


# checking if the connection is active
print(ssh_client.get_transport().is_active())


print('Closing connection')
ssh_client.close()
