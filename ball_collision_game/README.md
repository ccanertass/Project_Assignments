<h2>Game Overview</h2>
<p>
    In this game, a white ball (*) moves across a board based on the player's commands.
    The player can move the ball in four directions: Right (R), Left (L), Up (U), and Down (D).
    The objective is to navigate the board while collecting points from different colored balls
    and avoiding holes (H), which end the game upon contact.
</p>

<h3>Game Rules</h3>
<ul>
    <li>The white ball (*) moves horizontally or vertically one cell at a time.</li>
    <li>If the white ball moves onto a Red (R), Yellow (Y), or Black (B) ball, it replaces that ball, and the ball turns into an X.</li>
    <li>If the white ball moves onto a Hole (H), the game ends as the ball falls into the hole.</li>
    <li>If the white ball moves into a Wall (W), it cannot pass and bounces back two units in the opposite direction.</li>
    <li>If the white ball encounters an already replaced cell (X), it swaps with it.</li>
</ul>

<h2>Input Files</h2>
<p>The game requires two input text files:</p>
<ul>
    <li><strong>board.txt</strong>: Contains the exact representation of the board.</li>
    <li><strong>move.txt</strong>: Contains the moves made by the player in the order they play them.</li>
</ul>

<h2>Running the Program</h2>
<h3>1. Prepare the Input Files</h3>
<ol>
    <li>Open the <strong>IO</strong> directory.</li>
    <li>Choose either <strong>IO1</strong> or <strong>IO2</strong>.</li>
    <li>Navigate to the <strong>input</strong> folder.</li>
    <li>Copy both <code>board.txt</code> and <code>move.txt</code>.</li>
    <li>Paste them into the <code>src</code> folder.</li>
</ol>

<h3>2. Compile the Code</h3>
<p>Navigate to the <code>src</code> folder and run one of the following commands:</p>
<pre>
javac *.java
</pre>
<p>or</p>
<pre>
javac Main.java
</pre>

<h3>3. Generate and Compare Output</h3>
<ol>
    <li>After compilation, an <code>output.txt</code> file will be generated in the <code>src</code> folder.</li>
    <li>Compare the generated <code>output.txt</code> with the <code>output.txt</code> from the <strong>IO1</strong> or <strong>IO2</strong> folder (whichever you chose earlier).</li>
</ol>

<p>Ensure that the generated output matches the expected output to verify the correctness of the program.</p>
