#storing functions in a list and displaying them one by one

def fun():
    print('you are in function 1')
def display():
    print('you are in function display')
def msg():
    print('messege')

l1=[fun,display,msg]
for ele in l1:
    ele()

    
