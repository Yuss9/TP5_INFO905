from environment import Game
import numpy as np


class QLearningAgent:
    def __init__(self, num_states, num_actions, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.num_states = num_states
        self.num_actions = num_actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_values = np.zeros((num_states, num_actions))

    def choose_action(self, state):
        # Politique epsilon-greedy
        if np.random.rand() < self.epsilon:
            # Exploration : choisissez une action au hasard
            return np.random.choice(self.num_actions)
        else:
            # Exploitation : choisissez l'action avec la plus grande valeur Q
            return np.argmax(self.q_values[state, :])

    def update_q_values(self, state, action, reward, next_state):
        # Mettre à jour la table Q-valeurs en utilisant la formule de Q-learning
        best_next_action = np.argmax(self.q_values[next_state, :])
        self.q_values[state, action] += self.alpha * \
            (reward + self.gamma *
             self.q_values[next_state, best_next_action] - self.q_values[state, action])


# Fonction d'entraînement
def train_q_learning(agent, env, num_episodes):
    for episode in range(num_episodes):
        state = env.reset()
        total_reward = 0

        while True:
            action = agent.choose_action(state)
            next_state, reward, done, _ = env.move(action)
            agent.update_q_values(state, action, reward, next_state)
            total_reward += reward

            if done:
                break

            state = next_state

        if episode % 100 == 0:
            print(f"Episode {episode}, Total Reward: {total_reward}")


# Créer un environnement
env = Game(4, 4, wrong_action_p=0.1)

# Créer un agent Q-learning
num_states = env.n * env.m
num_actions = len(env.ACTIONS)
q_learning_agent = QLearningAgent(num_states, num_actions)

# Entraîner l'agent
train_q_learning(q_learning_agent, env, num_episodes=1000)

# Tester l'agent entraîné
state = env.reset()
env.print()

while True:
    action = q_learning_agent.choose_action(state)
    next_state, _, done, _ = env.move(action)
    env.print()

    if done:
        break

    state = next_state
