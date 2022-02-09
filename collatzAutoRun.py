if __name__ == '__main__':

    def collatz_sequence(x):
        seq = [x]

        if x < 1:
            return []

        while x > 1:
            if x % 2 == 0:
                x = x / 2

            elif x % 2 == 1:
                x = x * 3 + 1
            x = int(x)
            seq.append(x)

        return seq



    number = 3 #starts testing at initial sequence of 2
    z = collatz_sequence(number)


    while z[-1] == 1:
        number += 1 #tests next number if sequencing ends at 1
        z = collatz_sequence(number)

        print(z)

        print('Ending Number: ' + str(z[-1]))

        print('Length: ' + str(len(z)))

