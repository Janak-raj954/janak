import tkinter as tk
from tkinter import messagebox



questions = {'Which of the following is used for comments in Python' : 'C'
    ,"What will be the output of: l = [['janak'] , [['first year']] ; print(l[0][-2])":'B' ,
    'Which of the following is a valid variable name in Python?' : 'B' ,
    ' Which of the following statements is used to exit a loop in Python?' : 'A'
    ,"What is the output of print(2**3)?": "B",
    "Which data type is used to store True/False values?": "C",
    "Which of these is a mutable data type?": "C",
    "What is the output: print(3 == 3.0)?": "B",
    "What does the len() function do?": "B",
    "Which of these is a valid string in Python?": "D",
    "What does list.append(x) do?": "C",
    "Which function can convert string to integer?": "C",
    "What is a correct syntax to create a dictionary?": "A",
    "What is output of print(\"5\" + \"6\")?": "B",
    "Which operator is used for floor division?": "C",
    "Which dees .sort resturns?": "B",
    "How do you start a for loop in Python?": "B",
    "How do you start an if condition?": "C",
    "What is the output of print(type([]))?": "A",
    "Which one creates a tuple?": "C",
    "What is None in Python?": "C",
    "What does input() return?": "B",
    "What does str(5) return?": "A",
    "What is set in Python?": "A",
    "What will range(5) return?": "B",
    "What is output: print(bool(1))?": "B",
    "What will this code do: x = [1,2]; x.append([3,4])?": "B",
    "What is slicing in Python?": "B",
    "Which built-in function returns the type of variable?": "C",
    "What is output: bool([])?": "B",
    "Which of the following are valid Python data types?": "D",
    "Which of these is a correct Python comment?": "B",
    "What is the output of print(len('Python'))?": "C",
    "What is the output of print(5 > 3 and 2 < 1)?": "B" ,
     "If you want to print values of dictinary what will you write inside print()?" : "D",
       }




color = ('#00b0f0' , '#92D050' , '#ffc000' , '#A64DFF')
questions_list = list(questions)
choices = (('//' ,'/**/ ','#','""'), 
    ('j' , 'a' , 'm' , 'n'), 
    ('1variable' , 'variable_name' ,'variable-name' , 'var@name') ,
    ('break' , 'over' , 'exit' , 'end'), 
    ('6', '8', '9', '5'),
    ('str', 'int', 'bool', 'float'),
    ('tuple', 'string', 'list', 'int'),
    ('False', 'True', 'Error', 'None'),
    ('Returns the number of lines', 'Returns length', 'Measures size in MB', 'Finds errors'),
    ('"Hello"', "'Hello'", '"""Hello"""', 'All of the above'),
    ('Deletes x', 'Replaces list with x', 'Adds x to the end', 'Adds x to the beginning'),
    ('string()', 'str()', 'int()', 'convert()'),
    ('dict = {"name": "Ali"}', 'dict = ["name": "Ali"]', 'dict = ("name": "Ali")', 'dict = {"name", "Ali"}'),
    ('11', '56', 'Error', 'None'),
    ('/', '%', '//', '**'),
    ('unsorted list', 'None', '""', 'sorted list'),
    ('for(i=0;i<5;i++)', 'for x in range(5):', 'foreach x in 5', 'loop x from 1 to 5'),
    ('if x == 1', 'if (x == 1)', 'if x == 1:', 'if x = 1'),
    ('list', 'tuple', 'dict', 'set'),
    ('[1, 2]', '{1, 2}', '(1, 2)', '<1, 2>'),
    ('0', 'Empty string', 'Null object', 'False'),
    ('integer', 'string', 'float', 'list'),
    ('"5"', '5', '0', 'Error'),
    ('Unordered unique collection', 'Ordered duplicates', 'List', 'None'),
    ('[1,2,3,4,5]', '[0,1,2,3,4]', '[0,1,2,3,4,5]', 'Error'),
    ('False', 'True', '0', 'Error'),
    ('Adds 3 and 4 separately', 'Adds [3, 4] as list', 'Replaces x', 'Error'),
    ('Cutting variables', 'Dividing strings/lists', 'Memory allocation', 'None'),
    ('var()', 'typeof()', 'type()', 'datatype()'),
    ('True', 'False', 'Error', 'None'),
    ('int', 'float', 'list', 'All of the above'),
    ('// Hello', '# Hello', '<!-- Hello -->', "'Hello"),
    (' 5', '7', '6', 'Error'),
    ('True', 'False', 'None', 'Error'),
    ('values' , 'value' , 'value()' , 'values()'))


guesses = ['?' for i in range(len(questions))]
symbol = ('A' , 'B' , 'C'  ,'D')
symbol_var = [None for i in range(len(symbol))]
num = 0




def next_fun(n):
    
    global num
    global symbol

   
    num += (n)

    if (len(questions)  == num and n == 1):
        response = messagebox.askyesno("Confirm Action", "this is last mcqs after that you will get result")

        

        if response:
             for widget in root.winfo_children():
                widget.destroy()

             making_result()

        else: 
            messagebox.showinfo("Action Cancelled", "You chose not to proceed.")
            num -= 1
        
        
    
    else:
        if num == 0:
            
            prev_btn.config(state=tk.DISABLED)

        elif prev_btn['state'] != 'normal':
            prev_btn.config(state = tk.NORMAL) 






        for symb in symbol_var:
            symb.config(background = BG_COLOR)
            for widget in  symb.winfo_children():
                    widget.config(background = BG_COLOR)   

        changing_questions()

        for ind,cho in enumerate(symbol):
            if cho == guesses[num]:
                symbol_var[ind].config(background = SELECTED_BG)
                for widget in symbol_var[ind].winfo_children():
                    widget.config(background = SELECTED_BG) 
    
                break


    
       
               
def saving_data():
    
    nu = 0 

    for widget in  options_frame.winfo_children():
        symbol_var[nu] = widget
        nu += 1
     

# Theme Colors

TEXT_COLOR = "yellow"
BOX_BG = "#2A2A3D"
HIGHLIGHT = "yellow"

# Fonts
title_font = ("Helvetica", 24, "bold")
label_font = ("Helvetica", 16, "bold")
value_font = ("Helvetica", 18, "bold")



# Color Settings
COLOR_MAP = {
    "A": "#00B0F0",  # Blue
    "B": "#92D050",  # Green
    "C": "#FFC000",  # Yellow
    "D": "#A64DFF",  # Violet
}
SELECTED_BG = "#31354A"   # Unified highlight color
BG_COLOR = "#1E1E2F"      # Background color
TEXT_COLOR = "#FFFFFF"    # Font color

# Main window
root = tk.Tk()
root.title("Quiz App")
root.geometry("900x700")
root.configure(bg=BG_COLOR)




# Fonts
title_font = ("Helvetica", 24, "bold")
question_font = ("Helvetica", 16, "bold")
option_font = ("Helvetica", 14, "bold")
button_font = ("Helvetica", 12, "bold")

# Title
title_label = tk.Label(root, text="PYTHON QUIZ", font=title_font, bg=BG_COLOR, fg=TEXT_COLOR)
title_label.pack(pady=(20, 10))

# Question Frame
question_frame = tk.Frame(root, bg="#2A2A3D", padx=30, pady=20)
question_frame.pack(padx=20, pady=10, fill="x")

question_label = tk.Label(
    question_frame,
    text=f'1.  {questions_list[0]}',
    font=question_font,
    bg="#2A2A3D",
    fg=TEXT_COLOR
)
question_label.pack(anchor="w")

# Store references to update selection
option_rows = {}
selected_option = None

# Functions
def select_option(letter):
    global selected_option
    selected_option = letter
    update_selection()

def update_selection():
    for key, row in option_rows.items():
        bg = SELECTED_BG if key == selected_option else BG_COLOR
        row.configure(bg=bg)
        row.canvas.configure(bg=bg)
        row.option_button.configure(bg=bg)


    
    guesses[num] = selected_option


# Create option row
def create_option_row(parent, letter, text, color):
    row = tk.Frame(parent, bg=BG_COLOR)
    row.pack(fill="x", pady=10)

    canvas = tk.Canvas(row, width=40, height=40, highlightthickness=0, bg=BG_COLOR)
    canvas.pack(side="left")
    canvas.create_oval(0, 0, 40, 40, fill=color, outline="")
    canvas.create_text(20, 20, text=letter, fill="white", font=option_font)



    btn = tk.Button(
        row,
        text=text,
        font=option_font,
        command=lambda l=letter: select_option(l),
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        activebackground=SELECTED_BG,
        activeforeground=TEXT_COLOR,
        relief="flat",
        anchor="w",
        padx=20,
        pady=10,
        width=40
    )
    btn.pack(side="left", fill="x", expand=True)

    # Store references
    row.canvas = canvas


    row.option_button = btn
    option_rows[letter] = row
    


# Option Frame
options_frame = tk.Frame(root, bg=BG_COLOR)
options_frame.pack(pady=20, fill="x", padx=40)

# Create options A-D



def changing_questions():
    global num
    question_label.config(text = f'{num + 1}.  {questions_list[num]}')
    for i,symbol in enumerate(symbol_var):
            for widget in  symbol.winfo_children():
                if type(widget) == tk.Button:
                   widget.config(text = choices[num][i])

                

   
    
    
create_option_row(options_frame, "A", choices[num][0] , COLOR_MAP["A"])
create_option_row(options_frame, "B", choices[num][1] , COLOR_MAP["B"])
create_option_row(options_frame, "C", choices[num][2] , COLOR_MAP["C"])
create_option_row(options_frame, "D", choices[num][3] , COLOR_MAP["D"])
saving_data()
        



# Navigation Buttons
nav_frame = tk.Frame(root, bg=BG_COLOR)
nav_frame.pack(pady=30)

prev_btn = tk.Button(
    nav_frame, text="Previous", font=button_font,
    bg="#444", fg=TEXT_COLOR, padx=20, pady=10,
    relief="flat", activebackground="#666", activeforeground="white",command = lambda: next_fun(-1) , state= tk.DISABLED
)
prev_btn.pack(side="left", padx=20)

next_btn = tk.Button(
    nav_frame, text="Next", font=button_font,
    bg="#00B0F0", fg="white", padx=20, pady=10,
    relief="flat", activebackground="#0090D0", activeforeground="white",
    command = lambda: next_fun(1)
)
next_btn.pack(side="left", padx=20)














# Reusable block to create labeled result rows
def create_result_row(parent, label_text, value_text):
    frame = tk.Frame(parent, bg=BOX_BG, padx=20, pady=20)
    frame.pack(pady=10, padx=30, fill="x")

    label = tk.Label(frame, text=label_text, font=label_font, bg=BOX_BG, fg=TEXT_COLOR)
    label.pack(anchor="w")

    value = tk.Label(frame, text=value_text, font=value_font, bg=BOX_BG, fg=HIGHLIGHT)
    value.pack(anchor="w")







# Main results area

def making_result():
    marks = 0
   
    answers = list(questions.values())
    total_marks = len(questions)
    
    for i,ans in enumerate(answers):
        if ans == guesses[i]:
            marks += 1


    percentage = (marks / total_marks) * 100

    # Title
    title_label = tk.Label(root, text="RESULT SUMMARY", font=title_font, bg=BG_COLOR, fg=TEXT_COLOR)
    title_label.pack(pady=(30, 20))


   


    create_result_row(root, "Marks Obtained:", f'{marks}/{total_marks}')
    create_result_row(root, "Percentage:", f'{percentage}%')
    
    create_result_row(root, "Answers:" , ' '.join(answers))
    create_result_row(root, "Guesses" , ' '.join(guesses))

    


# Run the app
root.mainloop()