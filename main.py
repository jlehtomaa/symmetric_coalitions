"""
Example use case of the algorithm for obtaining the equilibrium coalition
structure of a symmetric farsighted coalition formation game. For details, see
Chapter 5 and the example 5.2. on p.62 in the following book:

Debraj Ray 2007: A Game-Theoretic Perspective on Coalition Formation.
Oxford University Press. Openly available at:
https://debrajray.com///wp-content/uploads/2021/04/CoalitionBook.pdf
"""

from symmetric_coalitions.game import SymmetricGame

if __name__ == "__main__":

    coalition_worths = {
        (3, (3,1)): 22,
        (1, (3,1)): 0,
        (2, (2,1,1)): 16,
        (1, (2,1,1)): 1
    }

    game = SymmetricGame(num_players=4, coalition_worths=coalition_worths)
    sol = game.solve()

    print("Final coalition structure is: ", sol)
