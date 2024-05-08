# import time 
# t= time.strftime('%H:%M:%S')
# hour = int ( time.strftime ('%H'))
# print(hour )

# if( hour>12):
#   print( "good morning ")

# a = int( input("inter your number : ") )
# print ( a  ) 


# Define a list of questions along with their options and correct answers
questions = [
#     {
#         "question": "What is the capital of India?",
#         "options": ["Delhi", "Mumbai", "Kolkata", "Chennai"],
#         "correct_answer": 1,  # Index of correct answer (0-based)
#     },
#     {
#         "question": "Which planet is known as the Red Planet?",
#         "options": ["Mars", "Venus", "Jupiter", "Saturn"],
#         "correct_answer": 0,
#     },
    
#     # Add more questions here...
# ]

# # Initialize the total winning amount
# total_winning = 0

# # Function to ask a question
# def ask_question(question_data):
#     print(question_data["question"])
#     for i, option in enumerate(question_data["options"], start=1):
#         print(f"{i}. {option}")

#     user_answer = int(input("Enter your choice (1, 2, 3, 4): ")) - 1
#     if user_answer == question_data["correct_answer"]:
#         print("Correct! You win ₹10,000.")
#         return True
#     else:
#         print("Oops! Incorrect answer.")
#         return False

# # Main game loop
# for q in questions:
#     if ask_question(q):
#         total_winning += 10000

# print(f"Congratulations! You won a total of ₹{total_winning}.")

# # Display the final amount won
# print("Thank you for playing KBC!") 

# #  solobve the  qustion on  my  pwn ope


from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)  # Convert 1-based indexing to 0-based indexing
    graph[b - 1].append(a - 1)

visited = [False] * n
parent = [-1] * n
queue = deque([0])
visited[0] = True

while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            parent[neighbor] = node
            queue.append(neighbor)

# Reconstruct the path from end to start
path = []
while n - 1 != -1:
    path.append(n - 1)  # Convert back to 0-based indexing
    n = parent[n - 1]

if path[-1] == 0:
    print(len(path))
    print(*path[::-1])  # Reverse the path to get start to end order
else:
    print("IMPOSSIBLE")
