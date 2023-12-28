import re
re.split(r"[.?!]", "One sentence. Another one? And teh last one!")

re.split(r"([.?!])", "One sentence. Another one? And teh last one!")

re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received and email for go_nuts95@my.example.com")

re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")