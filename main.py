from app import create_calculator
from app.input_validators import validate_number
from app.exceptions import CalculatorError
from app.calculation import Calculation
import pandas as pd
from colorama import init, Fore, Style

init(autoreset=True)

def print_help():
    print("Commands:")
    print("  add, subtract, multiply, divide, power, root, modulus, int_divide, percent, abs_diff")
    print("  history - display calculation history")
    print("  clear   - clear calculation history")
    print("  undo    - undo last calculation")
    print("  redo    - redo last undone calculation")
    print("  save    - save history to file")
    print("  load    - load history from file")
    print("  help    - show this message")
    print("  exit    - exit the application")

def main():
    calc = create_calculator()
    config = calc.config
    print("Enhanced Calculator. Type 'help' for commands.")

    while True:
        cmd = input("calc> ").strip()
        if not cmd:
            continue

        if cmd == "exit":
            break
        elif cmd == "help":
            print_help()
        elif cmd == "history":
            for c in calc.get_history():
                print(f"[{c.timestamp}] {c.operation}({c.a}, {c.b}) = {c.result}")
        elif cmd == "clear":
            calc.history.clear()
            print("History cleared.")
        elif cmd == "undo":
            try:
                calc.undo()
                print("Undone.")
            except CalculatorError as e:
                print(Fore.RED + f"Error: {e}")
        elif cmd == "redo":
            try:
                calc.redo()
                print("Redone.")
            except CalculatorError as e:
                print(Fore.RED + f"Error: {e}")
        elif cmd == "save":
            df = pd.DataFrame([c.to_dict() for c in calc.get_history()])
            df.to_csv(config["history_file"], index=False)
            print(f"History saved to {config['history_file']}")
        elif cmd == "load":
            try:
                df = pd.read_csv(config["history_file"])
                calc.history.clear()
                for _, row in df.iterrows():
                    calc.history.add(Calculation.from_dict(row.to_dict()))
                print("History loaded.")
            except FileNotFoundError:
                print(Fore.RED + "No history file found.")
            except pd.errors.EmptyDataError:
                print(Fore.RED + "History file is empty or malformed.")
        else:
            parts = cmd.split()
            if len(parts) != 3:
                print(Fore.YELLOW + "Usage: <operation> <a> <b>")
                continue
            op_name, a_raw, b_raw = parts
            try:
                a = validate_number(a_raw, calc.config["max_input"])
                b = validate_number(b_raw, calc.config["max_input"])
                c = calc.calculate(op_name, a, b)
                print(Fore.GREEN + f"= {c.result}")
            except CalculatorError as e:
                print(Fore.RED + f"Error: {e}")

if __name__ == "__main__":
    main()
