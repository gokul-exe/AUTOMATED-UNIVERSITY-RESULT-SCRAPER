from checkfolder import folder_check
from msedge.selenium_tools import EdgeOptions, Edge


def main():
    welcome()
    driver_setup()
    results()
def driver_setup():
        #Set the path to the Edge webdriver executable
        webdriver_path = r'webdriver\msedgedriver.exe'
        #Configure EdgeOptions
        options = EdgeOptions()
        options.use_chromium = True
        #Open the browser in maximized mode
        options.add_argument('--headless')  
        options.add_argument('--window-size=1920,1080')        
        global driver
        driver = Edge(executable_path=webdriver_path, options=options)      
def results():
        number_of_students=int(input("ENTER THE NUMBER OF STUDENTS YOU WANNA CHECK RESULT: "))
        start_str=input("ENTER THE STARTING ROLL NUMBER: ")[-3::] 
        start=(int(start_str))               
        #In my case the pondicherry university has a combination of string and int so making string as constant, im iterting through the last integers
        #actual roll number in my college is 19TH0400(change it accordingly)
        print("wait ....few min....Program working!")
        for _ in range(0,number_of_students):               
            rol_no = "19TH0"+str(start)
            # Open the desired webpage
            url = 'http://exam.pondiuni.edu.in/results/result.php?r='+rol_no+'&e=G'#(change url accordingly)
            driver.get(url)  
            result_error_div = driver.find_element_by_id("result_error_div")
            if "Invalid Register number / No Results found" in result_error_div.text:
                     print("Roll number", rol_no, "does not exist.")
            else:
                    # Take a screenshot of the webpage
                    path = folder_check(rol_no)
                    screenshot_file = path + '\\' + rol_no + '.png'
                    driver.save_screenshot(screenshot_file)
                    print("Full-screen screenshot saved as", screenshot_file)
            start+=1    
        driver.quit()
def welcome():
       print("""   
       
██████╗ ███████╗███████╗██╗   ██╗██╗  ████████╗███████╗    ███████╗ ██████╗██████╗  █████╗ ██████╗ ██████╗ ███████╗██████╗ 
██╔══██╗██╔════╝██╔════╝██║   ██║██║  ╚══██╔══╝██╔════╝    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██████╔╝█████╗  ███████╗██║   ██║██║     ██║   ███████╗    ███████╗██║     ██████╔╝███████║██████╔╝██████╔╝█████╗  ██████╔╝
██╔══██╗██╔══╝  ╚════██║██║   ██║██║     ██║   ╚════██║    ╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔═══╝ ██╔══╝  ██╔══██╗
██║  ██║███████╗███████║╚██████╔╝███████╗██║   ███████║    ███████║╚██████╗██║  ██║██║  ██║██║     ██║     ███████╗██║  ██║
╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝   ╚══════╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═╝                                                                                                                           
                                                                                                                           """)


main()
