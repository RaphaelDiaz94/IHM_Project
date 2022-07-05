import pytest
from app import app

def tests():

    assert app.config['TESTING'] == True
    assert app.config['DEBUG'] == False
    assert app.config['WTF_CSRF_ENABLED'] == False
    assert app.config['SECRET_KEY'] == 'secret'
    
