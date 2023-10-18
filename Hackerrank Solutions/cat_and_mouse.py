# Hackerrank

# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

def catAndMouse(x, y, z):
    xt = abs(z-x)
    yt = abs(z-y)
    
    if (xt == yt):
        return "Mouse C"
    elif (xt < yt):
        return "Cat A"
    else:
        return "Cat B"
