'''Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.'''

def array_diff(a, b):
    # your code here
    new = list()
    if len(a) >= len(b):
        for i in a:
            if i not in b:
                new.append(i)
        return (new)
    elif len(a) == 0 or len(b) ==0:
        new = []
        return new
    else:
        for i in b:
            if i not in a:
                new.append(i)
        return (new)
