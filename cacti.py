def cacti_number(value):
    def wrapper(plot):
        if not (isinstance(plot, list)):
            raise TypeError("Input should be a list only.")
       
        x = len(plot) - 1
        y = len(plot[0]) - 1 
             
        x_line = (0, x)
        y_line = (0, y)
        
        count = 0
        
        for i in range(len(plot)):
            for j in range(len(plot[0])):
                if plot[i][j] == 0:
                    
                    valid_check = True
                    
                    if not out_of_range(y_line, j + 1):
                        if plot[i][j + 1] == 1:   
                            valid_check = False
                            
                    if not out_of_range(y_line, j - 1):   
                        if plot[i][j - 1] == 1:       
                            valid_check = False
                    
                    if not out_of_range(x_line, i - 1):
                        if plot[i - 1][j] == 1:   
                            valid_check = False
                    
                    if not out_of_range(x_line, i + 1):
                        if plot[i + 1][j] == 1:   
                            valid_check = False
                        
                    if valid_check:
                        count += 1
                        plot[i][j] = 1
               
        return count
    return wrapper

def out_of_range(bound, steps):
        
        if (bound[0] > steps or bound[1] < steps):
            return True
        else:
            return False