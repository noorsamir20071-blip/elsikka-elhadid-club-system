class player:
    sport = "basketball"
    players_per_team = 5

    def __init__(self, name, speed, hand, num):
        self.name = name
        self.speed = speed
        self.hand = hand   
        self.num = num 

    def dunk(self):
        print(f"🔥 Player {self.name} dunk the ball with his {self.hand} hand!")

    def pass_to(self, other_player):
        print(f"🎯 #{self.num} {self.name} passes the ball to {other_player.name}.")  

    def shoot(self):
        print(f"🏀 Player {self.name} shoots the ball with his {self.hand} hand!") 

    @classmethod
    def change_sport(cls, new_sport):
        cls.sport = new_sport

    @classmethod
    def change_team_size(cls, new_size):   
        cls.players_per_team = new_size                 


class FootballPlayer(player):
    sport = "football"
    
    def kick_ball(self):
        print(f"⚽ {self.name} kicks the ball with a powerful shot!")

    def shoot(self):
        print(f"⚽ {self.name} shoots the ball with his foot into the top corner!")
club_database = []
try:
    with open("club_data.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if len(data) == 5:
                p_type, name, speed, hand, num = data
                if p_type == "Basketball":
                    club_database.append(player(name, speed, hand, num))
                elif p_type == "Football":
                    club_database.append(FootballPlayer(name, speed, hand, num))
except FileNotFoundError:
    pass
while True:
    print("\n Welcome to elsekka elhadid Club ")
    print("1. Add Basketball Player")
    print("2. Add Football Player")
    print("3. Show All Players & Actions")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter Basketball Player name: ")
        speed = input("Enter speed: ")
        hand = input("Enter dominant hand: ")
        num = input("Enter jersey number: ")

        p = player(name, speed, hand, num)
        club_database.append(p)
        with open("club_data.txt", "a") as file:
         file.write(f"Basketball,{name},{speed},{hand},{num}\n")
        

    elif choice == "2":
        name = input("Enter Football Player name: ")
        speed = input("Enter speed: ")
        hand = "N/A"
        num = input("Enter jersey number: ")

        p = FootballPlayer(name, speed, hand, num)
        club_database.append(p)
        with open("club_data.txt", "a") as file:
         file.write(f"Football,{name},{speed},{hand},{num}\n")

    elif choice == "3":
        if not club_database:
            print("No players added yet.")
        else:
            for p in club_database:
                print(f"\nPlayer: {p.name}")
                print(f"Number: {p.num}")
                print(f"Sport: {p.sport}")

                p.shoot()

                if isinstance(p, FootballPlayer):
                    p.kick_ball()
                else:
                    p.dunk()

    elif choice == "4":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice.")