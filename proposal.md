# Title

Big-O: How Code Slows as Data Grows


# Duration

30 minutes


# Description

Big-O is a computer science technique for analyzing how code performs as data gets larger.  It's a very handy tool for the working programmer, but it's often shrouded in off-putting mathematics.

In this talk, I'll teach you what you need to know about Big-O, and how to use it to keep your programs running well.  Big-O helps you choose the data structures and algorithms that will let your code work efficiently even on large data sets.

You can understand Big-O even if you aren't a theoretical computer science math nerd. Big-O isn't as mystical as it appears. It's wrapped in mathematical trappings, but doesn't have to be more than a common-sense assessment of how your code will behave.


# Who and Why (Audience)

This talk is aimed at people without formal computer science training, especially people who feel insecure because of it!  They should have written their own programs, and have a little familiarity with the basic Python data structures.  They will leave with an appreciation for why data structures are used as they are, and how to choose data structures and algorithms that are right for the job.


# Outline

- What is Big-O? (5 min)
    - "How code slows as data grows"
    - It's a summary of how runtime changes as data gets larger
    - Often presented with a lot of math
        - You can understand it without the math
    - Terminology
        - N is size of data, O(f(N)) is how the time grows
        - O() means "Order of"
    - Real-world examples to get a feel for it
        - Counting jellybeans
            - O(N) vs O(1)
        - Finding words in books
            - O(N) vs O(log N)
- Determining Big-O (10 min)
    - How to figure Big-O
        - Decide what N means (the size of your data)
        - Count the steps in a typical run of the code
            - What is a step?
                - Any unit of work that doesn't depend on N
                - Differences between different units can be glossed over
        - Discard lower-order components and coefficients
            - We only need the long-term growth, so only keep the most significant parts
    - An example: `find_mom()`
        - Searches a list of pairs
        - O(N)
    - Another example: `how_many_grandmothers()`
        - Calls `find_mom()` once for each mom
        - N times O(N)
        - O(N**2)
- More theory (7 min)
    - The graph of different runtimes
        - Ideal: O(1)
        - Avoid: O(N**2)
    - Python primitives and their complexities
        - Table of operations for list, dict, set
    - Last example: point matching, linear search vs clever O(1)
        - Real code: small code is O(N), big code is O(1)
        - Size of code can be misleading
- Other points (6 min)
    - Often, big-O doesn't matter
        - "Fancy algorithms are slow when N is small, and N is usually small."
    - Amortization
        - Not every operation has the same run-time
    - Expected vs worst-case
        - Hash randomization
    - The internet can be harsh: "You should be ashamed"


# Additional Notes



