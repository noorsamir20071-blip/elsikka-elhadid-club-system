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


def print_player_info(p):
    print(f"\nPlayer: {p.name}")
    print(f"Number: {p.num}")
    print(f"Sport: {p.sport}")
    print(f"Speed: {p.speed}")
    print(f"Hand: {p.hand}")


def search_player(club_database):
    query = input("Enter name or jersey number to search: ").strip()
    found = False

    for p in club_database:
        if query.isdigit():
            if str(p.num) == query:
                print_player_info(p)
                found = True
        else:
            if query.lower() in p.name.lower():
                print_player_info(p)
                found = True

    if not found:
        print("❌ No player found with this name or number.")


# --- دالة تحديث الملف بعد المسح ---
def save_all_to_file(club_database):
    with open("club_data.txt", "w") as file:
        for p in club_database:
            p_type = "Football" if isinstance(p, FootballPlayer) else "Basketball"
            file.write(f"{p_type},{p.name},{p.speed},{p.hand},{p.num}\n")


# --- دالة مسح لاعب ---
def delete_player(club_database):
    query = input("Enter jersey number or exact name of player to DELETE: ").strip()
    player_to_remove = None

    for p in club_database:
        if (query.isdigit() and str(p.num) == query) or (p.name.lower() == query.lower()):
            player_to_remove = p
            break

    if player_to_remove:
        club_database.remove(player_to_remove)
        save_all_to_file(club_database)  # تحديث الملف أوفلاين
        print(f"✅ Player '{player_to_remove.name}' has been deleted successfully!")
    else:
        print("❌ Player not found.")


# --- تحميل البيانات من الملف عند بداية التشغيل ---
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


# --- القائمة الرئيسية ---
while True:
    print("\n Welcome to elsekka elhadid Club ")
    print("1. Add Basketball Player")
    print("2. Add Football Player")
    print("3. Show All Players & Actions")
    print("4. Search Player")
    print("5. Delete Player 🗑️")
    print("6. Exit")

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
        search_player(club_database)

    elif choice == "5":
        delete_player(club_database)

    elif choice == "6":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice.")