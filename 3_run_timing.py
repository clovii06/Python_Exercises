# 3. Run Timing

"""
Pseudocode:
function run_timing():
    total_run_time = 0
    number_of_runs = 0

    while True:
        if not run_time:
            break

        get run_time
        total_run_time += run_time
        number_of_runs += 1

    average_run_time = total_run_time / number_of runs
    display average
"""

def run_timing():
    total_run_time = 0
    number_of_runs = 0

    while True:
        run_time = input("Enter run time: ")

        if not run_time:
            break

        total_run_time += float(run_time) # Convert to float
        number_of_runs += 1

    average_run_time = total_run_time / number_of_runs
    print(f"Average run time: {average_run_time}")

run_timing()