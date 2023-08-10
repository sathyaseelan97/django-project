from django import template

#This file is to define functions for the custom filter used in this application

register = template.Library()

@register.filter(name='slice')
def cut(value,arg):

    """
    This cuts out all of values of 'arg' from the string
    """
    #assuming value to be string
    return value.replace(arg,'')

#Registering the filter to template library
#first 'cut' denotes to the name of the filter to be called
# second denotes the function against which we want to register the template
# Below is one way of registering the filter other way is by using decorators

#register.filter('slice',cut)
