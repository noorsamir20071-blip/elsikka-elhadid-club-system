"""
class car:
    def __init__(self ,name,brand):

        self.name=name

        self.brand=brand

    def generate_response(self):
        return f"This is {self.brand} {self.name}."

       

car1 = (input("Enter your car name: "))
car2 = (input("Enter your car brand: "))
my_awesome_car = car(car1, car2)
print(my_awesome_car.generate_response())
"""


class player:
    sport = "basketball"
    players_per_team = 5
    def __init__(self,name,speed,hand,num):
        self.name=name
        self.speed=speed
        self.hand=hand   
        self.num=num 
    def dunk(self):
        print(f"🔥 Player {self.name} dunk the ball with his {self.hand} hand!")
    def pass_to(self, other_player):
        print(f"🎯 #{self.num} {self.name} passes the ball to {other_player.name}.")  
    def shoot(self):
        print(f" Player {self.name} shoots the ball with his {self.hand} hand!  ") 
    @classmethod
    def change_sport(cls, new_sport):
        cls.sport=new_sport
    @classmethod
    def change_team_size(cls, new_size):   
        cls.players_per_team = new_size   
class FootballPlayer(player):
    def kick_ball(self):
        print(f"⚽ {self.name} kicks the ball with a powerful shot!")  
    def shoot(self):
        print(f"⚽ {self.name} shoots the ball with his foot into the top corner!")                        
player1=player("yassin",80,"right",77)
player2=player("ammar",84,"right",2)
player3=player("kanton",90,"left",4)
foot_player = FootballPlayer("Salah", 95, "left", 11)
print(f"🏀 Player 1: {player1.name} | Speed: {player1.speed} | Hand: {player1.hand} | Shirt: #{player1.num} | Sport: {player1.sport}")
print(f"🏀 Player 2: {player2.name} | Speed: {player2.speed} | Hand: {player2.hand} | Shirt: #{player2.num} | Sport: {player2.sport}")
print(f"🏀 Player 3: {player3.name} | Speed: {player3.speed} | Hand: {player3.hand} | Shirt: #{player3.num} | Sport: {player3.sport}")
player2.dunk() 
player3.dunk() 
player2.pass_to(player1)
player1.dunk()
player3.pass_to(player1) 
player2.shoot()
player2.pass_to(player1)
player3.dunk()
foot_player.pass_to(player1) 
foot_player.kick_ball()
foot_player.shoot()

player.change_sport("ugly football")
print(f"Yassin now plays: {player1.sport}")
print(f"Ammar now plays: {player2.sport}")

player.change_team_size(7)
print(f"New team size for Yassin is: {player1.players_per_team}")
print(f"New team size for Ammar is: {player2.players_per_team}")

match_players = [player1, foot_player]
print("\n--- 🏁 Polymorphism Match Showcase 🏁 ---")
for p in match_players:
    p.shoot()


        
        
        