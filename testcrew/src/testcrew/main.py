#!/usr/bin/env python
import sys
import warnings

from testcrew.crew import Testcrew

def run():
    inputs = {'documentation_url': 'https://documentation-using-ai-agent.readthedocs.io/en/latest/'}
    Testcrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()