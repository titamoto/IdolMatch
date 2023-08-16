from db import seeds
from simple_term_menu import TerminalMenu
import re
from db.models import User
from db.test import questions

greeting = 'Welcome to IdolMatch!'

if __name__ == '__main__':
    #run seeds.py

    def main():
        print(greeting)
        print('Please enter your email:')
        email_input = input()
        if re.fullmatch(r'^\D[a-zA-Z0-9\.]+@[a-zA-Z]+\.[a-z]+', email_input):
            search_email(email_input)
        else:
            print('The input is invalid. Try again')

    def search_email(email):
        if User.email_found(email) == True:
            print('You have already done the test. What do you want:')
            options = ["show result", "redo the test", "back to main"]
            terminal_menu = TerminalMenu(options)
            menu_entry_index = terminal_menu.show()
            if menu_entry_index == 0:
                show_result(email)
            elif menu_entry_index == 1:
                start_test(email)
            else:
                main()
        else:
            start_test(email)

    def show_result(email):
        User.get_result(email)
        options = ["back to main", "redo the test"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        if menu_entry_index == 0:
            main()
        elif menu_entry_index == 1:
            start_test(email)       


    def start_test(email):
        User.delete_result(email)
        answers = []
        count = 0
        while count < len(questions):
            ask_question()
            count += 1
            answers.append(answer)
        calculate_result()
        persist_result(email)
        show_result(email)
    
    #run main menu:
    main()
    

#ask for email +
#search for email +
#email is in db -- confirm email -
    #yes -- show result/redo the test/exit +
    #no -- ask for email -
#email is not found: +
    #start quiz: +
    #show question, show the same instruction, ask for input 
    #check if input is in range 1 to 5
        #yes -- append answers list, ask next one
        #no -- print answer should be in range of 1 to 5
    #when no more questions -- ask if user wants result
        #no, too shy, exit
        #yes
            #process answers -- show result
            #redo the test/exit

