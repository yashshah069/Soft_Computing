import numpy as np

class SimpleBAM:
    def __init__(self, patterns_A, patterns_B):
        self.weights = np.dot(patterns_A.T, patterns_B)
    
    def recall_A(self, pattern_B):
        return np.dot(pattern_B, self.weights.T)
    
    def recall_B(self, pattern_A):
        return np.dot(pattern_A, self.weights)
    
# Example usage:
if __name__ == "__main__":
    patterns_A = np.array([[1, 1, -1], [-1, 1, 1], [-1, -1, -1]])
    patterns_B = np.array([[1, -1], [-1, 1], [1, 1]])
    
    bam = SimpleBAM(patterns_A, patterns_B)
    
    # Test recall for pattern B
    test_pattern_B = np.array([1, -1])
    recalled_pattern_A = bam.recall_A(test_pattern_B)
    print("Recalled Pattern A:", recalled_pattern_A)
    
    # Test recall for pattern A
    test_pattern_A = np.array([1, 1, -1])
    recalled_pattern_B = bam.recall_B(test_pattern_A)
    print("Recalled Pattern B:", recalled_pattern_B)


# Bidirectional Associative Memory (BAM) is a supervised learning model in Artificial
# Neural Network. This is hetero-associative memory, for an input pattern, it returns another
# pattern which is potentially of a different size. This phenomenon is very similar to the
# human brain. Human memory is necessarily associative. It uses a chain of mental
# associations to recover a lost memory like associations of faces with names, in exam
# questions with answers, etc. In such memory associations for one type of object with
# another, a Recurrent Neural Network (RNN) is needed to receive a pattern of one set of
# neurons as an input and generate a related, but different, output pattern of another set of
# neurons. Why BAM is required? The main objective to introduce such a network model is
# to store hetero-associative pattern pairs. This is used to retrieve a pattern given a noisy or
# incomplete pattern. BAM Architecture: When BAM accepts an input of n-dimensional
# vector X from set A then the model recalls m-dimensional vector Y from set B. Similarly
# when Y is treated as input, the BAM recalls X.
# Architecture:
# • BAM network consists of two layers: the input layer and the output layer.
# • The input layer receives input patterns, while the output layer stores and retrieves
# associated patterns.
# Training:
# • BAM network is typically trained using Hebbian learning or a similar associative
# learning rule.
# • During training, the network learns to associate input patterns with output patterns and
# vice versa.
# • The weight matrices WWW and TTT are adjusted based on the input-output pairs
# presented during training.
# Bidirectional Association:
# • BAM network allows bidirectional association between input and output patterns.
# • Given an input pattern, the network can retrieve the associated output pattern, and vice
# versa.
# Applications:
# • BAM networks have been used in various applications, including pattern recognition,
# associative memory, and content-addressable memory systems.
# • They are particularly useful for tasks where bidirectional association between patterns
# is required, such as autoassociative and heteroassociative memory tasks.