## 🎓 Automated University Result Scraper 🤖

This Python script automates the process of fetching and capturing results from a university result website. It uses Selenium WebDriver with Microsoft Edge browser to perform the automation. The script is designed to visit the result page for multiple roll numbers, capture full-screen screenshots, and save them in respective folders.

# 📋 Prerequisites

To run this script, you need the following:

- Python 3.x
- Selenium WebDriver
- Microsoft Edge browser
- Edge WebDriver (msedgedriver)

## ⚙️ Installation

1. Clone the repository or download the script files.

2. Install the required Python packages using pip:

   ```shell
   pip install -r requirements.txt

1.Make sure you have the Microsoft Edge browser installed on your system.

2.Download the appropriate version of the Edge WebDriver (msedgedriver) from the official Microsoft WebDriver page: Microsoft WebDriver

3.Place the downloaded msedgedriver.exe file in the "webdriver" folder of the project.

## ▶️ Usage
1.Open a terminal or command prompt.

2.Navigate to the project directory.

3.Run the script using the following command:

  ```shell
   python main.py
  ```

4.Follow the instructions displayed on the terminal to provide the number of students and the starting roll number.

5.The script will visit the result page for each roll number, capture full-screen screenshots, and save them in respective folders.

6.If a roll number does not exist or no results are found, a message will be displayed indicating the same.

## 📂 Folder Structure
1.The script will create a folder structure to organize the captured screenshots as follows:

2.Each student's results will be saved in a separate folder based on their roll number

3.The folders will be created in the same directory as the script.
# 🤝 Contributing
Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request.



