#!/usr/bin/env python3

import random
import time


def play_la_escape():
    print("=== ESCAPE FROM LOS ANGELES ===")
    name = input("Enter your character's name: ").strip()
    if not name:
        name = "Runner"

    obstacles = [
        "ICE agents",
        "gang members",
        "muggers",
        "a sudden auto accident",
        "a corrupt cop gang",
    ]

    total_blocks = 10
    current_block = 1
    encounter_chance = 0.65  # 65% chance an obstacle hits on any given block
    capture_odds = 0.50      # 50% chance of capture vs. evading capture

    print(f"\nAlright {name}, you need to make it {total_blocks} blocks down the street to reach the safe house.")
    print(f"Hazard rate per block: {int(encounter_chance * 100)}% | Capture odds when hit: {int(capture_odds * 100)}%\n")

    while current_block <= total_blocks:
        action = input(f"[Block {current_block}/{total_blocks}] Press Enter to run forward (or type 'q' to quit): ").strip().lower()
        if action == "q":
            print(f"\n{name} ducked into an alley and abandoned the run at Block {current_block}.")
            return

        print(f"{name} sprints down Block {current_block}...")
        time.sleep(0.5)

        # Step 1: Calculate odds of a problem hitting the character
        hazard_roll = random.random()
        print(f"  [Hazard Roll: {hazard_roll:.2f} vs. {encounter_chance:.2f} threshold]")

        if hazard_roll < encounter_chance:
            threat = random.choice(obstacles)
            print(f"  ! OBSTACLE: You run straight into {threat}!")
            time.sleep(0.5)

            # Step 2: 50% odds of capture vs. evading capture
            evasion_roll = random.random()
            print(f"  [Capture Roll: {evasion_roll:.2f} — need >= {capture_odds:.2f} to evade]")

            if evasion_roll < capture_odds:
                print(f"\nCAPTURED! {threat.capitalize()} cornered {name} on Block {current_block}. Game over.")
                return
            else:
                print(f"  -> CLOSE CALL! {name} dodged {threat} and kept running!\n")
        else:
            print(f"  -> Clear street! {name} made it past Block {current_block} untouched.\n")

        current_block += 1

    print(f"VICTORY! {name} survived all {total_blocks} blocks of Los Angeles and escaped capture!")


if __name__ == "__main__":
    play_la_escape()
