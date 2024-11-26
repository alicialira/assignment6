import sys
import json

def validate_input(numbers):
    try:
        return [int(num) for num in numbers.split(",")]
    except ValueError:
        print("Error: Input must contain only integers separated by commas.")
        sys.exit(1)

def bitwise_operations(numbers):
    result = {
        "AND": numbers[0],
        "OR": numbers[0],
        "XOR": numbers[0]
    }
    for num in numbers[1:]:
        result["AND"] &= num
        result["OR"] |= num
        result["XOR"] ^= num
    return result

def filter_numbers(numbers, threshold):
    return [num for num in numbers if num > threshold]

if __name__ == "__main__":
    # Read inputs from command-line arguments
    input_data = json.loads(sys.argv[1])
    numbers = validate_input(input_data["integers"])
    threshold = int(input_data["threshold"])

    bitwise_result = bitwise_operations(numbers)
    filtered_numbers = filter_numbers(numbers, threshold)

    output = {
        "bitwise": bitwise_result,
        "filtered": filtered_numbers
    }

    print(json.dumps(output))
