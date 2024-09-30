import os


def txt_to_bin(text):
    return " ".join(format(byte, "08b") for byte in text.encode("utf-8"))


def bin_to_txt(binary):
    binary_values = binary.split()
    byte_array = bytearray(int(b, 2) for b in binary_values)
    return byte_array.decode("utf-8")


def rename_file(path, new_extension):
    base = os.path.splitext(path)[0]
    new_path = f"{base}{new_extension}"
    os.rename(path, new_path)
    return new_path


def process_file(path: str):
    path = path.removeprefix('"').removesuffix('"')
    file_extension = os.path.splitext(path)[1]

    if file_extension == ".txt":
        with open(path, "r+", encoding="utf-8") as f:
            data = f.readlines()
            f.seek(0)
            f.truncate()
            for line in data:
                f.write(txt_to_bin(line.strip()) + "\n")
        rename_file(path, ".bin")
        input("Sucessfully converted to bin, press enter to exit ....")

    elif file_extension == ".bin":
        with open(path, "r+", encoding="utf-8") as f:
            data = f.readlines()
            f.seek(0)
            f.truncate()
            for line in data:
                f.write(bin_to_txt(line.strip()) + "\n")
        rename_file(path, ".txt")
        input("Sucessfully converted to txt, press enter to exit ....")


txt_or_bin = input("Enter B to [Bin -> Txt], or enter T to [Txt -> Bin] : ")[0].lower()
process_file(
    input(f"Drag n Drop the {".bin" if txt_or_bin == 'b' else ".txt"} file : ")
)
