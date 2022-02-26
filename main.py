class Tondeuse:
    """
        direction : initial direction
        x : intial x position
        y : intial y position
        x_final : x superieur
        y_final : y superieur
    """

    def __init__(self, x, y, direction, x_final, y_final):
        self.x = x
        self.y = y
        self.direction = direction
        self.x_final = x_final
        self.y_final = y_final

    # utilise pour changer la direction de la tondeuse
    def change_direction(self, new_direction):
        if self.direction == 'N' and new_direction == 'D':
            self.direction = 'E'
        elif self.direction == 'W' and new_direction == 'D':
            self.direction = 'N'
        elif self.direction == 'E' and new_direction == 'D':
            self.direction = 'S'
        elif self.direction == 'S' and new_direction == 'D':
            self.direction = 'W'
        elif self.direction == 'N' and new_direction == 'G':
            self.direction = 'W'
        elif self.direction == 'W' and new_direction == 'G':
            self.direction = 'S'
        elif self.direction == 'E' and new_direction == 'G':
            self.direction = 'N'
        elif self.direction == 'S' and new_direction == 'G':
            self.direction = 'E'

    # utilise pour deplacer la tondeuse
    def avance(self):
        if self.direction == 'N' and self.y < self.y_final:
            self.y = self.y + 1
        elif self.direction == 'E' and self.x < self.x_final:
            self.x = self.x + 1
        elif self.direction == 'S' and self.y > 0:
            self.y = self.y - 1
        elif self.direction == 'W' and self.x > 0:
            self.x = self.x - 1

    def print(self):
        print('Information: ', self.x, self.y, self.direction)


# code run start here

# open the file containing information about the macine
try:
    Input_file = open('input_file.txt', 'r')

    # read data from the file
    final_post = Input_file.readline()

    initial_post_T1 = Input_file.readline()
    instructions_T1 = Input_file.readline()

    initial_post_T2 = Input_file.readline()
    instructions_T2 = Input_file.readline()

    # intialise chaque tondeuse
    T1 = Tondeuse(int(initial_post_T1[0]), int(initial_post_T1[1]), initial_post_T1[2], int(final_post[0]),
                  int(final_post[1]))
    T2 = Tondeuse(int(initial_post_T2[0]), int(initial_post_T2[1]), initial_post_T2[2], int(final_post[0]),
                  int(final_post[1]))

    # execute section command for tondeuse 1
    for c in instructions_T1:
        if c == 'A':
            T1.avance()
        else:
            T1.change_direction(c)

    # execute section command for tondeuse 2
    for c in instructions_T2:
        if c == 'A':
            T2.avance()
        else:
            T2.change_direction(c)

    # print the result
    T1.print()
    T2.print()

except IOError:
    print("File not found or path is incorrect")
