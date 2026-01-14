import tkinter as tk

root = tk.Tk()
root.title("Human Rights")

# Main label
title_label = tk.Label(root, text="Human Rights", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Countries label
countries_label = tk.Label(root, text="Countries", font=("Arial", 12))
countries_label.pack(pady=5)

# Buttons for countries
btn_venezuela = tk.Button(root, text="Venezuela")
btn_venezuela.pack(pady=2)

def open_country_window(country_name):
    new_window = tk.Toplevel(root)
    new_window.title(f"Human Rights for {country_name}")
    label = tk.Label(new_window, text=f"Human Rights for {country_name}", font=("Arial", 14, "bold"))
    label.pack(padx=20, pady=20)

btn_southafrica = tk.Button(root, text="South Africa", command=lambda: open_country_window("South Africa"))
btn_venezuela.config(command=lambda: open_country_window("Venezuela"))

btn_pakistan = tk.Button(root, text="Pakistan")
btn_pakistan.config(command=lambda: open_country_window("Pakistan"))

btn_southafrica.pack(pady=2)
btn_pakistan.pack(pady=2)

root.mainloop()

# Human rights in Africa have been violated for decades, and they are making a positive change... Over the years, multiple rights have either been abused, violated or ignored. However, there has been a positive change in the way human rights are being treated in Africa. Many countries have made significant progress in improving the human rights situation, and there are now more opportunities for people to speak out against abuses and demand their rights. This positive change is a testament to the resilience and determination of the African people, who continue to fight for their rights and freedoms despite the challenges they face.
