# symmetric-coalitions-algo

This small repository implements the solutions algorithm for a symmetric coalition formation game as presented
in the book by Debraj Ray[^1], Chapter 5.2 page 55.

Simply run:

```
python main.py
```
to execute the algorithm with an example from the book.

## Algorithm details

### Terminology

* **symmetric partition functions:** The worth of a coalition in any given partition only depends on the number of players in each coalition. In other words, it does not matter who you team up with, only the sizes of the coalitions that form.

* **farsightedness**: A great description of farsightedness was coined by Aumann & Myerson (1988):

    *When a player considers forming a link with another
    one, he does not simply ask himself whether he may
    expect to be better off with this link than without it,
    given the previously existing structure. Rather, he looks
    ahead and asks himself, ‘Suppose we form this new
    link, will other players be motivated to form further
    new links that were not worthwhile for them before?
    Where will it all lead? Is the end result good or bad for
    me?’*[^2]

* **irreversible agreements:** Once a coalition gets formed, it stays in place for the rest of the game. That is, no new members can join, and no existing member can leave a treaty.

## References

[^1]: Debraj Ray 2007: A Game-Theoretic Perspective on Coalition Formation. Oxford University Press. Openly available at:
https://debrajray.com///wp-content/uploads/2021/04/CoalitionBook.pdf

[^2]: Aumann, R., and Myerson, R. (1988): Endogenous Formation of Links Between Players and Coalitions: An Application of the Shapley Value. Cambridge University Press.