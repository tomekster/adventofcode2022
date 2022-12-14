
move = {
        #((vector), dir): ((position_change), (new_vector))
        ((0,0),'R'): ((0,0), (0,1)),
        ((0,0),'L'): ((0,0), (0,-1)),
        ((0,0),'U'): ((0,0), (-1,0)),
        ((0,0),'D'): ((0,0), (1,0)),

        ((0,1),'R'): ((0,1), (0,1)),
        ((0,1),'L'): ((0,0), (0,0)),
        ((0,1),'U'): ((0,0), (-1,1)),
        ((0,1),'D'): ((0,0), (1,1)),

        ((0,-1),'R'): ((0,0), (0,0)),
        ((0,-1),'L'): ((0,-1), (0,-1)),
        ((0,-1),'U'): ((0,0), (-1,-1)),
        ((0,-1),'D'): ((0,0), (1,-1)),

        ((1,0),'R'): ((0,0), (1,1)),
        ((1,0),'L'): ((0,0), (1,-1)),
        ((1,0),'U'): ((0,0), (0,0)),
        ((1,0),'D'): ((1,0), (1,0)),

        ((-1,0),'R'): ((0,0), (-1,1)),
        ((-1,0),'L'): ((0,0), (-1,-1)),
        ((-1,0),'U'): ((-1,0), (-1,0)),
        ((-1,0),'D'): ((0,0), (0,0)),




        ((1,1),'R'): ((1,1), (0,1)),
        ((1,1),'L'): ((0,0), (1,0)),
        ((1,1),'U'): ((0,0), (0,1)),
        ((1,1),'D'): ((1,1), (1,0)),

        ((-1,-1),'R'): ((0,0), (-1,0)),
        ((-1,-1),'L'): ((-1,-1), (0,-1)),
        ((-1,-1),'U'): ((-1,-1), (-1,0)),
        ((-1,-1),'D'): ((0,0), (0,-1)),

        ((1,-1),'R'): ((0,0), (1,0)),
        ((1,-1),'L'): ((1,-1), (0,-1)),
        ((1,-1),'U'): ((0,0), (0,-1)),
        ((1,-1),'D'): ((1,-1), (1,0)),

        ((-1,1),'R'): ((-1,1), (0,1)),
        ((-1,1),'L'): ((0,0), (-1,0)),
        ((-1,1),'U'): ((-1,1), (-1,0)),
        ((-1,1),'D'): ((0,0), (0,1))
}

S = set()
pos = (0,0)
S.add(pos)
vect = (0,0)

with open('input.txt') as f:
    for line in f:
        direction, n = line.split()
        n = int(n)
        for i in range(n):
            pos_change, vect = move[(vect, direction)]
            new_pos = (pos[0] + pos_change[0], pos[1] + pos_change[1])
            S.add(new_pos)
            pos = new_pos
            
print(len(S))
