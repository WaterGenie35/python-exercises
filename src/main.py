import cProfile
import importlib.util
from argparse import ArgumentParser
from importlib import import_module


def main():
    parser = ArgumentParser(description="Just some generic programming exercises using Python.")
    parser.add_argument("exercise", choices=['project_euler'])
    parser.add_argument("problem_number", type=int)
    parser.add_argument("-p", "--profile", action='store_true', default=False)
    args = parser.parse_args()
    if args.profile:
        print("Profiling enabled")
    print(f"Exercise:\t{args.exercise}")
    print(f"Problem:\t{args.problem_number}")

    module_name = f"{args.exercise}.problem_{args.problem_number}"
    if args.exercise == 'project_euler':
        problem_group = (args.problem_number - 1) // 50
        group_start = (50 * problem_group) + 1
        group_end = group_start + 50 - 1
        group_dir = f"{group_start}-{group_end}"
        module_name = f"{args.exercise}.{group_dir}.problem_{args.problem_number}"
    if importlib.util.find_spec(module_name):
        problem = import_module(module_name)
        if args.profile:
            cProfile.runctx('problem.solution()', None, locals())
        else:
            problem.solution()
    else:
        print(f"No solution for {args.exercise} problem {args.problem_number} yet.")


if __name__ == '__main__':
    main()
