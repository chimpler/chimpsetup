from datetime import datetime

import os
import subprocess
from setuptools import Command


class VersionsCommand(Command):
    user_options = [
        ('file=', 'f', 'file containing the versions')
    ]

    def initialize_options(self):
        self.file = None

    def finalize_options(self):
        if not self.file:
            raise Exception('file option must be provided')

    def run(self):
        versions = {
            'app_version': self.distribution.get_version(),
            'built_at': datetime.now()
        }

        if not os.path.exists('.git'):
            process = subprocess.Popen('git rev-parse HEAD', shell=True, stdout=subprocess.PIPE)
            if process.returncode == 0:
                versions['git_version'] = process.stdout.strip()

        with open(self.file, 'w') as fd:
            for key, value in versions.items():
                fd.write("{key} = '{value}'\n".format(key=key, value=value))


