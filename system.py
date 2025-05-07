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

def generate_graph(file_name):
        import os

        fileDir = ""

        # Compile the Java code
        if os.system("mvn package -P\"uber-jar\" -f src/main_client_server_java/pomGraph.xml") == 0:
        # if True:  
            # Run the jar and capture output
            process = subprocess.Popen(
                f"java -jar src\\main_client_server_java\\target\\DesignlessProgramming-0.6-DEV.uber.jar \"{file_name}\" HandleExternalEvents.js",
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True
            )

            # Store the output and error
            stdout, stderr = process.communicate()
            if process.returncode == 0:
                print("Output:")
                print(stdout)  # Or store it in a variable for further use
                ##one of the line in the output is // Exporting space to: <fileDir>
                ##we need to extract the fileDir
                
                for line in stdout.split("\n"):
                    if "// Exporting space to: " in line:
                        fileDir = line.split("// Exporting space to: ")[1]
                        break
            else:
                print("Error:")
                print(stderr)
        else:
            print("Error in compiling the Java code")
            return
        if fileDir == "":
            print("Error in exporting the graph")
            return
            
        export_file_name = file_name + "+HandleExternalEvents.js.dot"
        full_export_file_path = fileDir+"/" + export_file_name 
        print (f"Graph exported to {full_export_file_path}")

        #open the graph in the browser
        import urllib.parse

        graphDot = open(full_export_file_path, "r").read()
        encoded_path = urllib.parse.quote(graphDot)
        graphUrl = f"https://dreampuf.github.io/GraphvizOnline/#{encoded_path}"
        print("If the browser does not open, please open the following link in the browser: ", graphUrl)
        import webbrowser
        webbrowser.open(graphUrl)
        
def main():
    # run_BPProgram(file_name="smartHouse_Paper.js")
    generate_graph(file_name="smartHouse_Paper.js")
    print("Done")

if __name__ == "__main__":
    main()


