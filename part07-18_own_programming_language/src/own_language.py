# Write your solution here
import string

data_set = {i:0 for i in list(string.ascii_uppercase)}

def _split_command_(string): # split the command
    return string.split()

def _mov_(command):
    data_set[command[1]] = command[2]
    
def _add_(command):
    data_set[command[1]] += command[2]

def _sub_(command):
    data_set[command[1]] -= command[2]

def _mul_(command):
    data_set[command[1]] *= command[2]

def _print_(command):
    result.append(data_set[command[1]])


def run(prog: list): # run the program 

    global result # making result global
    result = []

    global index
    index = 0

    while index < len(prog):
        command = _split_command_(prog[index])
        _command_name_ = command[0]

        if _command_name_ == "END":
            break
        elif _command_name_ == "MOV":
            _mov_(command)
        elif _command_name_ == "PRINT":
            _print_(command)
        elif _command_name_ == "ADD":
            _add_(command)
        elif _command_name_ == "SUB":
            _sub_(command)
        elif _command_name_ == "MUL":
            _mul_(command)
        elif _command_name_ == "JUMP":
            label = command[1]
            try:
                index = prog.index(label, index + 1)  # Look for the label after the current index
            except ValueError:
                pass
        elif _command_name_ == "IF":
            condition = command[1]  # Condition to evaluate
            value1 = data_set[command[1]]  # Value of variable A
            value2 = data_set[command[3]]  # Value of variable B
            if condition == ">=" and value1 >= value2:
                label = command[5]  # Get the label to jump to
                index = prog.index(label)
                continue  # Skip incrementing index in this case
            elif condition == "<=" and value1 <= value2:
                label = command[5]  # Get the label to jump to
                index = prog.index(label)
                continue  # Skip incrementing index in this case
            elif condition == ">" and value1 > value2:
                label = command[5]  # Get the label to jump to
                index = prog.index(label)
                continue  # Skip incrementing index in this case
            elif condition == "<" and value1 < value2:
                label = command[5]  # Get the label to jump to
                index = prog.index(label)
                continue  # Skip incrementing index in this case
            elif condition == "==" and value1 == value2:
                label = command[5]  # Get the label to jump to
                index = prog.index(label)
                continue  # Skip incrementing index in this case
            elif condition == "!=" and value1 != value2:
                label = command[5]  # Get the label to jump to
                index = prog.index(label)
                continue  # Skip incrementing index in this case
        
        index += 1

    return result



if __name__ == "__main__":
    program4 = []
    program4.append("MOV N 50")
    program4.append("PRINT 2")
    program4.append("MOV A 3")
    program4.append("begin:")
    program4.append("MOV B 2")
    program4.append("MOV Z 0")
    program4.append("test:")
    program4.append("MOV C B")
    program4.append("new:")
    program4.append("IF C == A JUMP error")
    program4.append("IF C > A JUMP over")
    program4.append("ADD C B")
    program4.append("JUMP new")
    program4.append("error:")
    program4.append("MOV Z 1")
    program4.append("JUMP over2")
    program4.append("over:")
    program4.append("ADD B 1")
    program4.append("IF B < A JUMP test")
    program4.append("over2:")
    program4.append("IF Z == 1 JUMP over3")
    program4.append("PRINT A")
    program4.append("over3:")
    program4.append("ADD A 1")
    program4.append("IF A <= N JUMP begin")
    result = run(program4)
    print(result)
