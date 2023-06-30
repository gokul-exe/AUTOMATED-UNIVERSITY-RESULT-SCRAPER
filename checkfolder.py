import os
def main():
    folder_check()
def folder_check(roll_number):
# Specify the output folder path
    output_folder = 'output\\'+roll_number

    # Check if the folder exists
    if not os.path.exists(output_folder):
        # Create the folder if it doesn't exist
        os.makedirs(output_folder)
        return output_folder
    else:
        return output_folder
if __name__=="__main__":
    main()