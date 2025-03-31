import name
import alter

print(f"Der Standardalter ist : {alter.age}")


try:
    eingegebenes_alter = int(input("Bitte geben Sie Ihr Alter ein: "))
except ValueError:
    print("Ungültige Eingabe. Bitte eine Zahl für das Alter eingeben.")
    exit()

alter.pruefe_alter(eingegebenes_alter)
realname = name.frage_name()

print(f"Hallo, Mein name ist {realname} und ich bin {eingegebenes_alter} Jahre alt!")