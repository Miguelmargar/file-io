while True:    
    menu = {
        "a": "ask a question",
        "b": "add a question",
        "e": "exit game"
    }
  
    print(menu)
    choice = input("what do you want to do? a, b or e: ")
        
    questions = {
        "who's going to win the world cup": "japan",
        "who's going to be runner up in the world cup": "germany"
    }   
        
      
        
    def ask_question():
        counter = 0
        for k, v in questions.items():
            user_answer = input(k)
            if user_answer == v:
                print("Correct answer")
                counter += 1
            else:
                print("incorrect answer")
            
        print(counter)  
    
    
        
    def add_question():
        user_question = input("Write a question ")
        user_answer = input("What is the answer? ")
        questions[user_question] = user_answer
        print(questions)
        
        
        
    if choice == "a":
        ask_question()
    elif choice == "b":
        add_question()
    else:
        break

