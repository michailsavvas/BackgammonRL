This is my final project for the class "CS221: Artificial Intelligence: Principles and Techniques", taken at Stanford University in Fall 2015.

The project is titled "An AI Agent for Backgammon". The goal is to develop a smart AI agent to play backgammon. We follow
Gerald Tesauro’s approach and use reinforcement learning with a sigmoid linear evaluation function and a neural network evaluation function.

Keywords: backgammon, TD-learning, reinforcement learning, limited tree search, adversarial game, neural networks

The final report for the project is located in the file "final.pdf".

Besides the final report, the following files are included:

- game.py : contains the mechanics of the game of the backgammon

- learn.py : contains all evaluation functions and gradients and the TD-Learning algorithm

- minimax.py : contains the minimax recursion (value and action)

- util.py : helper functions for manipulating Counters

- GUI.py : toy function that prints the configuration of the board (prints at most 7 pieces per point and does not keep track of bar and out)

- train_weights.py : called in order to train and save the weights to a text file
    - eval_mode : 1 for sigmoid linear, 2 for neural net
    - step_mode : 0 for constant \eta = 0.1, 1 for \eta = 1 / #simulations, 2 for \eta = 1 /
    [#simulations / update]
    - update : used in changing \eta
    - norm_step : normalize weights every norm_step iteration for eval_mode == 1, print weights to file
    - reward : reward for terminal state
    - initial : 0 for initial weights 0, 1 for uniformly random in [-1, 1], 2 for initializing from file
    - iterations, filename, output : clear
    
- trained_vs_random.py : runs simulations of games of the minimax agent with given weights vs. the random agent
    - input parameters : same as train_weights or clear
    
- play_minimax.py : runs games of user against minimax agent with given weights
    - input parameters : similar to above
    
- minimax_actions.py : prints minimax actions for red or black for the start state and a few test rolls
    - input parameters : similar to above or clear
    
- FINAL_SIGMOID_SET_I.txt : Set I of weights for sigmoid linear

- FINAL_SIGMOID_SET_II.txt : Set II of weights for sigmoid linear
    
- FINAL_ITER9152_NEURAL_STEP2_UPDATE2000_REWARD3_INIT0.txt : Set I of weights for neural net

- FINAL_ITER5109_NEURAL_STEP2_UPDATE2000_REWARD3_INITRAND.txt : Set I.5 of weights for neural net

- FINAL_ITER7002_NEURAL_STEP2_UPDATE2000_REWARD3_INITRAND.txt : Set II of weights for neural net

- init_labels_neural.txt : Contains the names of all the 10001 weights for the neural net

In addition, the following folders are included:

- Performance : Contains various text files with percentages of wins of minimax vs. random obtained by running trained_vs_random.py

- Test Weights and Performance, Test Scripts: Contain various python and weight files that were used to test and debug the above at different stages of the project. The names and conventions are not necessarily consistent with the above.
