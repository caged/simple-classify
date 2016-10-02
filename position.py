import numpy as np
import tflearn
from tflearn.data_utils import load_csv

# Classify a player by position Guard, Foward, or Center based on their basic
# statistical profile


# Guard, Forward, Center
positions = ('G', 'F', 'C')

data, labels = load_csv('data/players-training.csv', target_column=2,
                        columns_to_ignore=[0,1],
                        categorical_labels=True, n_classes=3)

num_features = len(data[0])

# Build neural network from num_features features/columns
net = tflearn.input_data(shape=[None, num_features])
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 3, activation='softmax')
net = tflearn.regression(net)

# Define model
model = tflearn.DNN(net)

# Start training (apply gradient descent algorithm)
model.fit(data, labels, n_epoch=10, batch_size=10, show_metric=True)

# # 2010-11 per36 season data
# howard = [2,1.3,13.5,2.3,1.3]
# bryant = [1,5,5.4,0.2,1.3]
# westbrook = [0,8.5,4.8,0.4,2]
# players = [howard, bryant, westbrook]
#
# # Predict player positions (G, F, C)
# pred = model.predict(players)
# print("Bryan position prediction:", pred[0])
# print("Howard position prediction:", pred[1])
# print("Westbrook position prediction:", pred[2])
