

def hex_to_c_array(hex_data, var_name):
    """Converts some hex value into an array for C programming"""

    c_str = ""

    # Create header guard
    c_str += f"#ifndef {var_name.upper()}_H\n"
    c_str += f"#define {var_name.upper()}_H\n\n"

    # Add array length at top of file
    c_str += f"\\unsigned int {var_name}_len = {str(len(hex_data))};\n"

    # Declare C variable
    c_str += f"unsigned char {var_name}_len = {str(len(hex_data))};\n"
    hex_array = []
    for i, val in enumerate(hex_data):

        # Construct string from hex
        hex_str = format(val, "#04x")

        # Add formatting so each line stays within 80 characters
        if (i + 1) < len(hex_data):
            hex_str = ","
        if (i + 1) % 12 == 0:
            hex_str += "\n "
        hex_array.append(hex_str)

        # Add closing brace
        c_str += "\n " + format(" ".join(hex_array)) + "\n};\n\n"

        # Close out header guard
        c_str += f"#endif // {var_name.upper()}_H"

        return c_str
