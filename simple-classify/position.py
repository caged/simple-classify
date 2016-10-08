import numpy as np
import tflearn
from tflearn.data_utils import load_csv
import csv

# Classify a player by position Guard, Foward, or Center based on their basic
# statistical profile


# Guard, Forward, Center
positions = ['G', 'F', 'C']

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

with open('data/players.csv', newline='') as f:
    next(f) # Skip header row
    test_data = csv.reader(f)

    with open('data/results.csv', 'w', newline='') as r:
        outfile = csv.writer(r)
        outfile.writerow(['season', 'name', 'position'] + positions)
        for row in test_data:
            meta = row[:3]
            stats = row[3:]
            meta[2] = positions[int(meta[2])]
            pred = model.predict([stats])[0]
            outfile.writerow(meta + pred)
