# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

from run import InputParser, Automata


def test_problem1():
    curr_path = os.getcwd()
    os.chdir(curr_path + '/P1/In')
    test_input_list = os.listdir()
    for test_input in test_input_list:
        if test_input.startswith("in"):
            test_input_file = open(test_input, 'r')
            input_parser = InputParser(test_input_file)
            regex = input_parser.get_expression().split('\n')[0]


def test_problem2():
    curr_path = os.getcwd()
    # Prepare result set of test files
    os.chdir(curr_path + '/P2/Out')
    test_output_list = os.listdir()
    test_output_result_set = {}
    for test_output in test_output_list:
        test_output_file = open(test_output, 'r')
        test_output_result_set[test_output] = test_output_file.readline().split('\n')[0]
        test_output_file.close()
    # Prepare input files
    os.chdir(curr_path + '/P2/In')
    test_input_list = os.listdir()
    for test_input in test_input_list:
        if test_input.startswith("in"):
            test_input_file = open(test_input, 'r')
            input_parser = InputParser(test_input_file)
            input_parser.parser()
            # simulate NFA
            nfa = Automata(input_parser.get_n(), input_parser.get_a(), input_parser.get_t(),
                           input_parser.get_expression(), input_parser.get_accept_states(),
                           input_parser.get_transaction_table())
            nfa.simulation()
            res = nfa.get_result()
            # format file name
            file_number = test_input[2:].split('.txt')[0]
            file_name_result = 'out' + file_number + '.txt'
            print("TEST_INPUT:" + test_output_result_set[file_name_result])
            print("RESULT_SET:" + res)
            if test_output_result_set[file_name_result] == res:
                print(test_input + ': ++++++++++PASS++++++++++')
            else:
                print(test_input + ': ++++++++++FAIL++++++++++')
            test_input_file.close()


def read_input_for_problem2():
    while True:
        expression = input("Enter expression: ")
        if not expression:
            break
        parameters = input("Enter n a t: ")
        accept_states = input("Enter accept states: ")
        input_parser = InputParser()
        input_parser.set_expression(expression)
        input_parser.set_parameters(parameters)
        input_parser.set_accept_states(accept_states)
        print("Enter transition function line by line")
        trans_line = input()
        state_index = 0
        while trans_line:
            input_parser.set_transition_table(trans_line, state_index)
            trans_line = input()
            state_index += 1
        # simulate NFA
        nfa = Automata(input_parser.get_n(), input_parser.get_a(), input_parser.get_t(),
                       input_parser.get_expression(), input_parser.get_accept_states(),
                       input_parser.get_transaction_table())
        nfa.simulation()
        res = nfa.get_result()
        print("Result is: ", res)


def run_test():
    curr_path = os.getcwd()
    os.chdir(curr_path + '/Public_tests')
    test_problem2()
    read_input_for_problem2()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_test()
