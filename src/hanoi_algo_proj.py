def hanoi_solver(disks):
    rod_1 = list(range(disks,0,-1))
    rod_2, rod_3 = [], []
    display = f'{rod_1} {rod_2} {rod_3}'

    def move_disk(disks, from_rod, to_rod, extra_rod):
        nonlocal display
        if disks > 0:
            move_disk(disks - 1, from_rod, extra_rod, to_rod)
            if from_rod:
                extra_rod.append(from_rod.pop())
            display += f'\n{rod_1} {rod_2} {rod_3}'
            move_disk(disks - 1, to_rod, from_rod, extra_rod)

    move_disk(disks, rod_1, rod_2, rod_3)
    return display

if __name__ == "__main__":
    # test run
    print(hanoi_solver(2))
    #print(hanoi_solver(3))
    #print(hanoi_solver(4))
    #print(hanoi_solver(5))