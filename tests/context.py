"""
stolen by Bcl0c from python-guide.org.

This should make tests aware of the underlying folder structure.
"""

import os 
import sys

#long alpha line, damn.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#this WILL get confusing. I should have named that class better or something.
import irpf 

