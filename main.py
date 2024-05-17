import datetime
import time

stress_points = {}

def check_stress_level(stress_level):
    
    if stress_level < 5:
        return 10  
    elif stress_level < 8:
        return 5    
    else:
        return 0    
def add_user(user_id: int) -> None:
    
    if user_id not in stress_points:
        stress_points[user_id] = 0

def update_stress_score(user_id: int, stress_level: int) -> None:
    
    points = check_stress_level(stress_level)
    if user_id in stress_points:
        stress_points[user_id] += points
    else:
        print(f"Usuário {user_id} não encontrado. Adicionando ao sistema.")
        add_user(user_id)
        stress_points[user_id] += points

def get_stress_score(user_id: int) -> int:
     
    return stress_points.get(user_id, 0)

def log_stress_level(user_id: int, stress_level: int) -> None:
     
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    points = check_stress_level(stress_level)
    print(f"{timestamp} - Usuário {user_id} registrou um nível de estresse de {stress_level} e ganhou {points} pontos.")
    update_stress_score(user_id, stress_level)

def Hours(range)
    hours = range(1, 13) 
     points = [5* h for in hours]
for h, p in zip (hours, points):
    print('hour %2i: %2i points' % (h, p))
    hours = range(6, 21)
     points = [10 * h for h in hours]
for h, p in zip(hours, points):
    print('Hour %2i: %2i points' % (h, p))
