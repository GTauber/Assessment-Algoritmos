import asyncio
import random

async def generator(queue, XLimit):
    for _ in range(XLimit):
        number = random.randint(0, 100)
        await queue.put(number)
        await asyncio.sleep(0.01)
    await queue.put(None)

async def narrator(queue, players):
    while True:
        number = await queue.get()
        if number is None:
            for player in players:
                player['queue'].put_nowait(None)
            break
        print(f"Number is {number}")
        for player in players:
            await player['queue'].put(number)

async def player(name, card, queue):
    hits = set()
    while True:
        number = await queue.get()
        if number is None:
            break
        if number in card:
            hits.add(number)
        print(f"{name} {number} {card} {len(hits)}")
        if hits == set(card):
            print(f"{name} is the WINNER {hits} {card}")
            for p in asyncio.all_tasks():
                p.cancel()
            break

async def main():
    random.seed()
    XLimit = 1000
    players_list = [
        ("player-1", [5,10,48,55]),
        ("player-2", [8,46,80,99]),
        ("player-3", [17,29,78,95])
    ]
    queue = asyncio.Queue()
    players = []
    for name, card in players_list:
        player_queue = asyncio.Queue()
        players.append({'name': name, 'card': card, 'queue': player_queue})
        asyncio.create_task(player(name, card, player_queue))
    await asyncio.gather(
        generator(queue, XLimit),
        narrator(queue, players)
    )

    print("Game is over")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except asyncio.CancelledError:
        print("Game was cancelled")

