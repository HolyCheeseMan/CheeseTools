import os
import customtkinter
import requests

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x250")
root.minsize(500, 250)
root.resizable(False, False)
root.title("Simple Installer")

try:
    username = os.getlogin()
except Exception as e:
    print(f"Error getting username: {e}")
    username = "DefaultUser"

def download():
    url = url_input.get()
    destination_folder = fr"C:\Users\{username}\Downloads"
    print(f"\nDownloading from URL {url}")
    response = requests.get(url)
    filename = os.path.join(destination_folder, url.split("/")[-1])
    with open(filename, "wb") as file:
        file.write(response.content)
    print(f"Downloaded {filename}")
    os.startfile(destination_folder)
    root.quit()

label = customtkinter.CTkLabel(master=root, text="Simple Installer", font=("Roboto", 35))
label.pack(padx=5, pady=10)

label_raw_url = customtkinter.CTkLabel(master=root, text="Input Raw URL", font=("Roboto", 15))
label_raw_url.pack(padx=5, pady=5)

url_input = customtkinter.CTkEntry(master=root, width=450, font=("Roboto", 20))
url_input.pack(padx=5, pady=5)

download_button = customtkinter.CTkButton(master=root, text="Download", font=("Roboto", 25), command=download)
download_button.pack(padx=5, pady=25)

root.mainloop()