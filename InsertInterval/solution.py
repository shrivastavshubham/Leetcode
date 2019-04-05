= intervals[i]
            #print(stack,elem.start,done)
            if elem.start < newInterval.start:
                stack.append([elem.start,elem.end])
            else:
                if not done:
                    done = True
                    if len(stack)==0:
                        stack.append([newInterval.start,newInterval.end])
                    else:
                        if stack[-1][1] < newInterval.start:
                            stack.append([newInterval.start,newInterval.end])
                        else:
                            if newInterval.end <= stack[-1][1]:None
                            else:stack[-1][1] = newInterval.end
                    i-=1
                else:
                        if stack[-1][1] < elem.start:
                            stack.append([elem.start,elem.end])
                        else:
                            if elem.end <= stack[-1][1]:None
                            else:stack[-1][1] = elem.end
            i+=1
        if not done:
            if stack[-1][1] < newInterval.start:
                stack.append([newInterval.start,newInterval.end])
            else:
                if newInterval.end <= stack[-1][1]:None
                else:stack[-1][1] = newInterval.end
        return stack
                
            
                
        
