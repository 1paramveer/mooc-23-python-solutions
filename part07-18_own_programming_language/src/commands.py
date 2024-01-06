from own_language import data_set

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


