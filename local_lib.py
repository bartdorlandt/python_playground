import os


def read_from_file(filename: str):
    with open(filename) as f:
        return f.read()


def save_file(data: object, filename: str) -> None:
    """Save data to a file.

    filename is expected to be a string.
    the file is stored in the root of this project/output.

    Args:
        data: the data to be stored
        filename: the filename to be used
    """
    output_file = os.path.abspath(filename)

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w") as f:
        f.write(str(data))
    # print(f"Successfully written to: '{output_file}'")
