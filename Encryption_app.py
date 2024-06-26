import os  # OS operations
from tkinter import *  # main UI
import pyautogui  # for ease of prompts and alerts


def openpastkeys():  # Open past keys files
    PastKeyFile = 'Past-keys.txt'  # init var to pastkey
    os.startfile(PastKeyFile)  # opens file on os dadwada


def DecryptStr(): #DecryptFunct (is activated upon press of 'Decrypt' button)
    Encrypted_Text = pyautogui.prompt(text="text to decrypt: ", title="Encrypt", default='')  # prompt for text to decrypt
    Encrypt_Key = pyautogui.prompt(text="key: ", title="Decrypt Key", default='')  # prompt for key
    Encrypt_Key = ''.join(sorted(set(Encrypt_Key), key=Encrypt_Key.index))  # removes duplicate letters
    if (len(Encrypt_Key) < 26) or (len(Encrypt_Key) > 26) or (" " in Encrypt_Key):  # checks for valid key (conditions are: not below or above 26, no spaces)
        pyautogui.alert(text="Invalid Key Entered!", title="INVALID KEY!", button="Ok") # alerts user to invalid key
        Encrypt_Key = "" # inits key to empty
        pass
    else:
        Encrypted_Text.lower()
        table = str.maketrans(Encrypt_Key, "abcdefghijklmnopqrstuvwxyz") #Generates Table
        Decrypted_Text = Encrypted_Text.translate(table) #init translated text to Decrypted Text Var
        Decrypted_Text_Output = open("Decrypted_Text_Output.txt", "w")  # opens file for writing
        Decrypted_Text_Output.seek(0)  # seeks to point at beginning of file
        Decrypted_Text_Output.truncate()  # clears file
        Decrypted_Text_Output.write(Decrypted_Text)  # writes newly encrypted text to output
        Decrypted_Text_Output.close()  # close file
        os.startfile("Decrypted_Text_Output.txt") #opens file on os with output
        g = open("Past-keys.txt", "a")  # opens file for append
        g.write(f"\n Decrypt Key: {Encrypt_Key}\n")  # appends decrypt key to history
        g.close()  # close file


def EncryptStr():
    Plain_text = pyautogui.prompt(text="text to encrypt: ", title="Encrypt", default='')  # prompt for Plain Text
    Encrypt_Key = pyautogui.prompt(text="key: ", title="Encrypt Key", default='')  # prompt for key
    Encrypt_Key = ''.join(sorted(set(Encrypt_Key), key=Encrypt_Key.index))  # removes duplicate letters
    if (len(Encrypt_Key) < 26) or (len(Encrypt_Key) > 26) or (
            " " in Encrypt_Key):  # checks for conditions (not above or below 26, no spaces)
        pyautogui.alert(text="Invalid Key Entered!", title="INVALID KEY!", button="Ok")  # Rejects Invalid key and alerts user
        Encrypt_Key = ""  # initialise key to empty str for reinput
        pass
    else:
        Plain_text.lower()
        table = str.maketrans("abcdefghijklmnopqrstuvwxyz", Encrypt_Key)  #generates table
        Newcrypted_Text = Plain_text.translate(table) #inits Newly encrypted text to translated message
        Encrypted_Text_Output = open("Encrypted_Text_Output.txt", "w")  # opens file for writing
        Encrypted_Text_Output.seek(0)  # seeks to point at beginning of file
        Encrypted_Text_Output.truncate()  # clears file
        Encrypted_Text_Output.write(Newcrypted_Text)  # writes newly encrypted text to output
        Encrypted_Text_Output.close()  # close file
        os.startfile("Encrypted_Text_Output.txt") #opens file on os
        j = open("Past-keys.txt", "a") #opens file to append mode
        j.write(f"\n Encrypt Key: {Encrypt_Key}") #appends key to key history
        j.close() #close file


# Main Script starts from here onwards

window = Tk()  # init instance of window
window.title("Encryption Project")
window.iconbitmap(default='icon.ico')
window.geometry("1700x1000")  # set geometry of window
window.configure(bg="black")  # change background of window to black
frame = Frame(window)  # inits frame
frame.configure(bg="black") #configure background to black
frame.pack()  # packs frame
frame2 = Frame(frame) #init frame 2 for container of buttons
frame2.pack(side=BOTTOM) #packs frame 2 to bottom

Instructions = StringVar()  # init instructions for user to a string var
Instructions.set("\n"
                 "\n"
                 "\nInstructions:\n Click on the Encrypt/Decrypt and then input the message needed to be "
                 "Encrypted/Decrypted respectively, then click 'ok' and "
                 "\nthen input the key that will be used Encrypt/Decrypt your message, then click 'ok' \n"
                 "\nThe key should be a string that is 26 alphanumeric characters long (no repeated characters "
                 "or spaces!)."
                 "\nThe message will be encrypted accordingly, 1st letter to A, 2nd letter to B and so on and so forth in alphabetical order.\n"
                 "\nYour Message will be returned accordingly in a text file that will be opened for you!"
                 "\nDon't lose your key or you won't be able to decrypt the message you encoded with that key!"
                 "\nAll Keys are saved to the Key history which can be accessed at any time by pressing the 'Key History' Button"
                 "\nHave fun!"
                 "\n"
                 "\n")  # set instructions for user

Label = Label(frame,textvariable=Instructions, fg="white", bg="black", font=("Calibre", 15))  # init label
Label.pack()  # packs label

PastkeysButton = Button(frame, text="Key History", fg="black", bg="#999999", width="50", height="5",font=("Consolas", 15), command=openpastkeys)
# init button to display past keys
PastkeysButton.pack(side=TOP)  # packs button to top

DecryptButton = Button(frame2, text="Decrypt", fg="red", bg="#999999", width="23", height="10", font=("Consolas", 16),
                       command=DecryptStr) # inits button to decrypt
DecryptButton.grid(row=1, column=1)  # packs button to left

EncryptButton = Button(frame2, text="Encrypt", fg="green", bg="#999999", width="23", height="10", font=("Consolas", 16),
                       command=EncryptStr) # inits button to encrypt
EncryptButton.grid(row=1, column=2)  # packs button to right

window.mainloop()
# listen for events, loop window
