# Copyright 2020 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import subprocess
import sys
import unittest

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class TestBQMFunctionality(unittest.TestCase):

    def test_smoke_bqm_conversion(self):
        """run bqm_conversion.py and check that nothing crashes"""

        demo_file = os.path.join(project_dir, 'BQM_Functionality/bqm_conversion.py')
        subprocess.check_output([sys.executable, demo_file])

    def test_smoke_bqm_offsets(self):
        """run bqm_offsets.py and check that nothing crashes"""

        demo_file = os.path.join(project_dir, 'BQM_Functionality/bqm_offsets.py')
        subprocess.check_output([sys.executable, demo_file])

    def test_smoke_general_program_bqm(self):
        """run general_program_bqm.py and check that nothing crashes"""

        demo_file = os.path.join(project_dir, 'BQM_Functionality/general_program_bqm.py')
        subprocess.check_output([sys.executable, demo_file])

class TestBasicPrograms(unittest.TestCase):

    def test_smoke_general_program_ising(self):
        """run general_program_ising.py and check that nothing crashes"""

        demo_file = os.path.join(project_dir, 'Basic_Programs/general_program_ising.py')
        subprocess.check_output([sys.executable, demo_file])

    def test_smoke_general_program_qubo(self):
        """run general_program_qubo.py and check that nothing crashes"""

        demo_file = os.path.join(project_dir, 'Basic_Programs/general_program_qubo.py')
        subprocess.check_output([sys.executable, demo_file])

if __name__ == '__main__':
    unittest.main()