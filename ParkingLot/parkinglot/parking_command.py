import subprocess
import argparse

def execute_commands(input_file, output_file):
    try:
        with open(input_file, "r") as input_file, open(output_file, "w") as output_file:
            for line in input_file:
                line = 'python manage.py ' + line
                try:
                    result = subprocess.check_output(line, shell=True, stderr=subprocess.STDOUT, text=True)
                    output_file.write(f"Command: {line}")
                    output_file.write(result)
                    output_file.write("\n\n")
                except subprocess.CalledProcessError as e:
                    output_file.write(f"Command: {line}")
                    output_file.write(f"Error: {e.output}\n\n")
        print("Commands executed and results written to 'results.txt'")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Execute commands from an input file and save results to an output file.")
    parser.add_argument("input_file", help="Path to the input file containing commands.")
    parser.add_argument("output_file", help="Path to the output file where results will be saved.")
    args = parser.parse_args()

    execute_commands(args.input_file, args.output_file)
