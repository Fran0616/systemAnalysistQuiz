class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer
#name of list that stores the question
question_prompts = ["1. Objected Oriented System Analysis and Design (OOSAD) is a technique that integrates Data and Processes into elements called Objects.(True/False)\n",
                    "2. For system analysis and design, the requirements indicate how the system should behave, and the features and functions it should possess.  (True/False)\n",
                    "3. Feasibility analysis investigates economic, organizational, technical, resource, and schedule feasibility. (True/False)\n",
                    "4. Requirements Engineering is the act of only gathering users’ and stakeholders’ needs and constraints for the system. (True/False)\n",
                    "5. A model is a representation of an important aspect of the real world. (True/False)\n",
                    "6. A requirement for a mobile app to run on an IOS platform is consider a functional requirement. (True/False)\n",
                    "7. A project cannot have both predictive and adaptive elements. (True/False)\n",
                    "8. Technology alone increases productivity and profits. (True/False)\n",
                    "9. Identifying a problem/opportunity should consider and focus on all the following, except: (Multiple Choice)\n a. Who is affected\n b. The solution\n c. Complexity\n d. Regional impact ",
                    "10. Inheritance relationships exist between: (Multiple Choice)\n a. instances and classe\n b. a superclass and subclasses\n c. an actor and a use case\n d. attributes and methods",
                    "11. All the following are types of non-functional requirements, except: (Multiple Choice)\n a. Business\n b. Operation\n c. Performance\n d. Security\n",
                    "12. The most important role of a systems analyst in business is ____________________. (Multiple Choice)\n a. understanding the business\n b. problem solving\n c. knowing what data needs to be stored and used\n d.	special programming skills\n",
                    "13. Susan is asked to manage a small team. When she met with the team for the first time the group discussed the feasibility study in which they are currently performing. Susan knows then knows they are in ______________________ phase of the SDLC? (Multiple Choice)\n a. systems analysis\n b. systems design\n c. systems planning\n d. systems implementation\n",
                    "14. Challenges to global software development include all the following, except: (Multiple Choice)\n a. Management issues/n b. Less skilled labor force\n c. Political and cultural differences\n d. Geographical differences\n",
                    "15. Which of the following is the analyst’s approach to problem solving? (Multiple Choice)\n a. Verify that the benefits of solving the problem outweigh the costs, then research and understand the problem.\n b. Develop a set of possible solutions, then verify that the benefits of solving the problem outweigh the costs.\n c. Verify that the benefits of solving the problem outweigh the costs, then define the requirements for solving the problem.\n d. Implement the solution, then define the details of the chosen solution."
                  
            

    ]
#name of list that stores the correct answers for each question on the question promt
questions = [
     Question(question_prompts[0], "t"),
     Question(question_prompts[1], "t"),
     Question(question_prompts[2], "t"),
     Question(question_prompts[3], "f"),
     Question(question_prompts[4], "t"),
     Question(question_prompts[5], "f"),
     Question(question_prompts[6], "f"),
     Question(question_prompts[7], "f"),
     Question(question_prompts[8], "b"),
     Question(question_prompts[9], "b"),
     Question(question_prompts[10], "a"),
     Question(question_prompts[11], "b"),
     Question(question_prompts[12], "c"),
     Question(question_prompts[13], "b"),
     Question(question_prompts[14], "c")    
]
#function that determines if the answer is correct and how many you got correct
def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("you got", score, "out of", len(questions))

run_quiz(questions)
