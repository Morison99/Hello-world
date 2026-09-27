
# def neuron(inputs, weights, bias):
#     z = sum(w * x for w, x in zip(weights, inputs)) + bias
#     return 1 if z >= 0 else 0


# # ورودی‌ها: [آفتابی، تعطیلی، حوصله]، آستانه ۳ ← بایاس = ۳-
# picnic_weights = [3, 2, 1]

# print("آفتابی=۱، تعطیل=۰، حوصله=۱ ←", neuron(
#     [1, 0, 1], picnic_weights, bias=-3))
# print("آفتابی=۰، تعطیل=۰، حوصله=۱ ←", neuron(
#     [0, 0, 1], picnic_weights, bias=-3))


from sklearn.datasets import make_circles
from sklearn.datasets import make_blobs
import numpy as np
import matplotlib.pyplot as plt

print("done")


# def and_neuron(x1, x2):
#     z = 1*x1 + 1*x2 - 1.5
#     return 1 if z > 0 else 0


# for x1, x2 in [(0, 0), (0, 1), (1, 0), (1, 1)]:
#     print(f"{x1} AND {x2}  →  {and_neuron(x1, x2)}")


# w1, w2, b = 1, 1, -0.5      # ✏️ مقداردهی کن


# def or_neuron(x1, x2):
#     return 1 if w1*x1 + w2*x2 + b > 0 else 0


# for x1, x2 in [(0, 0), (0, 1), (1, 0), (1, 1)]:
#     target = 1 if (x1 == 1 or x2 == 1) else 0
#     out = or_neuron(x1, x2)
#     print(f"{x1} OR {x2}  →  {out}   {'✅' if out == target else '❌'}")

# points = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# labels = np.array([0, 1, 1, 0])

# plt.figure(figsize=(5, 5))
# for (x1, x2), lab in zip(points, labels):
#     color = "mediumseagreen" if lab == 1 else "gray"
#     plt.scatter(x1, x2, s=500, color=color, edgecolor="black", zorder=3)
#     plt.text(x1, x2 - 0.18, f"{x1} XOR {x2} = {lab}", ha="center", fontsize=11)
# plt.xlim(-0.5, 1.5)
# plt.ylim(-0.7, 1.5)
# plt.title("XOR is not linearly separable")
# plt.grid(alpha=0.3)
# plt.show()


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


# z = np.linspace(-8, 8, 200)

# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.8))
# ax1.plot(z, (z > 0).astype(float), color="crimson", linewidth=2)
# ax1.set_title("Hard threshold")
# ax1.set_xlabel("z")
# ax1.grid(alpha=0.3)
# ax2.plot(z, sigmoid(z), color="steelblue", linewidth=2)
# ax2.set_title("Sigmoid")
# ax2.set_xlabel("z")
# ax2.grid(alpha=0.3)
# plt.show()


# for value in [0, 5, -5, 100]:
#     print(f"sigmoid({value}) =", sigmoid(value))


# X, y = make_blobs(n_samples=200, centers=[[3, 3], [7, 7]],
#                   cluster_std=1.3, random_state=42)

# plt.figure(figsize=(6, 5))
# plt.scatter(X[y == 0, 0], X[y == 0, 1],
#             color="steelblue", alpha=0.7, label="class 0")
# plt.scatter(X[y == 1, 0], X[y == 1, 1],
#             color="coral", alpha=0.7, label="class 1")
# plt.xlabel("x1")
# plt.ylabel("x2")
# plt.title("Training data")
# plt.legend()
# plt.show()

# w = np.array([-1.0, 1.0])       # وزن اولیه عمدا نامناسب
# b = 0.0
# learning_rate = 0.5

# losses = []
# snapshots = {0: (w.copy(), b)}

# for epoch in range(1, 201):
#     a = sigmoid(X @ w + b)                       # گذر رو به جلو، همه نمونه‌ها
#     error = a - y                                # dL/dz برای هر نمونه
#     w = w - learning_rate * (X.T @ error) / len(X)   # dL/dw میانگین‌گیری‌شده
#     b = b - learning_rate * error.mean()             # dL/db
#     # میانگین |خطا| برای منحنی هزینه
#     losses.append(np.abs(error).mean())
#     if epoch in (5, 30, 200):
#         snapshots[epoch] = (w.copy(), b)

# accuracy = ((a > 0.5).astype(int) == y).mean()
# print("دقت بعد از ۲۰۰ ایپاک:", round(accuracy, 3))
# print("میانگین |خطا|:", round(losses[0], 3), "←", round(losses[-1], 3))

# fig, axes = plt.subplots(2, 2, figsize=(10, 8))
# for ax, (epoch, (ws, bs)) in zip(axes.ravel(), snapshots.items()):
#     ax.scatter(X[y == 0, 0], X[y == 0, 1], color="steelblue", alpha=0.5)
#     ax.scatter(X[y == 1, 0], X[y == 1, 1], color="coral", alpha=0.5)
#     xs = np.array([-1.0, 12.0])
#     ax.plot(xs, -(ws[0]*xs + bs) / ws[1], "k-", linewidth=2)
#     ax.set_xlim(-1, 12)
#     ax.set_ylim(-1, 12)
#     ax.set_title(f"epoch {epoch}")
# plt.suptitle("Decision boundary during training", fontsize=14)
# plt.tight_layout()
# plt.show()

# plt.figure(figsize=(8, 4))
# plt.plot(losses, color="purple", linewidth=2)
# plt.xlabel("Epoch")
# plt.ylabel("Mean |error|")
# plt.title("Training loss")
# plt.grid(alpha=0.3)
# plt.show()


# for lr in [0.01, 0.5, 20]:                       # ✏️ تبدیلش کن به [0.01, 0.5, 20]
#     w_try, b_try = np.array([-1.0, 1.0]), 0.0
#     losses_try = []
#     for _ in range(200):
#         error = sigmoid(X @ w_try + b_try) - y
#         w_try = w_try - lr * (X.T @ error) / len(X)
#         b_try = b_try - lr * error.mean()
#         losses_try.append(np.abs(error).mean())
#     plt.plot(losses_try, linewidth=2, label=f"learning rate = {lr}")

# plt.xlabel("Epoch")
# plt.ylabel("Mean |error|")
# plt.legend()
# plt.grid(alpha=0.3)
# plt.show()


# X2, y2 = make_circles(n_samples=300, factor=0.45, noise=0.08, random_state=42)

# plt.figure(figsize=(5.5, 5.5))
# plt.scatter(X2[y2 == 0, 0], X2[y2 == 0, 1],
#             color="steelblue", alpha=0.7, label="class 0")
# plt.scatter(X2[y2 == 1, 0], X2[y2 == 1, 1],
#             color="coral", alpha=0.7, label="class 1")
# plt.title("Concentric data")
# plt.legend()
# plt.show()

# w, b = np.array([-1.0, 1.0]), 0.0
# for epoch in range(500):
#     error = sigmoid(X2 @ w + b) - y2
#     w = w - 0.5 * (X2.T @ error) / len(X2)
#     b = b - 0.5 * error.mean()

# accuracy = ((sigmoid(X2 @ w + b) > 0.5).astype(int) == y2).mean()
# print("نورون تنها، ۵۰۰ ایپاک، دقت:", round(accuracy, 3))


def plot_boundary(predict, X, y, title=""):
    gx, gy = np.meshgrid(np.linspace(X[:, 0].min() - 0.3, X[:, 0].max() + 0.3, 200),
                         np.linspace(X[:, 1].min() - 0.3, X[:, 1].max() + 0.3, 200))
    grid = np.c_[gx.ravel(), gy.ravel()]
    zz = predict(grid).reshape(gx.shape)
    plt.contourf(gx, gy, zz, levels=[-0.5, 0.5,
                 1.5], colors=["#d6e4f0", "#ffddcc"])
    plt.scatter(X[y == 0, 0], X[y == 0, 1], color="steelblue", s=15)
    plt.scatter(X[y == 1, 0], X[y == 1, 1], color="coral", s=15)
    plt.title(title)


# plt.figure(figsize=(5.5, 5.5))
# plot_boundary(lambda G: (sigmoid(G @ w + b) > 0.5).astype(int), X2, y2,
#               "Single neuron: linear boundary")
# plt.show()


def train_network(X, y, hidden=4, learning_rate=2.0, epochs=4000, seed=42):
    rng = np.random.default_rng(seed)
    W1 = rng.normal(0, 1, (X.shape[1], hidden))   # وزن‌های ورودی ← پنهان
    b1 = np.zeros(hidden)
    W2 = rng.normal(0, 1, (hidden, 1))            # وزن‌های پنهان ← خروجی
    b2 = np.zeros(1)
    y_col = y.reshape(-1, 1)
    losses = []

    for epoch in range(epochs):
        # گذر رو به جلو
        H = sigmoid(X @ W1 + b1)                  # فعال‌سازی‌های پنهان
        out = sigmoid(H @ W2 + b2)                # احتمال خروجی

        # پس‌انتشار خطا
        delta_out = out - y_col                              # dL/dz در خروجی
        delta_hidden = (delta_out @ W2.T) * H * \
            (1 - H)      # dL/dz در لایه پنهان

        # گام گرادیان کاهشی (گرادیان = ورودیᵀ @ delta، میانگین‌گیری‌شده)
        W2 -= learning_rate * (H.T @ delta_out) / len(X)
        b2 -= learning_rate * delta_out.mean(0)
        W1 -= learning_rate * (X.T @ delta_hidden) / len(X)
        b1 -= learning_rate * delta_hidden.mean(0)

        losses.append(np.abs(delta_out).mean())

    return (W1, b1, W2, b2), losses


def predict_network(params, X):
    W1, b1, W2, b2 = params
    H = sigmoid(X @ W1 + b1)
    return (sigmoid(H @ W2 + b2)[:, 0] > 0.5).astype(int)


print("پیاده‌سازی شبکه کامل شد ✅")
# params, losses_net = train_network(X2, y2, hidden=4)

# accuracy = (predict_network(params, X2) == y2).mean()
# print("شبکه با ۴ نورون پنهان:", round(accuracy, 3))

# plt.figure(figsize=(5.5, 5.5))
# plot_boundary(lambda G: predict_network(params, G), X2, y2,
#               "Two-layer network: closed decision region")
# plt.show()

# W1, b1, W2, b2 = params
# gx, gy = np.meshgrid(np.linspace(-1.5, 1.5, 200), np.linspace(-1.5, 1.5, 200))
# H_grid = sigmoid(np.c_[gx.ravel(), gy.ravel()] @ W1 + b1)

# fig, axes = plt.subplots(1, 4, figsize=(14, 3.6))
# for j, ax in enumerate(axes):
#     ax.contourf(gx, gy, H_grid[:, j].reshape(
#         gx.shape), levels=20, cmap="Greys")
#     ax.scatter(X2[y2 == 0, 0], X2[y2 == 0, 1], color="steelblue", s=6)
#     ax.scatter(X2[y2 == 1, 0], X2[y2 == 1, 1], color="coral", s=6)
#     ax.set_title(f"hidden neuron {j + 1}")
# plt.suptitle(
#     "Each hidden neuron: one soft linear boundary; their combination bounds the inner region", fontsize=12)
# plt.tight_layout()
# plt.show()

points = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
labels = np.array([0, 1, 1, 0])

plt.figure(figsize=(5, 5))
for (x1, x2), lab in zip(points, labels):
    color = "mediumseagreen" if lab == 1 else "gray"
    plt.scatter(x1, x2, s=500, color=color, edgecolor="black", zorder=3)
    plt.text(x1, x2 - 0.18, f"{x1} XOR {x2} = {lab}", ha="center", fontsize=11)
plt.xlim(-0.5, 1.5)
plt.ylim(-0.7, 1.5)
plt.title("XOR is not linearly separable")
plt.grid(alpha=0.3)
plt.show()

params, losses_net = train_network(points, labels, hidden=4)

accuracy = (predict_network(params, points) == labels).mean()
print("شبکه با ۴ نورون پنهان:", round(accuracy, 3))

plt.figure(figsize=(5.5, 5.5))
plot_boundary(lambda G: predict_network(params, G), points, labels,
              "Two-layer network: closed decision region")
plt.show()

params_xor, _ = train_network(points.astype(float), labels, hidden=4)

print("پیش‌بینی:", predict_network(params_xor, points.astype(float)))
print("برچسب‌ها: ", labels)
