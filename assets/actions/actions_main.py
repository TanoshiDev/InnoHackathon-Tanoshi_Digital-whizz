import flet as ft

def refresh(*args) -> list[ft.Text]:
    posts = ["Hello!", "Good Morning"]
    authors = ["USERNAME1", "USerNAme2"]
    
    callback = [ft.Text(f"{authors[i]}\n{posts[i]}") for i in range(len(posts))]
    print(callback)
    return callback    