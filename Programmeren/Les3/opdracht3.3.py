def lang_genoeg(lengte):
    if lengte < 120:
        print('Je bent te klein')
    else:
        print('Je bent lang genoeg')

lengte = int(input('Wat is je lengte in cm?: '))
lang_genoeg(lengte)
