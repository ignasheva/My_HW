def function_opens_a_file(file_path: str) -> bool:
    file = open(file_path)
    s = file.readline()
    try:
        item = int(s.strip())
    except ValueError:
        print("Could not convert data to an integer")
        return False
    else:
        return True if 1 <= item < 3 else False
    finally:
        file.close()
