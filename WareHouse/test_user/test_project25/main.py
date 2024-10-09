import subprocess
subprocess.check_call(["pip", "install", "asteval"])
from calculator import CalculatorFrame, CalcButton
def main():
    root = tk.Tk()
    root.title("Calculator")
    calc_frame = CalculatorFrame(root)
    calc_frame.pack()
    root.mainloop()
if __name__ == "__main__":
    main()