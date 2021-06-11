from typing import TextIO


class InputParser:
    def __init__(self, input_file: TextIO = None):
        self.text_file = input_file
        self.n = None
        self.a = None
        self.t = None
        self.expression = None      # expression to evaluate
        self.accept_states = []     # list of accept states
        self.transition_table = {}  # {int: {str: list}}  # transition function {state: {symbol: state}}

    def parser(self):
        self.set_expression()
        self.set_parameters()
        self.set_accept_states()
        self.set_transition_table()

    def set_expression(self, standard_exp=None):
        if standard_exp is None:
            self.expression = self.text_file.readline()
        else:
            self.expression = standard_exp

    def set_parameters(self, standard_parameters=None):
        if standard_parameters is None:
            self.n, self.a, self.t = self.text_file.readline().split(" ")
        else:
            self.n, self.a, self.t = standard_parameters.split(" ")
        self.n = int(self.n)
        self.a = int(self.a)
        self.t = int(self.t)

    def set_accept_states(self, states_line=None):
        if states_line is None:
            line = self.text_file.readline().split(" ")
        else:
            line = states_line.split(" ")
        self.accept_states = [int(state) for state in line]

    def set_transition_table(self, transition_line=None, state_index=0):
        if transition_line is None:
            state_index = 0
            for line in self.text_file:
                self._add_transaction_line(line, state_index)
                state_index += 1
        else:
            self._add_transaction_line(transition_line, state_index)

    def _add_transaction_line(self, line: str, state_index: int):
        split_line = line.split(" ")
        k = int(split_line[0])
        split_line = split_line[1:]
        self.transition_table[state_index] = {}
        # read pairs of transitions
        for j in range(k):
            symbol = split_line[2 * j]
            state = int(split_line[2 * j + 1])
            if symbol not in self.transition_table[state_index]:
                state_list = [state]
                self.transition_table[state_index][symbol] = state_list
            else:
                self.transition_table[state_index][symbol].append(state)

    def print_parameters(self):
        print("n: {}, a: {}, t: {}".format(self.n, self.a, self.t))

    def print_expression(self):
        print("Expression: {}".format(self.expression))

    def print_accept_states(self):
        print("Automata accepts states: ", self.accept_states)

    def print_transition_table(self):
        print("Transition table: ", self.transition_table)

    def get_n(self) -> int:
        return self.n

    def get_a(self) -> int:
        return self.a

    def get_t(self) -> int:
        return self.t

    def get_expression(self) -> str:
        return self.expression

    def get_accept_states(self) -> list:
        return self.accept_states

    def get_transaction_table(self) -> dict:
        return self.transition_table


class Automata:
    def __init__(self, n: int, a: int, t: int, expression: str, accept_states: list, transition_table: dict):
        self.n = n
        self.a = a
        self.t = t
        self.expression = expression
        self.accept_states = accept_states
        self.transition_table = transition_table
        self.result = ''
        self.current_state = [0]    # start state is always 0

    def simulation(self):
        for symbol in self.expression:
            if symbol == '\n':
                break
            new_states = []
            for state in self.current_state:
                curr_transitions = self.transition_table[state]  # {symbol: [states]}
                if symbol in curr_transitions:
                    new_states += curr_transitions[symbol]

            self.current_state = new_states
            if self.check_accept_state():
                self.result += 'Y'
            else:
                self.result += 'N'

    def get_result(self) -> str:
        return self.result

    def check_accept_state(self) -> bool:
        for state in self.current_state:
            if state in self.accept_states:
                return True
        return False
