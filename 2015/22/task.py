from __future__ import annotations
from dataclasses import dataclass, field
from functools import total_ordering
import heapq

def task1(input_lines: list[str]):
    boss_health = int(input_lines[0].split(": ")[1])
    boss_at = int(input_lines[1].split(": ")[1])
    heap: list[GameState] = []
    checked_elements = set()

    print(f"Boss stats: {boss_health} health, {boss_at} ATK")

    heapq.heappush(heap, GameState(50, 500, boss_health, boss_at))

    while (len(heap) > 0):
        new_elem = heapq.heappop(heap)
        if new_elem.player_health <= 0:
            continue
        if new_elem.boss_health <= 0:
            print(new_elem.actions)
            print(new_elem.spent_mana)
            return
        if new_elem.player_mana < 53:
            continue
        if hash(new_elem) in checked_elements:
            continue

        checked_elements.add(hash(new_elem))
        for new_state in new_elem.get_follow_states():
            heapq.heappush(heap, new_state)
        
    print("No solution? :(")

def task2(input_lines: list[str]):
    boss_health = int(input_lines[0].split(": ")[1])
    boss_at = int(input_lines[1].split(": ")[1])
    heap: list[GameState] = []
    checked_elements = set()

    print(f"Boss stats: {boss_health} health, {boss_at} ATK")

    heapq.heappush(heap, GameState(50, 500, boss_health, boss_at, hardmode=True))

    while (len(heap) > 0):
        new_elem = heapq.heappop(heap)
        if new_elem.player_health <= 0:
            continue
        if new_elem.boss_health <= 0:
            print(new_elem.actions)
            print(new_elem.spent_mana)
            return
        if new_elem.player_mana < 53:
            continue
        if hash(new_elem) in checked_elements:
            continue

        checked_elements.add(hash(new_elem))
        for new_state in new_elem.get_follow_states():
            heapq.heappush(heap, new_state)
        
    print("No solution? :(")

@dataclass(init=True, unsafe_hash=True)
@total_ordering
class GameState:
    player_health: int
    player_mana: int
    boss_health: int
    boss_at: int
    remaining_shield_turns: int = 0
    remaining_poison_turns: int = 0
    remaining_recharge_turns: int = 0
    spent_mana: int = 0
    actions: list[str] = field(default_factory=list, compare=False, hash=False)
    df: int = 0
    hardmode: bool = False

    def calculate_turn(self):
        # Start of boss turn
        self.do_start_of_turn_effects()
        if self.boss_health > 0:
            # Boss attack
            self.do_boss_attack()
            # Start of player turn
            self.do_start_of_turn_effects()
            if self.hardmode:
                self.player_health -= 1

    def do_start_of_turn_effects(self):
        self.df = 0
        if self.remaining_poison_turns > 0:
            self.boss_health -= 3
            self.remaining_poison_turns -= 1
        if self.remaining_recharge_turns > 0:
            self.player_mana += 101
            self.remaining_recharge_turns -= 1
        if self.remaining_shield_turns > 0:
            self.df = 7
            self.remaining_shield_turns -= 1
    
    def do_boss_attack(self):
        self.player_health -= max(1, self.boss_at - self.df)

    def get_follow_states(self) -> list[GameState]:
        following_states = []

        # Magic Missile
        if self.player_mana >= 53:
            mm_state = GameState(
                self.player_health,
                self.player_mana - 53,
                self.boss_health - 4,
                self.boss_at,
                self.remaining_shield_turns,
                self.remaining_poison_turns,
                self.remaining_recharge_turns,
                self.spent_mana + 53,
                self.actions + ["mm"],
                self.df,
                self.hardmode
            )
            mm_state.calculate_turn()
            following_states.append(mm_state)
        
        # Drain
        if self.player_mana >= 73:
            d_state = GameState(
                self.player_health + 2,
                self.player_mana - 73,
                self.boss_health - 2,
                self.boss_at,
                self.remaining_shield_turns,
                self.remaining_poison_turns,
                self.remaining_recharge_turns,
                self.spent_mana + 73,
                self.actions + ["d"],
                self.df,
                self.hardmode
            )
            d_state.calculate_turn()
            following_states.append(d_state)
        
        # Shield
        if self.player_mana >= 113 and self.remaining_shield_turns <= 0:
            s_state = GameState(
                self.player_health,
                self.player_mana - 113,
                self.boss_health,
                self.boss_at,
                self.remaining_shield_turns + 6,
                self.remaining_poison_turns,
                self.remaining_recharge_turns,
                self.spent_mana + 113,
                self.actions + ["s"],
                self.df,
                self.hardmode
            )
            s_state.calculate_turn()
            following_states.append(s_state)
        
        # Poison
        if self.player_mana >= 173 and self.remaining_poison_turns <= 0:
            p_state = GameState(
                self.player_health,
                self.player_mana - 173,
                self.boss_health,
                self.boss_at,
                self.remaining_shield_turns,
                6,
                self.remaining_recharge_turns,
                self.spent_mana + 173,
                self.actions + ["p"],
                self.df,
                self.hardmode
            )
            p_state.calculate_turn()
            following_states.append(p_state)

        # Recharge
        if self.player_mana >= 229 and self.remaining_recharge_turns <= 0:
            r_state = GameState(
                self.player_health,
                self.player_mana - 229,
                self.boss_health,
                self.boss_at,
                self.remaining_shield_turns,
                self.remaining_poison_turns,
                5,
                self.spent_mana + 229,
                self.actions + ["r"],
                self.df,
                self.hardmode
            )
            r_state.calculate_turn()
            following_states.append(r_state)
        
        return following_states
    
    def __lt__(self, other: GameState):
        return (
            (self.spent_mana, self.boss_health, self.player_health, self.player_mana, self.remaining_recharge_turns, self.remaining_poison_turns, self.remaining_shield_turns)
            <
            (other.spent_mana, other.boss_health, other.player_health, other.player_mana, other.remaining_recharge_turns, other.remaining_poison_turns, other.remaining_shield_turns)
        )