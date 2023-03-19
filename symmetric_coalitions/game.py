import math
from symmetric_coalitions.utils import sorted_integer_partition

class SymmetricGame:
    """
    A solution algorithm for a symmetric coalition formation game as presented
    in the following book in Chapter 5.2 page 55:

    Debraj Ray 2007: A Game-Theoretic Perspective on Coalition Formation.
    Oxford University Press. Openly available at:
    https://debrajray.com///wp-content/uploads/2021/04/CoalitionBook.pdf

    Args:
        num_players (int):
            Number of players in the game.
        coalition_worths (dict):
            Transferable coalition worths, as defined in Ray 2007 p.54 section
            5.1. Keys are tuples indicating the coalition structure and values
            are floats indicating the worths. For instance, the worths
            corresponding to the Example 5.1 on p. 57 can be represented as:
            coalition_worths = {
                (4, (4,1)): 6.,
                (1, (4,1)): 2.,
                (3, (3,2)): 3.,
                (2, (3,2)): 8.,
                (2, (2,1,1,1)): 0.1,
                (1, (2,1,1,1)): 3.,
                (3, (3,1,1)): 10.,
                (1, (3,1,1)): 0.
            }
        coalition_worths (float), default=0.:
            Coalition worth for any coalition structure not specified explicitly
            in `coalition_worths`.

    Example use of the class, replicating the Example 5.2 on p.62 in Ray 2007.

    coalition_worths = {
        (3, (3,1)): 22.,
        (1, (3,1)): 0.,
        (2, (2,1,1)): 16.,
        (1, (2,1,1)): 1.
    }

    game = SymmetricGame(num_players=4, coalition_worths=coalition_worths)
    sol = game.solve()

    print('Solution: ', sol)
    >>> Solution: (2,1,1)

    """

    def __init__(
        self,
        num_players: int,
        coalition_worths: dict,
        default_payoff: float=0.
    ):

        self.num_players = num_players
        self.coalition_worths = coalition_worths
        self.default_payoff = default_payoff


    def solve(self) -> tuple:
        """Run the solution algorithm and apply the result recursively to
        come up with the equilibrium numerical structure.

        Returns:
            (tuple):
                Numerical coalition structure.
        """

        self._construct_decision_rule()
        return self._unroll_steps()

    def _concatenate(self, subcoal: tuple) -> tuple:
        """Helper function to concatenate intermediate coalition structures.
        Corresponds to function `c` in Ray 2007 p.55, algorithm Step 2.

        Args:
            subcoal (tuple):
                An intermediate coalition structure to be completed.
        Returns:
            (tuple):
                A resulting coalition structure, based in the input `subcoal`
                and the decision rule constructed so far in `self.next_coalition`
                by the main algorithm.
        """
        coal = subcoal
        while sum(coal) < self.num_players:
            coal += self.next_coalition[tuple(sorted(coal, reverse=True))]

        return tuple(sorted(coal, reverse=True))

    def _construct_decision_rule(self) -> None:
        """Run steps 1-3 of the algorithm on p.55-56 to construct the decision
        rule `t` in the text."""

        # We apply the algorithm recursively on all substructures of players
        # that add up to any positive integer strictly less than the total
        # number of players to determine what is the size of the coalition that
        # forms next.

        # The subcalitions below corresponds to \mathbf{n} in the text (p.55).
        # For instance, if n=3, subcoalitions = {1: [(1,)], 2: [(2,), (1,1)]}.
        subcoalitions = {i: sorted_integer_partition(i)
                         for i in range(1, self.num_players)}

        # STEP 1:
        # Initialize the decision rule. For any substructure that has already
        # formed and where n-1 players have been assigned to (permanently binding)
        # coalitions, the next coalition must be of size one.
        self.next_coalition = {coalition: (1,) for coalition
                              in subcoalitions[self.num_players-1]}

        # STEP 2: For all possible substructures (=intermediate coalitions
        # already formed), look for the coalition size that forms next.
        for m in reversed(range(self.num_players)): # m \in {n-1, ..., 0}

            # The size of the next coalition that forms must be from the set
            # {1, ..., n-m}. For example:
            # If num_players=5 and m = 4, the next coalition is from {1}.
            # If num_players=5 and m = 3, the next coalition is from {1, 2}.

            if m > 0:
                existing_coals = subcoalitions[m]
            elif m == 0:
                existing_coals = [()]

            for coalition in existing_coals:
                max_worth = -math.inf
                argmax = None

                # STEP 3: Find the largest integer that maximizes the
                # average worth of the next coalition that forms from the
                # current substructure. Corresponds to the variable `t` in the
                # Ray 2007 book.
                for next_size in range(1, self.num_players-m+1):

                    subcoal = self._concatenate(coalition + (next_size,))

                    try:
                        worth = self.coalition_worths[(next_size, subcoal)] / next_size
                    except KeyError:
                        worth = self.default_payoff

                    if worth > max_worth:
                        max_worth = worth
                        argmax = next_size

                    elif worth == max_worth:
                        argmax = max(argmax, next_size)

                # Update the decision rule.
                self.next_coalition[coalition] = (argmax,)

    def _unroll_steps(self) -> tuple:
        """Run step 4 of the algorithm on p.56.
        Starting from an empty set, apply the decision rule recursively to
        form the equilibrium coalition structure."""

        coal = ()
        while sum(coal) < self.num_players:
            coal += self.next_coalition[coal]

        return tuple(sorted(coal, reverse=True))
