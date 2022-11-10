def informacion():
    areas = ["cuina", 7.88, "menjador", 13.0, "terrassa", 20.34, "lavabo", 6.55, "habitació1", 7.98, "habitació2", 12, "rebedor", 4.23]
    print(areas[1])
    print(areas[len(areas)-1])
    print(areas[2])
    print(areas[1:4])
    print(areas[3:len(areas)])
    print(areas[9]+areas[11])
    areas[7] = 8
    print(areas[7])
    areas.append('pati interior')
    areas.append(2.78)
    print(areas)
    