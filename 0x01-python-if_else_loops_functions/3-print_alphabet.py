#!/usr/bin/python3

# Print the ASCII alphabet, in lowercase, not followed by a new.
for alphabet in range(97, 123):
    if alphabet == 101 or alphabet == 113:
        continue
    print(f"{alphabet:c}", end='')