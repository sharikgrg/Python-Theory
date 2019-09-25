# functions and functional programs#
#functions are like a machine

# they take in arguments#
# they have a block of code to run
# they output (return) something (return)

# running and calling a function
# they need to be called to be executed

# Good practices:
    # good names (humans understand and descriptive)
    # following convention
    # constants are capitalised
    # They should be atomic and small
        # They should be testable
        # Reduces technical debt
    # comments when appropriate
    # Do not print in FUNCTIONS -- Return

# Functions allow us to be Dry
    # DON'T REPEAT YOURSELF

# Separation of concerns
# TDD

#Aim for cleaner, dryer and testable

def return_hey_to_zeus():
    return('Hey Zeus')
print(return_hey_to_zeus())
#
def full_name(f_name, l_name):
    full = f_name + ' ' + l_name
    return full

# this is the basis of all the test
    # set_up (give controlled inputs)
    # Assertion (check for expected outcomes)
    # Feedback output to our users
print(full_name('sharik', 'gurung') == 'sharik gurung')