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
Adhu bahala funny! 😄
"""

def play_mad_libs():
    stories = [
        {
            "id": 1,
            "inputs": [
                ("Hesaru", "name"), ("Jagha", "place"),
                ("Praani", "animal"), ("Thinisuvudu", "food"),
                ("Visheshana", "adjective"), ("Kriye", "verb")
            ]
        },
        {
            "id": 2,
            "inputs": [
                ("Hesaru", "name"), ("Kelsa", "job"),
                ("Nagara", "city"), ("Sankhye", "number"),
                ("Visheshana", "adjective"), ("Kriye", "verb")
            ]
        }
    ]

    story = random.choice(stories)
    answers = {}

    print(f"\n📝 Story {story['id']} - Words kodi!")
    print("=" * 35)

    for prompt, key in story["inputs"]:
        answers[key] = input(f"{prompt}: ")

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

def main():
    print("📖 Mad Libs Game!")
    print("=" * 35)

    while True:
        play_mad_libs()
        again = input("\nMatte play maadali? (yes/no): ").lower()
        if again != "yes":
            print("👋 Bye!")
            break

main()
