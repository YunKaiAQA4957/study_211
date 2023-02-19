import datetime
 
def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.datetime.now()
        res_time = end_time - start_time
        print(f"Время выполнения: {res_time}")
        return result
    return wrapper


@execution_time
def li_num(x, y):
    li = []
    for i in range(x, y+1):
        if i > 1:
            for j in range(2, i):          
                if (i % j) == 0:
                    break
            else:
                li.append(i)
    return li

print(li_num(0, 1000))
print(li_num(50, 5000))