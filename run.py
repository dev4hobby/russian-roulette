from russian_roulette import Gun
if __name__ == '__main__':
    _g = Gun()
    print(_g.bullet)

    # execute till you satisfying..
    while not _g.broken:
        _g.shoot()

print("g'bye")
