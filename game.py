import time
import random

def start_game():
    print("=== ХАНТЕР БЛОКБАСТЕР: ЧИСТЫЙ ТЕРМИНАЛ ===")
    player = {"hp": 2500, "max_hp": 2500, "level": 25, "is_berserk": False, "berserk_timer": 0, "shield_used": False}
    boss = {"name": "Гигантский Дракон", "level": 60, "hp": 85000, "max_hp": 85000}
    
    while player["hp"] > 0 and boss["hp"] > 0:
        print(f"\n--- СТАТУС ---")
        print(f"Хантер [Lv.{player['level']}] | HP: {player['hp']}/{player['max_hp']}")
        print(f"{boss['name']} [Lv.{boss['level']}] | HP: {boss['hp']}/{boss['max_hp']}")
        
        if player["is_berserk"]:
            print(f"🔥 БЕРСЕРК АКТИВЕН! Осталось ходов: {player['berserk_timer']}")
            player["berserk_timer"] -= 1
            if player["berserk_timer"] <= 0:
                player["is_berserk"] = False
                if random.randint(1, 100) <= 75:
                    print("💀 ОТДАЧА БЕРСЕРКА (75%)! Ты пал! Сброс до Lv. 1!")
                    player["level"] = 1
                    player["hp"] = 500
                    player["max_hp"] = 500
                    player["shield_used"] = False
                else:
                    print("🎉 25% ДЖЕКПОТ! Ты укротил берсерк! FULL HP!")
                    player["hp"] = player["max_hp"]

        print("\nДействия:")
        print("[1] ⚔️ Удар мечом")
        print("[2] 🛡️ Вспышка щита / Берсерк")
        print("[3] 🏃 Сбежать")
        
        action = input("Твой выбор: ")
        
        if action == "1":
            damage = random.randint(450, 550)
            boss["hp"] = max(0, boss["hp"] - damage)
            print(f"⚔️ Ты нанес боссу {damage} урона!")
        elif action == "2":
            if not player["is_berserk"]:
                player["hp"] -= 1000
                print("🛡️ Вспышка щита активирована! -1000 HP!")
                if player["hp"] <= 0 and not player["shield_used"]:
                    player["hp"] = 100
                    player["shield_used"] = True
                    player["is_berserk"] = True
                    player["berserk_timer"] = 5
                    print("⚡ Сработал экстренный протокол! Вход в БЕРСЕРК на 5 ходов!")
            else:
                print("⚠️ Берсерк уже активен!")
        elif action == "3":
            print("🏃 Ты сбежал с поля боя, но путь самурая продолжается...")
            break
        else:
            print("❌ Ошибка управления!")
            continue
            
        if boss["hp"] <= 0:
            print(f"\n🎉 ПОБЕДА! {boss['name']} повержен!")
            break
            
        boss_damage = random.randint(200, 400)
        player["hp"] -= boss_damage
        print(f"🔥 {boss['name']} атакует в ответ и наносит {boss_damage} урона!")
        
        if player["hp"] <= 0 and not player["is_berserk"]:
            print("\n💀 ПОРАЖЕНИЕ! Твои HP на нуле...")
            break
            
        time.sleep(0.5)

if __name__ == "__main__":
    start_game()
  
