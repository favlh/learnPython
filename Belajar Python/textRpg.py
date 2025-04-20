import random

# Setup awal
player_level = 1
player_exp = 0
exp_to_level_up = 50

player_max_hp = 100
player_hp = player_max_hp
player_attack = (10, 20)
player_healing = 30
player_potion = 5

print("⚔️ Selamat datang di dunia petualangan, ksatria pemberani! ⚔️")

while player_hp > 0:
    # Buat monster baru tiap loop
    monster_hp = 80 + (player_level * 10)
    monster_attack = (5 + player_level, 15 + player_level)
    print(f"\n👹 Seekor monster muncul! HP: {monster_hp}")

    # Loop pertarungan
    while monster_hp > 0:
        print(f"\n👤 LEVEL: {player_level} | EXP: {player_exp}/{exp_to_level_up}")
        print(f"❤️ HP Kamu: {player_hp}/{player_max_hp} | 👹 HP Monster: {monster_hp}")
        print(f"💊 Potion: {player_potion} sisa")
        print("Apa yang ingin kamu lakukan?")
        print("1. Serang")
        print("2. Kabur")
        if player_potion > 0:
            print("3. Gunakan Potion (30 HP)")
        else:
            print("❗ Potion kamu sudah habis!")

        choice = input(">>> Pilih opsi (1/2/3): ")

        if choice == "1":
            # Serangan player
            damage = random.randint(*player_attack)
            monster_hp -= damage
            print(f"\n💥 Kamu menyerang monster dan memberi {damage} damage!")

            if monster_hp <= 0:
                print("🎉 Kamu mengalahkan monster! Dapat 30 EXP!")
                player_exp += 30

                # level up
                if player_exp >= exp_to_level_up:
                    player_level += 1
                    player_exp -= exp_to_level_up
                    exp_to_level_up += 20
                    player_max_hp += 25
                    player_hp = player_max_hp
                    player_attack = (player_attack[0] + 3, player_attack[1] + 5)
                    player_healing += 5
                    player_potion += 2

                    print(f"\n🌟 LEVEL UP! Kamu sekarang level {player_level}!")
                    print(f"❤️ Max HP naik jadi {player_max_hp}, serangan makin kuat, dan efek potion meningkat!")
                    print(f"💊 Kamu dapat 1 potion baru, dan efek potion meningkat menjadi {player_healing} HP!")

                break

            # Serangan monster
            monster_damage = random.randint(*monster_attack)
            player_hp -= monster_damage
            print(f"😡 Monster membalas dan memberi {monster_damage} damage!")

            if player_hp <= 0:
                print("💀 Kamu tumbang... Dunia ini terlalu kejam untukmu.")
                break

        elif choice == "2":
            print("🏃‍♂️ Kamu kabur dari pertarungan. Monster tertawa puas. 😈")
            player_hp = 0
            break

        elif choice == "3" and player_potion > 0:
            player_hp += player_healing
            if player_hp > player_max_hp:
                player_hp = player_max_hp
            player_potion -= 1
            print(f"💊 Kamu menggunakan potion dan sembuh {player_healing} HP! Sisa potion: {player_potion}")

        else:
            print("❗ Pilihannya cuma 1, 2, atau 3!")

print("\n🌟 Terima kasih sudah bermain, ksatria sejati!")