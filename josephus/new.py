def main():
    queue_of_patients({"Ali": 25, "Bob": 15, "Joma": 2, "Farzad": 5, "Alex": 34, "Haji": 15 })


def queue_of_patients(mydict):
    list_times = []
    min_time = 0
    for key in mydict.keys():
        list_times.append(mydict[key])
    
    list_times.sort()

    index = 0
    while index < len(list_times):
        for k, v in mydict.items():
            if list_times[index] == v:
                print(k, end= " ")
                min_time += v * ((len(list_times)- index) - 1)
        index += 1
    print()
    print(f"min_time: {min_time}")
    
    



main()