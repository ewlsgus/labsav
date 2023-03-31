import os, sys
from pathlib import Path

sys.path.append(os.path.join(Path(__file__).resolve().parents[1], 'utilities'))

class Calculate():
    r'''Define useful utility functions'''
    def __init__(self):
        pass

    def get_super(self):
        return self