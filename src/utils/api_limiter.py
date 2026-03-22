from src.db.api_usage import check_usage

def api_limit():
    
    if (check_usage()) < 30:
        
        return(1) #safe
    else:
        return(0) #limit reached

#END WITH TUSHAR