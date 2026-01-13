# import tkinter as tk
# from tkinter import ttk, messagebox

# # --- Window Creation Function ---

# def open_country_window(country):
#     """
#     Creates and displays a new Toplevel window for the selected country.
#     This window will serve as the container for specific human rights content.
#     """
#     # Create the new top-level window
#     new_window = tk.Toplevel()
#     new_window.title(f"Human Rights in {country}")
#     new_window.geometry("500x350")
#     new_window.resizable(True, True)
#     new_window.attributes('-topmost', True) # Keep the new window on top temporarily

#     # Styling and Layout
#     main_frame = ttk.Frame(new_window, padding="20 20 20 20")
#     main_frame.pack(expand=True, fill='both')

#     # Title Label for the new screen
#     title = ttk.Label(
#         main_frame,
#         text=f"{country}: Human Rights Context",
#         font=('Inter', 18, 'bold'),
#         foreground='#2c3e50'
#     )
#     title.pack(pady=(0, 15))

#     # Placeholder/Instruction Text
#     # You can replace this with your actual detailed content (text areas, lists, etc.)
#     context_text = f"Welcome to the dedicated page for human rights information concerning {country}. "
#     context_text += "You can now implement the logic to load and display relevant data, documents, or statistics here. "

#     if country == "South Africa":
#         context_text += "Focus areas often include socio-economic rights, equality, and post-apartheid justice initiatives."
#     elif country == "Bangladesh":
#         context_text += "Focus areas often include labor rights, freedom of speech, and issues related to climate change displacement."

#     content_label = ttk.Label(
#         main_frame,
#         text=context_text,
#         wraplength=450,
#         justify=tk.LEFT,
#         font=('Inter', 11)
#     )
#     content_label.pack(fill='x', pady=10)

#     # Close Button for the new screen
#     close_btn = ttk.Button(
#         main_frame,
#         text="Close Window",
#         command=new_window.destroy,
#         style="Accent.TButton"
#     )
#     close_btn.pack(pady=20)


# # --- Main Application Setup ---

# root = tk.Tk()
# root.title("Global Human Rights Index")
# root.geometry("350x180")
# root.resizable(False, False)

# # Apply basic styling for better appearance
# style = ttk.Style()
# style.theme_use('clam')
# style.configure('TFrame', background='#ecf0f1')
# style.configure('TLabel', background='#ecf0f1', padding=5)
# style.configure('Accent.TButton', font=('Inter', 10, 'bold'), background='#3498db', foreground='white')
# style.map('Accent.TButton', background=[('active', '#2980b9')])


# # Main Content Frame
# app_frame = ttk.Frame(root, padding="15 15 15 15")
# app_frame.pack(expand=True, fill='both')

# # 1. Main Title
# title_label = ttk.Label(
#     app_frame,
#     text="Human Rights Focus",
#     font=('Inter', 18, 'bold'),
#     foreground='#2c3e50'
# )
# title_label.pack(pady=(0, 15))

# # 2. "Countries:" Label
# countries_label = ttk.Label(
#     app_frame,
#     text="Countries:",
#     font=('Inter', 12, 'italic')
# )
# countries_label.pack(pady=(0, 5))

# # 3. Button Frame
# button_frame = ttk.Frame(app_frame)
# button_frame.pack(pady=5)

# # 4. South Africa Button (functional)
# south_africa_button = ttk.Button(
#     button_frame,
#     text="South Africa",
#     command=lambda: open_country_window("South Africa"), # Calls the new window function
#     style="Accent.TButton"
# )
# south_africa_button.pack(side=tk.LEFT, padx=10)

# # 5. Bangladesh Button (functional)
# bangladesh_button = ttk.Button(
#     button_frame,
#     text="Bangladesh",
#     command=lambda: open_country_window("Bangladesh"), # Calls the new window function
#     style="Accent.TButton"
# )
# bangladesh_button.pack(side=tk.LEFT, padx=10)

# # Start the main event loop
# root.mainloop()


############## Version 2 ##############

# import tkinter as tk
# from tkinter import ttk, messagebox
# import matplotlib
# matplotlib.use('TkAgg') # Use the Tkinter backend for Matplotlib
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from matplotlib.figure import Figure
# import numpy as np

# # --- Graph Generation Function ---

# def create_graph(frame, country):
#     """
#     Generates a sample Matplotlib graph and embeds it into the given Tkinter frame.
#     The data changes based on the country.
#     """
#     # 1. Setup the Figure
#     fig = Figure(figsize=(7, 4), dpi=100, facecolor='#ecf0f1')
#     ax = fig.add_subplot(111)
    
#     # 2. Define Data based on Country
#     if country == "South Africa":
#         categories = ['Equality', 'Housing', 'Labor', 'Justice', 'Security']
#         complaints = [85, 40, 65, 78, 55]
#         colors = ['#e74c3c', '#3498db', '#f1c40f', '#2ecc71', '#9b59b6']
#         title_text = "Human Rights Scores by Area (South Africa)"
#         y_label = "Normalized Score (0-100)"

#     elif country == "Bangladesh":
#         categories = ['Labor Rights', 'Free Speech', 'Climate Impact', 'Safety', 'Women\'s Rights']
#         complaints = [92, 55, 70, 60, 75]
#         colors = ['#1abc9c', '#34495e', '#f39c12', '#c0392b', '#e67e22']
#         title_text = "Human Rights Complaints Volume (Bangladesh)"
#         y_label = "Complaint Index (Normalized)"

#     # 3. Create the Plot (Bar Chart)
#     ax.bar(categories, complaints, color=colors)
    
#     # 4. Set Plot Aesthetics
#     ax.set_title(title_text, fontsize=12, fontweight='bold')
#     ax.set_ylabel(y_label, fontsize=10)
#     ax.tick_params(axis='x', rotation=15, labelsize=9)
#     ax.tick_params(axis='y', labelsize=9)
#     ax.grid(axis='y', linestyle='--', alpha=0.7)
    
#     # 5. Embed the graph in the Tkinter frame
#     canvas = FigureCanvasTkAgg(fig, master=frame)
#     canvas.draw()
    
#     # 6. Get the Tkinter widget and pack it
#     canvas_widget = canvas.get_tk_widget()
#     canvas_widget.pack(fill=tk.BOTH, expand=True, pady=(20, 10), padx=5)


# # --- Window Creation Function ---

# def open_country_window(country):
#     """
#     Creates and displays a new Toplevel window for the selected country,
#     now including the Matplotlib graph.
#     """
#     # Create the new top-level window
#     new_window = tk.Toplevel()
#     new_window.title(f"Human Rights in {country}")
#     # Increased size to accommodate the graph
#     new_window.geometry("800x600") 
#     new_window.resizable(True, True)
#     new_window.attributes('-topmost', True) 

#     # Styling and Layout Frame
#     main_frame = ttk.Frame(new_window, padding="20 20 20 20")
#     main_frame.pack(expand=True, fill='both')

#     # Title Label for the new screen
#     title = ttk.Label(
#         main_frame,
#         text=f"{country}: Human Rights Context",
#         font=('Inter', 18, 'bold'),
#         foreground='#2c3e50'
#     )
#     title.pack(pady=(0, 15))

#     # Placeholder/Instruction Text
#     context_text = f"Welcome to the dedicated page for human rights information concerning {country}. "
#     context_text += "Below is a sample visualization of key human rights metrics. "

#     if country == "South Africa":
#         context_text += "South Africa, as its name suggests, is a large country that lies in southern Africa. Over time, South Africa has been facing a couple of problems relating to human rights, such as: Inequality: Africa used to suffer from indequality and unfair discrimination between physical appearances; in the past, the fair-toned people were considered superior to the those with darker shades, causing conflict with raital comments along with physical activity. Around the 1950s, many people like Mahatma Ghandi and Martin Lurther King took a determined step ahead, and helped to restore equality to the country. Thanks to such heroes, today, South Africa does not host much raital discrimination, but some still persists due to corruption and other unsolved matters. Housing: South Africa has been facing a housing crisis for many years now. Many people are homeless and live in shanty towns, which are not safe and lack basic amenities. The government has been trying to address this issue by building more affordable housing, but the demand still exceeds the supply. Labor Rights: South Africa has a high unemployment rate, which has led to exploitation of workers in some industries. Many workers do not receive fair wages or benefits, and some are subjected to unsafe working conditions. The government has implemented labor laws to protect workers' rights, but enforcement remains a challenge. Justice: South Africa's justice system has faced criticism for being slow and inefficient. Many cases take years to resolve, leading to frustration among victims and their families. Efforts are being made to improve the efficiency of the justice system, but progress is slow. Security: South Africa has a high crime rate, which affects the safety and security of its citizens. The government has implemented various measures to combat crime, but it remains a significant concern for many South Africans. Moreover, many crimes occur daily in South Africa, putting innocent residents and tourists at risk. Everyday, Africa is working towards solving these problems, along with the help of international organizations such as United Nations and human rights activists. Hopefully, soon, we will see Africa rise above these challenges and become a beacon of hope for human rights worldwide."
#     elif country == "Bangladesh":
#         context_text += "Bangladesh is a country that lies in the western area in what is known as the Indian Subcontinent. It was formed on March 16th 1971, making it a relatively new nation compared to other countries. Bangladesh current state has improved from the passed signifacntly, initially, there used to be mass discrimination and civil wars between two religions at the time (Hindu & Muslim), they were unable to live in harmony at the time, leading to the suffering of a great number of people. Sometimes, they were judged by religion, whether it was in a court, or if it was who got the rights in the hospital. Today, thankfully, these probelms were mostly resolved, reducing the death toll and making it a slightly better place. Unfortunately, few problems still persist today, such as: Labor Rights: Workers face signifantl challanges, which include minimal wages, low saftey standards and resitriction of freedom on occasions, bargaining and speech. They are sometimes iltreated based on their cast (lower paying job, worse treated and lower respect). Sometimes, many forget that humans are the same type at the end of the day, and each shoud be treated fairly, specially if they are innocent and have commited no sins or crimes. In addition to that, rate of child maridge and child labour still persist; children are being treated unfairly and are forced to perform things against their will. Last but not least, Bangladesh residents also suffer from lack of protection, where they are under the threat of illegal armed groups, thus, Bangladesh enforcments of law have to be stronger, along with their saftey mechnanisims such as police, military and secuirty to provide a safer nation to live in. They are making visible changes with help of the United Nations, recovering from their damage and making their country a better place.   ."

#     content_label = ttk.Label(
#         main_frame,
#         text=context_text,
#         wraplength=750, # Adjusted wraplength for wider window
#         justify=tk.LEFT,
#         font=('Inter', 11)
#     )
#     content_label.pack(fill='x', pady=(0, 15))
    
#     # ---------------------------
#     # Embed the Graph Here
#     # ---------------------------
#     create_graph(main_frame, country)


#     # Close Button for the new screen
#     close_btn = ttk.Button(
#         main_frame,
#         text="Close Window",
#         command=new_window.destroy,
#         style="Accent.TButton"
#     )
#     # Pack the close button at the bottom
#     close_btn.pack(pady=10)


# # --- Main Application Setup (Unchanged) ---

# root = tk.Tk()
# root.title("Global Human Rights Index")
# root.geometry("350x180")
# root.resizable(False, False)

# # Apply basic styling for better appearance
# style = ttk.Style()
# style.theme_use('clam')
# style.configure('TFrame', background='#ecf0f1')
# style.configure('TLabel', background='#ecf0f1', padding=5)
# style.configure('Accent.TButton', font=('Inter', 10, 'bold'), background='#3498db', foreground='white')
# style.map('Accent.TButton', background=[('active', '#2980b9')])


# # Main Content Frame
# app_frame = ttk.Frame(root, padding="15 15 15 15")
# app_frame.pack(expand=True, fill='both')

# # 1. Main Title
# title_label = ttk.Label(
#     app_frame,
#     text="Human Rights Focus",
#     font=('Inter', 18, 'bold'),
#     foreground='#2c3e50'
# )
# title_label.pack(pady=(0, 15))

# # 2. "Countries:" Label
# countries_label = ttk.Label(
#     app_frame,
#     text="Countries:",
#     font=('Inter', 12, 'italic')
# )
# countries_label.pack(pady=(0, 5))

# # 3. Button Frame
# button_frame = ttk.Frame(app_frame)
# button_frame.pack(pady=5)

# # 4. South Africa Button (functional)
# south_africa_button = ttk.Button(
#     button_frame,
#     text="South Africa",
#     command=lambda: open_country_window("South Africa"),
#     style="Accent.TButton"
# )
# south_africa_button.pack(side=tk.LEFT, padx=10)

# # 5. Bangladesh Button (functional)
# bangladesh_button = ttk.Button(
#     button_frame,
#     text="Bangladesh",
#     command=lambda: open_country_window("Bangladesh"),
#     style="Accent.TButton"
# )
# bangladesh_button.pack(side=tk.LEFT, padx=10)

# # Start the main event loop
# root.mainloop()
 
############### Version 3 ##############
import tkinter as tk
from tkinter import ttk, messagebox
# Import ScrolledText for large text blocks with a scrollbar
from tkinter.scrolledtext import ScrolledText 
import matplotlib
# Use the Tkinter backend for Matplotlib
matplotlib.use('TkAgg') 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

# ---- ---

def create_graph(frame, country):
    """
    Generates a sample Matplotlib graph and embeds it into the given Tkinter frame.
    The data changes based on the country.
    """
    # 1. -
    fig = Figure(figsize=(7, 4), dpi=100, facecolor='#ecf0f1')
    ax = fig.add_subplot(111)
    
    # 2. -
    if country == "South Africa":
        categories = ['Equality', 'Housing', 'Labor', 'Justice', 'Security']
        # -
        complaints = [85, 40, 65, 78, 55] 
        colors = ['#e74c3c', '#3498db', '#f1c40f', '#2ecc71', '#9b59b6']
        title_text = "Human Rights Scores by Area (South Africa)"
        y_label = "Normalized Score (0-100)"

    elif country == "Bangladesh":
        categories = ['Labor Rights', 'Free Speech', 'Climate Impact', 'Safety', 'Women\'s Rights']
        # -
        complaints = [92, 55, 70, 60, 75]
        colors = ['#1abc9c', '#34495e', '#f39c12', '#c0392b', '#e67e22']
        title_text = "Human Rights Complaints Volume (Bangladesh)"
        y_label = "Complaint Index (Normalized)"
    else:
        # -
        return 

    # -)
    ax.bar(categories, complaints, color=colors)
    
    # -
    ax.set_title(title_text, fontsize=12, fontweight='bold', color='#2c3e50')
    ax.set_ylabel(y_label, fontsize=10, color='#34495e')
    # -
    ax.tick_params(axis='x', rotation=15, labelsize=9, colors='#34495e') 
    ax.tick_params(axis='y', labelsize=9, colors='#34495e')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    # -
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    
    # 5. -
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    
    # 6. -
    canvas_widget = canvas.get_tk_widget()
    # -
    canvas_widget.pack(fill=tk.BOTH, expand=True, pady=(15, 5), padx=5)


# --- -n ---

def open_country_window(country):
    """
    Creates and displays a new Toplevel window for the selected country,
    now including the Matplotlib graph and a scrollable text area.
    """
    new_window = tk.Toplevel()
    new_window.title(f"Human Rights in {country}")
    # -
    new_window.geometry("800x650") 
    new_window.resizable(True, True)
    # -
    new_window.attributes('-topmost', True) 

    # -
    main_frame = ttk.Frame(new_window, padding="20 20 20 20", style='TFrame')
    main_frame.pack(expand=True, fill='both')

    # -
    title = ttk.Label(
        main_frame,
        text=f"🌍 {country}: Human Rights Overview",
        font=('Inter', 20, 'bold'),
        foreground='#2c3e50', # -
        style='TLabel'
    )
    title.pack(pady=(0, 15))

    # --- - ---
    # -
    context_text_area = ScrolledText(
        main_frame, 
        wrap=tk.WORD, 
        font=('Inter', 11),
        height=10, # -
        padx=10,
        pady=10,
        relief=tk.FLAT, # -
        bg='#f9f9f9' # -
    )
    context_text_area.pack(fill='x'r, pady=(0, 15))

    # -
    context_content = f"Welcome to the dedicated page for human rights information concerning **{country}**. Below you will find a detailed context and a visualization of key human rights metrics.\n\n"
    
    if country == "South Africa":
        # -
        context_content += (
            "**Context:** South Africa has made significant strides since the end of apartheid, but persistent human rights challenges remain.\n\n"
            "**Key Issues Include:**\n"
            "1.  **Socio-economic Inequality:** Deep-seated economic disparities often translate into unequal access to housing, healthcare, and quality education.\n"
            "2.  **Labor and Land Rights:** Disputes over land reform and workers' rights, especially in mining and agriculture, are ongoing areas of concern.\n"
            "3.  **Crime and Security:** High rates of violent crime and gender-based violence pose a constant threat, challenging citizen security and the effectiveness of the justice system.\n\n"
            "Ongoing efforts by the government and civil society aim to fully realize the constitutional promise of human dignity and equality for all citizens. \n \n "
            "Paragraph section: \n"
            "Over time, South Africa has been facing a couple of problems relating to human rights, such as: Inequality: Africa used to suffer from indequality and unfair discrimination between physical appearances; in the past, the fair-toned people were considered superior to the those with darker shades, causing conflict with raital comments along with physical activity. Around the 1950s, many people like Mahatma Ghandi and Martin Lurther King took a determined step ahead, and helped to restore equality to the country. Thanks to such heroes, today, South Africa does not host much raital discrimination, but some still persists due to corruption and other unsolved matters. Housing: South Africa has been facing a housing crisis for many years now. Many people are homeless and live in shanty towns, which are not safe and lack basic amenities. The government has been trying to address this issue by building more affordable housing, but the demand still exceeds the supply. Labor Rights: South Africa has a high unemployment rate, which has led to exploitation of workers in some industries. Many workers do not receive fair wages or benefits, and some are subjected to unsafe working conditions. The government has implemented labor laws to protect workers' rights, but enforcement remains a challenge. Justice: South Africa's justice system has faced criticism for being slow and inefficient. Many cases take years to resolve, leading to frustration among victims and their families. Efforts are being made to improve the efficiency of the justice system, but progress is slow. Security: South Africa has a high crime rate, which affects the safety and security of its citizens. The government has implemented various measures to combat crime, but it remains a significant concern for many South Africans. Moreover, many crimes occur daily in South Africa, putting innocent residents and tourists at risk. Everyday, Africa is working towards solving these problems, along with the help of international organizations such as United Nations and human rights activists. Hopefully, soon, we will see Africa rise above these challenges and become a beacon of hope for human rights worldwide. \n \n"
            "Graph caption & explanation: \n"
            "The bar chart below depicts the improvement levles of human rights across key areas in South Africa. The graph shows that South Africa faces significant challenges in equality and housing. The data underlines the need for continued reforms to address socio-economic disparities and enhance citizen security."
        )
    elif country == "Bangladesh":
        context_content += (
            "**Context:** Bangladesh has experienced rapid economic growth but faces complex human rights challenges related to industrialization and climate change.\n\n"
            "**Key Issues Include:**\n"
            "1.  **Labor Rights:** Poor working conditions, low wages, and restrictions on unionization are pervasive, particularly in the ready-made garment industry.\n"
            "2.  **Freedom of Expression:** Concerns persist regarding limitations on media freedom and the use of laws to stifle political dissent and public criticism.\n"
            "3.  **Climate Change Impact:** Environmental displacement is increasingly driving internal migration, leading to issues related to housing, resource access, and public safety.\n\n"
            "The nation is actively working with international partners to manage its growing economy while strengthening civil and political rights protections. \n \n"
            "Paragraph section: \n"
            "Bangladesh is a country that lies in the western area in what is known as the Indian Subcontinent. It was formed on March 16th 1971, making it a relatively new nation compared to other countries. Bangladesh current state has improved from the passed signifacntly, initially, there used to be mass discrimination and civil wars between two religions at the time (Hindu & Muslim), they were unable to live in harmony at the time, leading to the suffering of a great number of people. Sometimes, they were judged by religion, whether it was in a court, or if it was who got the rights in the hospital. Today, thankfully, these probelms were mostly resolved, reducing the death toll and making it a slightly better place. Unfortunately, few problems still persist today, such as: Labor Rights: Workers face signifantl challanges, which include minimal wages, low saftey standards and resitriction of freedom on occasions, bargaining and speech. They are sometimes iltreated based on their cast (lower paying job, worse treated and lower respect). Sometimes, many forget that humans are the same type at the end of the day, and each shoud be treated fairly, specially if they are innocent and have commited no sins or crimes. In addition to that, rate of child maridge and child labour still persist; children are being treated unfairly and are forced to perform things against their will. Last but not least, Bangladesh residents also suffer from lack of protection, where they are under the threat of illegal armed groups, thus, Bangladesh enforcments of law have to be stronger, along with their saftey mechnanisims such as police, military and secuirty to provide a safer nation to live in. They are making visible changes with help of the United Nations, recovering from their damage and making their country a better place. \n \n "
            "Graph caption & explanation: \n"
            "The bar chart below illustrates the mass volume of human rights complaints across key areas in Bangladesh, highlighting significant concerns in labor rights and freedom of speech. The data underscores and accentuates the urgent, indespensible need for reforms to ensure safer working conditions and greater protections for civil liberties."
        )

    # -
    context_text_area.insert(tk.END, context_content)
    # -
    context_text_area.config(state=tk.DISABLED)
    
    # ---------------------------
    # -
    # ---------------------------
    graph_frame = ttk.Frame(main_frame)
    graph_frame.pack(fill='both', expand=True)
    create_graph(graph_frame, country)


    # -
    close_btn = ttk.Button(
        main_frame,
        text="Close Window",
        command=new_window.destroy,
        style="Accent.TButton" # -
    )
    close_btn.pack(pady=10)
    
    # -
    new_window.after(500, lambda: new_window.attributes('-topmost', False))


# --- Main Application Setup ---

root = tk.Tk()
root.title("Global Human Rights Index Dashboard")
root.geometry("400x220") # -
root.resizable(False, False)

# -
style = ttk.Style()
style.theme_use('clam')
# -
style.configure('TFrame', background='#ecf0f1') # -
style.configure('TLabel', background='#ecf0f1', padding=5, font=('Inter', 11))
# -
style.configure('Title.TLabel', font=('Inter', 22, 'bold'), foreground='#2c3e50') 
# -
style.configure('Accent.TButton', 
    font=('Inter', 11, 'bold'), 
    background='#3498db', # -
    foreground='white',
    relief=tk.FLAT, # -
    padding=[10, 5]
)
# -
style.map('Accent.TButton', 
    background=[('active', '#2980b9')] # Slightly darker blue on hover
)


# -
app_frame = ttk.Frame(root, padding="20 20 20 20", style='TFrame')
app_frame.pack(expand=True, fill='both')

# 1. Main Title
title_label = ttk.Label(
    app_frame,
    text="Global Human Rights Focus",
    style='Title.TLabel'
)
title_label.pack(pady=(0, 20))

# 2. "Countries:" Label
countries_label = ttk.Label(
    app_frame,
    text="Select a Country - Anay Rustogi (codemaster.ar@gmail.com):",
    font=('Inter', 12, 'italic'),
    style='TLabel'
)
countries_label.pack(pady=(0, 10))

# 3. Button Frame
button_frame = ttk.Frame(app_frame, style='TFrame')
button_frame.pack(pady=5)

# 4. South Africa Button (functional)
south_africa_button = ttk.Button(
    button_frame,
    text="🇿🇦 South Africa",
    command=lambda: open_country_window("South Africa"),
    style="Accent.TButton"
)
south_africa_button.pack(side=tk.LEFT, padx=15)

# 5. Bangladesh Button (functional)
bangladesh_button = ttk.Button(
    button_frame,
    text="🇧🇩 Bangladesh",
    command=lambda: open_country_window("Bangladesh"),
    style="Accent.TButton"
)
bangladesh_button.pack(side=tk.LEFT, padx=15)

# Start the main event loop
root.mainloop()


#import react
# import tkinter as tk
# from tkinter import ttk, messagebox
# import matplotlib
# matplotlib.use('TkAgg') # Use the Tkinter backend for Matplotlib
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from matplotlib.figure import Figure
# import numpy as np
# # --- Graph Generation Function ---
# def create_graph(frame, country):
#     """
#     Generates a sample Matplotlib graph and embeds it into the given Tkinter frame.
#     The data changes based on the country.
#     """
#     # 1. Setup the Figure







 