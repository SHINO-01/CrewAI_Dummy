#!/usr/bin/env python
import sys
import warnings

from testcrew.crew import Testcrew

def run():
    inputs = {'documentation_url': 'https://your-docs.readthedocs.io'}
    Testcrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()