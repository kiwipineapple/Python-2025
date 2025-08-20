def beispiel(a,*args, **kwargs ):
    print("a:", a)
    print("args:", args)
    print("kwargs:", kwargs)

beispiel(10,50, 20, 30,40, name="Max", beruf="Dozent")
