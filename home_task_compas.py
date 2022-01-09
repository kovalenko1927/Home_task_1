def direction(facing, turn):
    directions=['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    turns=turn//45

    start_idx=directions.index(facing)
    end_idx=(start_idx + turns) % len(directions)

    return directions[end_idx]

direction('S', 180)