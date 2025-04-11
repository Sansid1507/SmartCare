
def save_data(data):
    with open("data/logs/health_log.txt", "a") as file:
        file.write(str(data) + "\n")
