import paramiko as paramiko

# START CONNECTION
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('18.133.122.116', 22, 'ec2-user', 'ec2-user', key_filename='key__git_ignore/gitme23key.pem')

# RUN COMMANDS
# stdin, stdout, stderr = ssh.exec_command("ls -a")
# lines = stdout.readlines()
# print(lines)

# UPLOAD

sftp = ssh.open_sftp()


def upload_file(file_source_path, file_destination_path):
    sftp.put(file_source_path, file_destination_path)


upload_file('batchFiles/create_csv.sh', 'create_csv.sh')
upload_file('batchFiles/script.py', 'script.py')
upload_file('batchFiles/run_scripts.sh', 'run_scripts.sh')

ssh.exec_command('./run_scripts.sh')

ssh.close()
