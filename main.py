def task_1(num=3):
    result = ""
    for i in range(1,10+1):
        result += f"{num} * {i} = {num * i}\n"
    print(result)


def task_2():
    my_list = list(range(1,100+1))
    print(sum(my_list)/len(my_list))


def task_3(num):
    if num<50:
        print("You entered too small number")
        return
    number_of_iteration = 0
    while num>50:
        num /= 2
        number_of_iteration += 1
    print(f"min result - {num}, number of iteration - {number_of_iteration}")
    return

print("Task 1")
task_1()
print("*" * 100)
print("Task 2")
task_2()
print("*" * 100)
print("Task 3, with param 40")
task_3(40)
print("Task 3, with param 10000")
task_3(5000)
    

