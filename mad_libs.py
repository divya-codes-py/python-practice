import random

def story_1(name, place, animal, food, adjective, verb):
    return f"""
📖 Story 1: The Amazing Adventure!
=====================================
Ondu dina {name} {place} ge hoda.
Adara hatthira ondu {adjective} {animal} itthu.
{animal} bahala {food} ishta paḍuttittu.
{name} mattu {animal} eradhu seri {verb} maadidaru.
Adhu bahala channagirtu! 🎉
"""

def story_2(name, job, city, number, adjective, verb):
    return f"""
📖 Story 2: The Funny Day!
=====================================
{name} ondu {adjective} {job} aagittu.
Avaru {city} alli {number} varshadinda idaru.
Pratidinavu avaru {verb} maaduttidaru.
Janaru avara bagge bahala {adjective} aagidru!
Adhu bahala funny story! 😄
"""

def story_3(name, superhero, villain, place, weapon, adjective):
    return f"""
📖 Story 3: The Super Battle!
=====================================
{name} ondu dina {place} alli {superhero} nodi.
{superhero} {adjective} {villain} jote haadaaduttittu.
{name} avarigu ondu {weapon} koḍtu sahaaya maaditu.
{villain} odi hoitu, {superhero} gellitu!
{name} hero aaithu! 🦸
"""

def play_mad_libs():
    stories = [
        {
            "id": 1,
            "inputs": [
                ("Hesaru (noun)", "name"),
                ("Ondu jagha (place)", "place"),
                ("Ondu praani (animal)", "animal"),
                ("Ondu thinisuvudu (food)", "food"),
                ("Ondu visheshana (adjective)", "adjective"),
                ("Ondu kriye (verb)", "verb")
            ]
        },
        {
            "id": 2,
            "inputs": [
                ("Hesaru (noun)", "name"),
                ("Ondu kelsa (job)", "job"),
                ("Ondu nagara (city)", "city"),
                ("Ondu sankhye (number)", "number"),
                ("Ondu visheshana (adjective)", "adjective"),
                ("Ondu kriye (verb)", "verb")
            ]
        },
        {
            "id": 3,
            "inputs": [
                ("Nimma hesaru", "name"),
                ("Ondu superhero hesaru", "superhero"),
                ("Ondu villain hesaru", "villain"),
                ("Ondu jagha (place)", "place"),
                ("Ondu astra (weapon)", "weapon"),
                ("Ondu visheshana (adjective)", "adjective")
            ]
        }
    ]

    story = random.choice(stories)
    answers = {}

    print(f"\n📝 Story {story['id']} - Words kodi!")
    print("=" * 35)

    for prompt, key in story["inputs"]:
        answers[key] = input(f"{prompt}: ")

    print("\n⏳ Story ready maaduttide...")
    print("=" * 35)

    if story["id"] == 1:
        print(story_1(
            answers["name"], answers["place"], answers["animal"],
            answers["food"], answers["adjective"], answers["verb"]
        ))
    elif story["id"] == 2:
        print(story_2(
            answers["name"], answers["job"], answers["city"],
            answers["number"], answers["adjective"], answers["verb"]
        ))
    elif story["id"] == 3:
        print(story_3(
            answers["name"], answers["superhero"], answers["villain"],
            answers["place"], answers["weapon"], answers["adjective"]
        ))

def main():
    print("📖 Mad Libs Game!")
    print("=" * 35)
    print("Words kodi — funny story create aaguttade! 😄")

    while True:
        play_mad_libs()

        again = input("\nMatte play maadali? (yes/no): ").lower()
        if again != "yes":
            print("👋 Bye! Keep reading! 📖")
            break

main()
