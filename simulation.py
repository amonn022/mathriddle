import numpy as np

def one_game_simulation():
    coinflips = np.random.choice(['H','T'],100)
    aliceIndex = np.arange(0,100).tolist()
    bobIndex = np.concatenate(
    (np.arange(0,100,2),
    np.arange(1,100,2))
    ).tolist()

    alice_pos = 0
    bob_pos = 0

    while True:
        if alice_pos < 99:
            alice_coin1 = coinflips[aliceIndex[alice_pos]]
            alice_coin2 = coinflips[aliceIndex[alice_pos+1]]
            # Compare to see if they are the same
            if(alice_coin1==alice_coin2):
                return "Alice"
            alice_pos+= 1

        if bob_pos < 99:
            bob_coin1 = coinflips[bobIndex[bob_pos]]
            bob_coin2 = coinflips[bobIndex[bob_pos+1]]
            # Compare to see if they are the same in bob's case 
            if(bob_coin1==bob_coin2):
                return "Bob"
            bob_pos+= 1


def full_simulation(num_games):
    alice_wins = 0
    bob_wins = 0

    for _ in range(num_games):
        winner = one_game_simulation()
        if winner == "Alice":
            alice_wins+=1
        else:
            bob_wins+=1
    return alice_wins, bob_wins



alice_win_count, bob_win_count =  full_simulation(1000)

print(f"Alice won {alice_win_count} times")
print(f"Bob won {bob_win_count} times")