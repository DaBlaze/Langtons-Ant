# Langton's Ant

A simple implementation of [Langton's Ant](https://en.wikipedia.org/wiki/Langton%27s_ant) in Python. This script uses the built-in turtle module for functionality.

![Langton's Ant program running](https://dablaze.io/assets/images/github/langtons-ant/langtons-ant-example.png)

The ant follows three simple rules:

1. If the ant is on a white square, it turns right and moves forward.

2. If the ant is on a black square, it turns left and moves foward.

3. Before the ant leaves the square, it inverts the color of the square.

After taking around 10,000 steps the ant will enter a repeating pattern and create an infinite "highway."

## How to Run

```bash
# Clone the repo
git clone https://github.com/dablaze/Langtons-Ant.git

# Enter the repo directory
cd Langtons-Ant

# Run the program
python3 main.py
```
