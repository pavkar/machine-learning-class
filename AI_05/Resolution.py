import copy

def invert(listToInvert):
    toReturn = []
    
    if (listToInvert == None):
        return toReturn
 
    for i in listToInvert:
        toReturn.append(-i)
    return toReturn

def subsume(list1, list2):
    if list1 == None or list2 == None:
        return []
    return all(element in list2 for element in list1)


def is_subsumed(processed, nextCandidate):
    for subsumedProcess in processed:
        if subsume(subsumedProcess, nextCandidate):
            return True
    return False

def resolve(nextCandidate, notSubsumedProcess):
    toReturn = []
    
    if nextCandidate == None or notSubsumedProcess == None:
        return toReturn
    
    for x in nextCandidate:
        for y in notSubsumedProcess:
            if (x == -y):
                finalList = []
                
                notSubsumedProcessCopy = list(copy.deepcopy(nextCandidate))
                if len(notSubsumedProcessCopy) > 0:
                    notSubsumedProcessCopy.remove(x)
                    if notSubsumedProcessCopy != None:
                        finalList.extend(notSubsumedProcessCopy)
                
                process = list(copy.deepcopy(notSubsumedProcess))
                if len(process) > 0:
                    process.remove(y)
                    if process != None:
                        finalList.extend(process)
                
                finalList = set(finalList)
                finalList = list(finalList)
                
                toReturn.append(finalList)
    return toReturn
    
def resolution(clauses, alpha):
    
    if clauses == None or alpha == None:
        return False
    
    clauses.extend([invert(alpha)])
    processed = []

    while len(clauses) > 0:
        nextCandidate = clauses.pop(0)

        if not is_subsumed(processed, nextCandidate):
            for notSubsumedProcess in processed:
                resolvents = resolve(nextCandidate, notSubsumedProcess)
                print(resolvents)
                
                for resolvent in resolvents:
                    if len(resolvent) == 0:
                        return True
                    clauses.append(resolvent)
            processed.append(nextCandidate)
    return False

if __name__ == '__main__':
    print(resolution([[1,2], [2,-1],[-2,1]],[2]))
    print(resolution([[1,2], [2,-1],[-2,-1]],[-2]))
