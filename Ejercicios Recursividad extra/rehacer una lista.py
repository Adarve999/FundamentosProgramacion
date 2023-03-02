
def flatten(data):
    if data == []:
        final=[]
    else:
        if type(data[0]) == list:
            final=flatten(data[0]+flatten(data[1:]))
        else:
            