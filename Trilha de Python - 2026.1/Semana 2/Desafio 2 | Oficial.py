# Simulador de Batalha de Cartas (TCG)

def atacar(nome_atacante, ataque, nome_defensor, hp_defensor):
    novo_hp = hp_defensor - ataque

    if novo_hp < 0:
        novo_hp = 0

    print(f"{nome_atacante} atacou {nome_defensor} causando {ataque} de dano!")
    return novo_hp


def exibir_placar(nome1, hp1, nome2, hp2):
    print("\n========== PLACAR ==========")
    print(f"{nome1}: {hp1} HP")
    print(f"{nome2}: {hp2} HP")
    print("============================\n")


nome1 = input("Nome do Monstro 1: ")
hp1 = int(input("HP do Monstro 1: "))
ataque1 = int(input("Ataque do Monstro 1: "))

nome2 = input("Nome do Monstro 2: ")
hp2 = int(input("HP do Monstro 2: "))
ataque2 = int(input("Ataque do Monstro 2: "))

if hp1 <= 0 or hp2 <= 0 or ataque1 <= 0 or ataque2 <= 0:
    print("Valor inválido! HP e ataque devem ser maiores que zero.")
else:
    turno = 1

    while hp1 > 0 and hp2 > 0:
        print(f"========== TURNO {turno} ==========")

        hp2 = atacar(nome1, ataque1, nome2, hp2)
        exibir_placar(nome1, hp1, nome2, hp2)

        if hp2 > 0:
            hp1 = atacar(nome2, ataque2, nome1, hp1)
            exibir_placar(nome1, hp1, nome2, hp2)

        turno += 1

    if hp1 > 0 and hp2 == 0:
        print(f"🏆 O grande vencedor foi {nome1}!")
    elif hp2 > 0 and hp1 == 0:
        print(f"🏆 O grande vencedor foi {nome2}!")
