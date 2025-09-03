# Simple Calculator GUI using Tkinter
import tkinter as tk

def on_click(char):
    if char == 'C':
        entry.delete(0, tk.END)
    elif char == '=':
        try:
            # Replace the unicode multiplication and division with python operators
            import ast, operator

            expression = entry.get().replace('×', '*').replace('÷', '/')

            # Define allowed operators
            allowed_operators = {
                ast.Add: operator.add,
                ast.Sub: operator.sub,
                ast.Mult: operator.mul,
                ast.Div: operator.truediv,
                ast.USub: operator.neg
            }

            def eval_expr(node):
                if isinstance(node, ast.Num):  # <number>
                    return node.n
                elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
                    if type(node.op) in allowed_operators:
                        return allowed_operators[type(node.op)](eval_expr(node.left), eval_expr(node.right))
                    else:
                        raise ValueError("Unsupported operator")
                elif isinstance(node, ast.UnaryOp):  # - <operand>
                    if type(node.op) in allowed_operators:
                        return allowed_operators[type(node.op)](eval_expr(node.operand))
                    else:
                        raise ValueError("Unsupported unary operator")
                else:
                    raise ValueError("Invalid expression")
            try:
                node = ast.parse(expression, mode='eval').body
                result = str(eval_expr(node))
            except Exception:
                result = "Error"
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, char)

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=12, font=('Arial', 24), borderwidth=2, relief='ridge', justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=8, pady=8)

# Define the button layout to match the image
button_layout = [
    ['C', '7', '8', '9', '÷'],
    [None, '4', '5', '6', '×'],
    [None, '1', '2', '3', '-'],
    [None, '0', '.', '=', '+']
]

for row, row_vals in enumerate(button_layout):
    for col, char in enumerate(row_vals):
        if char is None:
            continue
        btn = tk.Button(root, text=char, width=4, height=2, font=('Arial', 20),
                        command=lambda ch=char: on_click(ch))
        btn.grid(row=row+1, column=col, padx=4, pady=4)

root.mainloop()