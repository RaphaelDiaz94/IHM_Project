import pytest
from app import app

def tests():

    assert app.config['TESTING']==True

    
    
