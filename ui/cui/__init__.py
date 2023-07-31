import click
from config.language import language

@click.group()
def root_group():
    pass

def init():
    # Welcome to use
    print(language.WELCOME)
    
    root_group()