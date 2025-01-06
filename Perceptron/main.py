import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split  # to split the data easily
from sklearn.preprocessing import StandardScaler  # to normalize the data
import matplotlib.pyplot as plt  # for plotting
import seaborn as sns  # for plotting
from ucimlrepo import fetch_ucirepo

# Fetch dataset
banknote_authentication = fetch_ucirepo(id=267)

# Data (as pandas dataframes)
X = banknote_authentication.data.features
y = banknote_authentication.data.targets

print(f"Number of inputs: {X.shape[0]}")
print(f"Number of features: {X.shape[1]}")
print("\nTargets classes and the number of those classes")
print(y.value_counts())

# Summary statistics
print("\nSummary Statistics:")
print(X.describe())

# Convert dataframes to numpy arrays
X_np = X.to_numpy()
y_np = y.to_numpy()

# Split the data into two sets. One for training and one for testing.
X_train, X_test, y_train, y_test = train_test_split(X_np, y_np, test_size=0.2, random_state=42)

print("Shape of X_train:", X_train.shape)
print("Shape of X_test:", X_test.shape)
print("Shape of Y_train:", y_train.shape)
print("Shape of Y_test:", y_test.shape)

# Z-score normalization (standardization)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)  # Normalize the train data

# Test data also transformed with the parameters that were calculated from the training set
X_test = scaler.transform(X_test)


# activation function which will classify the given input x to a class which is either 1 or 0
def activation(w, x, b):  # weights, x vector, and the bias
    if (np.sum(w * x) + b) >= 0:
        return 1
    else:
        return 0


# parameters wights_array and bias are initial weights and bias
# the first 3 should be of type numpy arrays. bias and lr can be integer or flaoting points
def perceptron(train_array, label_array, weights_array, bias, learning_rate):
    for i in range(len(train_array)):  # for every vector x in the train array
        x = train_array[i]  # ith input

        target = label_array[i][0]  # the label of the x, that is, the target value in the ML literature

        # Because I didn't classify the labels to be in conventional {1, -1} set and used the given labels {1, 0}
        # I have to create a variable to use in the updating part below
        targ_mul = 1
        if target == 0:
            targ_mul = -1

        classified = activation(weights_array, x, bias)  # which class we said it belongs to
        if target != classified:  # we identified a misclassified example
            for j in range(len(weights_array)):
                weights_array[j] = weights_array[j] + (learning_rate * targ_mul * x[j])  # weights are updated
            bias = bias + (learning_rate * targ_mul)  # bias is updated

    return weights_array, bias


def evaluate(eval_X, eval_y, weights, bias):
    hit, tp, tn, fp, fn = 0, 0, 0, 0, 0
    for k in range(len(eval_X)):
        x = eval_X[k]
        classified2 = activation(weights, x, bias)
        label = eval_y[k][0]

        if classified2 == label:  # Hit!
            hit = hit + 1
            if classified2 == 0:  # label also 0
                tn = tn + 1
            else:  # label also 1
                tp = tp + 1

        else:  # They are not equal
            if classified2 == 0:  # label = 1
                fn = fn + 1
            else:
                fp = fp + 1

    accuracy = hit / len(eval_X)
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = (2 * precision * recall) / (precision + recall)
    print(f"Accuracy: {accuracy:.3f}")
    print(f"Precision: {precision:.3f}")
    print(f"Recall: {recall:.3f}")
    print(f"F1: {f1:.3f}")


initial_weights = np.array([0.1, 0.1, 0.1, 0.1])
initial_bias = 0.1
lr = 0.2
w, b = perceptron(X_train, y_train, initial_weights, initial_bias, lr)
print("Calculated weights = ", w)
print("Calculated bias = ", b)
print("Predicting on the training data:")
evaluate(X_train, y_train, w, b)
print()
print("Predicting on the test data:")
evaluate(X_test, y_test, w, b)

X_train_df = pd.DataFrame(X_train, columns=['variance', 'skewness', 'curtosis', 'entropy'])  # pandas data frame
correlation_matrix = X_train_df.corr()  # correlation matrix variance and entropi chosen
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0)
plt.title('Correlation Matrix Heatmap')
plt.show()

init_reduced_w = np.array([-1.21, 0.04])
init_reduced_b = -0.7

X_train_reduced_VE = X_train[:, [0, 3]]  # another way --_ X_train_reduced = df[['variance', 'entropy']].values # numpy array (1097)
reduced_w, reduced_b = perceptron(X_train_reduced_VE, y_train, init_reduced_w, init_reduced_b, learning_rate=0.2)
evaluate(X_train_reduced_VE, y_train, reduced_w, reduced_b)

def plot_decision_boundary(x_name, y_name, X, y, w, b, edgecolor):

    X_df = pd.DataFrame(X, columns=[x_name, y_name])
    y_df = pd.DataFrame(y, columns=['class'])
    y_df = y_df.reset_index(drop=True)
    frames = [X_df, y_df]
    data = pd.concat(frames, axis=1)

    sns.scatterplot(x=x_name, y=y_name, hue="class", data=data, edgecolor=edgecolor)

    min1, max1 = X[:, 0].min() - 1, X[:, 0].max() + 1
    min2, max2 = X[:, 1].min() - 1, X[:, 1].max() + 1

    x1grid = np.arange(min1, max1, 0.01)
    x2grid = np.arange(min2, max2, 0.01)

    xx, yy = np.meshgrid(x1grid, x2grid)

    r1, r2 = xx.flatten(), yy.flatten()
    grid = np.hstack((r1.reshape(-1, 1), r2.reshape(-1, 1)))

    yhat = []
    for x in grid:
        yhat.append(activation(w, x, b))
    yhat = np.array(yhat)

    zz = yhat.reshape(xx.shape)
    plt.contourf(xx, yy, zz, cmap='Paired', alpha=0.5)

    plt.show()


plot_decision_boundary("variance", "entropy", X_train_reduced_VE, y_train, reduced_w, reduced_b, "k")

X_train_reduced_VS = X_train[:, [0, 1]]  # another way --_ X_train_reduced = df[['variance', 'entropy']].values # numpy array (1097)
plot_decision_boundary("variance", "skewness", X_train_reduced_VS, y_train, reduced_w, reduced_b, "k")
evaluate(X_train_reduced_VS, y_train, reduced_w, reduced_b)

#One more for skewness curtosis
X_train_reduced_SC = X_train[:, [1, 2]]
plot_decision_boundary("skewness", "curtosis", X_train_reduced_SC, y_train, reduced_w, reduced_b, "k")
evaluate(X_train_reduced_SC, y_train, reduced_w, reduced_b)
