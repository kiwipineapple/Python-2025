def greeting(name, *, anrede="Herr/Frau"):
    print(f"Hallo {anrede} {name}!")

greeting("Müller", anrede="Dr.")     # Hallo Dr. Müller!
greeting("Meier")                                # Hallo Herr/Frau Meier!


# greeting("Meier", "Professor") # TypeError