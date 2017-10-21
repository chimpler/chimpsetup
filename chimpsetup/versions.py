from datetime import datetime

import os
import subprocess
from setuptools import Command


class VersionsCommand(Command):
    git_commands = {
        'git_commit': 'git rev-parse HEAD',
        'git_branch': 'git rev-parse --abbrev-ref HEAD',
        'git_message': 'git log -1 --pretty=%B',
        'git_date': "git log -n 1 --pretty='format:%cd' --date=format:'%Y-%m-%d %H:%M:%S'",
        'git_tag': "git describe --exact-match --tags $(git log -n1 --pretty='%h')"
    }

    user_options = [
        ('file=', 'f', 'file containing the versions')
    ]

    def initialize_options(self):
        self.file = None

    def finalize_options(self):
        if not self.file:
            raise Exception('file option must be provided')

    def _execute_command(self, cmd):
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        process.wait()
        if process.returncode == 0:
            return process.stdout.read().strip()
        else:
            return None

    def run(self):
        versions = {
            'app_version': self.distribution.get_version(),
            'built_at': datetime.now()
        }

        git_versions = dict([(k, self._execute_command(v)) for k, v in self.git_commands.items()]) if os.path.exists('.git') else {}

        cleaned_versions = dict([(k, v) for k, v in versions.items() + git_versions.items() if v is not None and v != 'Undefined'])

        with open(self.file, 'w') as fd:
            for key, value in cleaned_versions.items():
                fd.write("{key} = '{value}'\n".format(key=key, value=value))


