""" Creating a simple random name generator, using Fictional TV character names """
import random

def main():
    """
        In contrast to the book project, this script contains full names that must be
        split into first and lastname lists, based on the space between names.
    """
    famous_tv_cops = ['Frank Columbo', 'Brenda Johnson', 'Lennie Briscoe',
    'Frank Drebin', 'Joe Friday', 'Pete Malloy', 'Jim Reed', 'Hank Schrader',
    'Clancy Wiggum', 'Vic Mackey', 'Ray Holt', 'Olivia Benson', 'Barney Fife',
    'Andy Sipowicz', 'Rustin Cohle', 'Martin Hart', 'Carl Winslow', 'James Crockett',
    'Ricardo Tubbs', 'Barney Miller', 'Christine Cagney', 'Mary Lacey', 'Horatio Caine',
    'David Starsky', 'Kenneth Hutchinson', 'Mike Stone', 'Steve Keller', 'Vince Masuka',
    'Jim Dangle', 'Travis Junior', 'Trudy Wiegel', 'Frank Rizzo', 'Andrew Blake',
    'Henry Callahan', 'John McClane', 'Martin Riggs', 'Thomas Magnum', 'Leroy Gibbs',
    'Jake Peralta', 'Rosco Coltrane', 'James Gordon', 'John Munch', 'Roger Murtaugh',
    'Andy Taylor', 'Danny Reagan', 'Buford Justice', 'Frank Bulitt', 'Axel Foley',
    'Virgil Tibbs', 'Nicholas Angel', 'Jimmy McNulty', 'Jim Malone', 'Kate Beckett',
    'Joe Friday', 'Jim Rockford', 'Martin Brody', 'Sonny Crockett']


    firstnames = []
    lastnames = []

    #remove duplicates by converting to dict(no dups allowed) and back to list
    famous_tv_cops = list(dict.fromkeys(famous_tv_cops))

    for name in famous_tv_cops:
        f_name, l_name = name.strip().split()
        firstnames.append(f_name)
        lastnames.append(l_name)


    while True:
        firstname = random.choice(firstnames)
        lastname = random.choice(lastnames)

        print("Your random name: %s %s \n\n" % (firstname, lastname))

        user_input = input("Generate another name? Press y to continue:\t")
        if user_input.lower() != 'y':
            break

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
