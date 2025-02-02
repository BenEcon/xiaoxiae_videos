from collections import deque

def get_tree(depth):
    def can_be_best(remaining, ores, robots, max_geodes):
        """Return True if the state can beat max_geodes score."""
        # shit estimation: assume we can build a geode robot every turn
        return ((remaining * (remaining - 1)) // 2 + robots[-1] * remaining + ores[-1]) > max_geodes

    def can_build_robot(ores, cost):
        for o, c in zip(ores, cost):
            if o < c:
                return False
        return True

    def want_to_build_robot(robots, robot, blueprint):
        robot_count = robots[robot]

        # always build geode
        if robot == 3:
            return True

        if robot_count == 0:
            return True

        for costs in blueprint:
            if costs[robot] > robot_count:
                return True

        return False

    def next_states(remaining, ores, robots, blueprint):
        """Return the next state, given the current ores and robots."""
        states = [(list(ores), list(robots))]

        # attempt to build more robots
        # we're assuming that we can built at most one each turn
        for i, cost in enumerate(blueprint):
            # if we have enough robots to generate the required resources forever, don't build it
            if not want_to_build_robot(robots, i, blueprint):
                continue

            if not can_build_robot(ores, cost):
                continue

            states.append(
                (
                    [o - c - (0 if i != j else 1)
                     for j, (o, c) in enumerate(zip(ores, cost))],
                    [r + (0 if i != j else 1)
                     for j, r in enumerate(robots)],
                )
            )

        for (ores, robots) in states:
            for i in range(len(ores)):
                ores[i] += robots[i]

            yield remaining - 1, tuple(ores), tuple(robots)


    blueprint = """Blueprint 1: Each ore robot costs 4 ore.  Each clay robot costs 2 ore.  Each obsidian robot costs 3 ore and 14 clay.  Each geode robot costs 2 ore and 7 obsidian."""
    parts = blueprint.strip().split()

    # robot costs
    blueprint = (
        (
            (int(parts[6]), 0, 0, 0), # ore
            (int(parts[12]), 0, 0, 0), # clay
            (int(parts[18]), int(parts[21]), 0, 0),  # obsidian
            (int(parts[27]), 0, int(parts[30]), 0),  # geode
        )
    )

    #                   Ores        Robots
    #               Or Cl Ob Ge   Or Cl Ob Ge
    queue = deque([(depth, (0, 0, 0, 0), (1, 0, 0, 0))])
    visited = {queue[0]: None}
    max_geodes = 0

    while len(queue) != 0:
        current = queue.popleft()
        max_geodes = max(max_geodes, current[1][-1])

        if current[0] == 0:
            continue

        if not can_be_best(*current, max_geodes):
            continue

        for next_state in next_states(*current, blueprint):
            if next_state not in visited:
                queue.append(next_state)
                visited[next_state] = current

    for k, v in visited.items():
        if v == None:
            visited[k] = visited[k]
            break

    print(depth, len(visited), max_geodes)

for i in range(100):
    get_tree(i)
