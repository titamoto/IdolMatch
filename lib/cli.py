from simple_term_menu import TerminalMenu
import re
import time
from data.models import User
from data.test import questions
from data.types import types
from seeds import seed
# from db.session import session

greeting =' ____  ____  _____  __    __  __    __   ____  ___  _   _ \n(_  _)(  _ \(  _  )(  )  (  \/  )  /__\ (_  _)/ __)( )_( )\n _)(_  )(_) ))(_)(  )(__  )    (  /(__)\  )( ( (__  ) _ ( \n(____)(____/(_____)(____)(_/\/\_)(__)(__)(__) \___)(_) (_)\n'

if __name__ == '__main__':

    def main():
        print("\n" * 10)
        print(greeting)
        print("Welcome to IdolMatch!")
        ask_email()

    def ask_email():
        print('Please enter your email:')
        email_input = input()
        if re.fullmatch(r'^\D[a-zA-Z0-9\.]+@[a-zA-Z]+\.[a-z]+', email_input):
            search_email(email_input)
        else:
            print('The input is invalid. Try again')
            time.sleep(2)
            ask_email()

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
        result = User.get_result(email)
        print(result)
        time.sleep(2)
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
            answer = ask_question(count)
            count += 1
            answers.append(answer)
        result = calculate_result(answers)
        #create a user record in the database:
        user = User(
            email=email,
            type=result,
            type_alias=types[result]
        )
        user.persist_result()
        show_result(email)
    
    def ask_question(count):
        print (
            f'\n{questions[count]}\n\n'
            'Type a number from 1 to 5, where "1" corresponds with the left statement, \n"5"--with the right, and "3" is neutral:'
                )
        answer = input()
        #breaks if input is not a number
        try:
            answer =int(answer)
        except ValueError:
            print(f'{answer} is not a number from 1 to 5. Try again:')
            return ask_question(count)
        if answer not in range(1, 6):
            print(f'{answer} is not a number from 1 to 5. Try again:')
            return ask_question(count)
        else:
            return answer

    def calculate_result(a):
        ie = 30-a[2]-a[6]-a[10]+a[14]-a[18]+a[22]+a[26]-a[30]
        sn = 12+a[3]+a[7]+a[11]+a[15]+a[19]-a[23]-a[27]+a[31]
        ft = 30-a[1]+a[5]+a[9]-a[13]-a[17]+a[21]-a[25]-a[29]
        jp = 18+a[0]+a[4]-a[8]+a[12]-a[16]+a[20]-a[24]+a[28]
        first_letter = 'E' if ie > 24 else 'I'
        second_letter = 'N' if sn > 24 else 'S'
        third_letter = 'T' if ft > 24 else 'F'
        fourth_letter = 'P' if jp > 24 else 'J'
        result = first_letter + second_letter + third_letter + fourth_letter
        return result
    
    #seed the db:
    seed()
    #run main menu:
    main()
    


