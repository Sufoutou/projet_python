import inquirer

if __name__ == "__main__":

    questions = [
        inquirer.Checkbox("logs", 
                          message="Please define your type of request?", 
                          choices=["@ip", "Hours", "browser", "request GET", "request Post" "Hours",],
                        ),
                ]
    
        

    answers = inquirer.prompt(questions)

    print(answers)