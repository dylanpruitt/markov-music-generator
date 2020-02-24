# markov-music-generator
An attempt to create a music generator using Markov chains.

Chord Progression Generator
---
The chord progression generator uses [Markov chains](http://setosa.io/ev/markov-chains/) to create a chord progression.
Each chord is represented by a state, and each state has a matrix of probability values that determine what state the chord will change to when it is updated.

For example, the I chord has a matrix `[0, 0.05, 0.05, 0.05, 0.10, 0.05, 0.15, 0.2, 0.05, 0.10, 0.10, 0.10]` of probability values (the total sum is 1). Every time the progression switches chords, it randomly selects a new chord to move to based on the probability values of the matrix.
