from collections import Counter

def print_statistics(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    mode = Counter(numbers).most_common(1)[0][0]
    
    print(f"min, max, sum, average and mode after addition of {numbers[-1]} is {minimum}, {maximum}, {total_sum}, {average}, {mode}.")

def process_stream(stream):
    numbers = []
    for num in stream:
        numbers.append(num)
        print_statistics(numbers)


