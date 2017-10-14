import pygit2
import os
import subprocess

def get_current_branch_name_from_repository(repository):
  return repository.head.shorthand

def get_push_command_for_branch(branch_name):
  branch_name = get_current_branch_name_from_repository(repository)
  return 'git push origin -f ' + branch_name

def get_origin_url():
  origin_url = str(subprocess.check_output(['git', 'remote', 'get-url', 'origin']), 'utf-8')
  return origin_url.replace('.git\n','')

def get_diff_url():
  return origin_url + '/compare/' + branch_name + '?expand=1'

if __name__ == "__main__":
  repository = pygit2.Repository('.')
  branch_name = get_current_branch_name_from_repository(repository)
  push_command = get_push_command_for_branch(repository)
  os.system(push_command)
  origin_url = get_origin_url()
  print('View diff at ' + get_diff_url())


# testing
