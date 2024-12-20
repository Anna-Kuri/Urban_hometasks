import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(5):
        number = i + 1
        await asyncio.sleep(i * 5 / power)
        print(f'Силач {name} поднял шар номер {number}')

    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    participant_1 = asyncio.create_task(start_strongman('Félix', 100))
    participant_2 = asyncio.create_task(start_strongman('Max', 50))
    participant_3 = asyncio.create_task(start_strongman('Peter', 40))

    await participant_1
    await participant_2
    await participant_3

asyncio.run(start_tournament())
