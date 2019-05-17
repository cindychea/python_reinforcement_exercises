def draw_shape(options):
    shape = ""

    for r in range(options['rows']):
        for c in range(options['cols']):
            shape += options['char']

        shape += "\n"


    return shape



print(draw_shape({'rows': 4, 'cols': 4,'char': '*'}))
print(draw_shape({'rows': 3, 'cols': 9,'char': '0'}))

# Pass in the appropriate argument when calling the function in order to generate the following output:

# ****
# ****
# ****
# ****
# Now pass in a different argument in order to generate the following output:

# 000000000
# 000000000
# 000000000