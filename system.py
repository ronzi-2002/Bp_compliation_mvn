import threading
import subprocess



def run_BPProgram(file_name, compile = True, gui_file_path = None):
        #java -jar .\target\DesignlessProgrammin.jar
        import os
        if compile:
            #first check if you have maven installed
            if os.system("mvn package -P\"uber-jar\" -f src/main_client_server_java/pom.xml") == 0:
                print("Compiled successfully")
            else:
                print("Error in compiling the Java code")
                return
        
        process = subprocess.Popen(f"java -jar src\\main_client_server_java\\target\\DesignlessProgramming-0.6-DEV.uber.jar -f {file_name} ", shell=True)

def main():
    run_BPProgram(file_name="smartHouse_Paper.txt")
    print("Done")

if __name__ == "__main__":
    main()


