from scrollnote import ScrollNote
scroll = ScrollNote("")
scroll.load()

print("==== Welcome to ScrollNote! ====")

if scroll.content == "":
    print("You have no content in your scroll")
else:
    print(f"Today's Content:\n{scroll.content}")


ask_edit = input("Do you want to edit today's note?\n> edit / exit ").lower()

if ask_edit == "exit":
    print("Okay, see you tomorrow")
elif ask_edit == "edit":
    print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.\n")
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)
    scroll.content = ("\n").join(contents)
    scroll.save()
    print("Entry saved. See you tomorrow.")