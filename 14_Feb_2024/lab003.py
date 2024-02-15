def makepizza(*topings):
    for toping in topings:
        print(toping)


makepizza('onion', 'tomato')
makepizza('onion', 'tomato', 'corn')
makepizza('onion', 'tomato', 'olive')
makepizza('onion', 'tomato', 'olive', 'pineapple')


def make_pizza_base(*topings, base):
    print(topings, base)
    for i in topings:
        print(i)
    print(base)

make_pizza_base('onion', 'mashroom', 'olives', base = "thin")

def make_pizza(*topings, base = 'wheat'):
    print(topings, base)
    for top in topings:
        print (top)
    return top, base

top1, top2 = make_pizza("onion", 'tomato', 'mashroom')
print(top1)
print(top2)