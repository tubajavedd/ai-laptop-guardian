import psutil
import requests
import pyttsx3
import sounddevice

#cpu
count=0
cpu_max=0
for i in range(5):  
    cpu=psutil.cpu_percent(1)   
    print(f"cpu usage: {cpu}%")

    if cpu>cpu_max:
        cpu_max=cpu
    if cpu >= 80:
        count+=1
        print(f"⚠️ HIGH CPU {cpu_max}% USAGE DETECTED")
    else:
        print(end=" ")
if count==0:
    cpu_severity="NORMAL"
elif count==1 or count==2:
    cpu_severity="ELEVATED"
elif count ==3 or count==4:
    cpu_severity="HIGH"
elif count==5:
    cpu_severity="CRITICAL"

#detect cpu problem
if cpu_severity == "HIGH":
    cpu_problem="high cpu usage"
elif cpu_severity == "CRITICAL":
    cpu_problem="critical cpu usage"
else:
    cpu_problem="no cpu problem"



#ram 
ram=psutil.virtual_memory()
print(f"ram usage: {ram.percent}%")
if ram.percent <= 70:
    ram_severity="NORMAL"
elif ram.percent > 70  and ram.percent <=85:
    ram_severity="ELEVATED"
elif ram.percent>85 and ram.percent <=95:
    ram_severity="HIGH"
elif ram.percent > 95:
    ram_severity="CRITICAL"

#detect ram problem
if ram_severity == "HIGH":
    ram_problem="high ram usage"
elif ram_severity == "CRITICAL":
    ram_problem="critical ram usage"
else:
    ram_problem="no ram problem"


#storage
storage=psutil.disk_usage("C:\\")
print(f"storage usage:{storage.percent}%")
if storage.percent <= 70:
    storage_severity="NORMAL"
elif storage.percent > 70 and storage.percent <85:
    storage_severity="ELEVATED"
elif storage.percent >= 85 and storage.percent < 95:
    storage_severity="HIGH"
elif storage.percent >= 95:
    storage_severity="CRITICAL"

#detect storage problem
if storage_severity == "HIGH":
    storage_problem="high storage usage"
elif storage_severity == "CRITICAL":
    storage_problem="critical storage usage"
else:
    storage_problem="no storage problem"




problems=[]
if cpu_severity == "HIGH" or cpu_severity=="CRITICAL":
    problems.append(cpu_problem)
if ram_severity == "HIGH" or ram_severity=="CRITICAL":
    problems.append(ram_problem)
if storage_severity == "HIGH" or storage_severity=="CRITICAL":
    problems.append(storage_problem)

print("problems:",problems)  

#overall status
if len(problems)==0:
    overall_status="no problem"
else:
    overall_status="ACTION REQUIRED !"

highest_ramm=0
highest_cpu=0
realcpu_count=0
highest_cpu_process = "No process detected"
highest_ram_process = "No process detected"
cpuid=0
rammid=0

#tell about the application

for process in psutil.process_iter():
    
    realcpu=process.cpu_percent(0.1)
    if realcpu >= 80 :
        realcpu_count += 1
        # if realcpu_count >= 3 :
        #     print("CPU usage consistently high")

    ramm=process.memory_info()
    if process.name()=="System Idle Process":
        continue
    if realcpu > highest_cpu:
        cpuid=process.pid
        highest_cpu = realcpu
        highest_cpu_process=process.name()

    if ramm.rss > highest_ramm :
        rammid=process.pid
        highest_ramm=ramm.rss
        highest_ram_process=process.name()

highest_ramm=highest_ramm//(1024*1024)
print(f"\nhighest_cpu_process is happend due to: {highest_cpu_process.upper()} and it is about {highest_cpu}\n\nhighest_ram_process is happend due to: {highest_ram_process.upper()} and it is about {highest_ramm}\n")



  
system_data={
    "OVERALL_STATUS":overall_status,
    "cpu_application_name":highest_cpu_process,
    "cpu_application_id":cpuid,
    "Highest_app_cpu%":highest_cpu,
    "highest_cpu_process_count":realcpu_count,
    "cpu_severity":cpu_severity,
    "cpu_usage":cpu,
    "cpu_problem":cpu_problem,
    "highest ram application":highest_ram_process,
    "ram_application_id":rammid,
    "highest ram":highest_ramm,
    "ram_severity":ram_severity,
    "ram_usage":ram.percent,
    "ram_problem":ram_problem,
    "storage_severity":storage_severity,
    "storage_usage":storage.percent,
    "storage_problem":storage_problem
}


instructions="""
-You are a laptop health assistant.
-You receive structured laptop information from Python.
-Check OVERALL_STATUS first.
-If OVERALL_STATUS is "no problem", output only NO_ALERT.
-If OVERALL_STATUS requires action:
-Identify the affected resource: CPU, RAM, or storage.
-Identify the relevant application if one is provided.
-Consider the severity.
-Explain the problem briefly in simple language.
-Recommend one safe action.
-The severity fields are authoritative.
-Only report CPU as a problem when cpu_severity is HIGH or CRITICAL.
-Only report RAM as a problem when ram_severity is HIGH or CRITICAL.
-Only report storage as a problem when storage_severity is HIGH or CRITICAL.
-If cpu_severity is NORMAL, do not generate a CPU alert even if a process has a high CPU value.
-Never recommend restarting, stopping, killing, or modifying Windows system processes.
-Only recommend actions explicitly allowed by the application.
-Ask the user for permission before any action.
-Never claim a problem that is not present in the provided data.
-Never claim that a virus or malware was detected unless the data explicitly says so.
-Never execute commands or actions yourself.
-Never invent system information, application names, or results.
-Do not give multiple troubleshooting steps unless specifically asked.
-Keep the response voice-friendly and concise.
-Maximum 1–2 sentences for an alert.
-Use cpu_problem as the final authority for whether CPU has a problem.
-Use ram_problem as the final authority for whether RAM has a problem.
-Use storage_problem as the final authority for whether storage has a problem.
-If cpu_problem is "no cpu problem", do not mention CPU as a problem or recommend any CPU-related action.
-Do not use Highest_app_cpu% alone to decide whether CPU needs attention.
-Do not use headings, bullet points, email format, or long explanations.
-If an application is identified as consuming high CPU/RAM, mention its name when relevant.
-For an action such as closing an application, ask for confirmation first.
-RAM_USAGE is the total percentage of RAM currently used by the whole system.
-HIGHEST_RAM is the memory used by the application/process identified as HIGHEST_RAM_APPLICATION, measured in MB.
-Never treat HIGHEST_RAM as a percentage.
-Never say that an application is using the total system RAM percentage unless the data explicitly says so.
"""


system_data_text=str(system_data)
print(system_data_text)

prompt= instructions + system_data_text

url="http://localhost:11434/api/generate"
info={
    "model":"gemma3",
    "prompt":prompt,
    "stream":False
}
response=requests.post(
    url,
    json = info
)
data=response.json()
print(data["response"])

######voice
engine=pyttsx3.init()
engine.say(data["response"])#add the text to speech queue
engine.runAndWait()#process the queue and speaks it
voices=engine.getProperty("voices")
for voice in voices:
    print("voice name :",voice.name)
    print("voice language :",voice.languages)
    print()


allowed_apps= [
"Chrome.exe",
"msedge.exe",
"Notepad.exe",
"Code.exe",
"llama-server.exe"
"msmpeng.exe",
"msedgewebview2.exe"
]

while True:
    if overall_status == "ACTION REQUIRED !":
        user_input=input("\nTell me your choice:\n")
        if user_input not in [ "YES","Yes","yes" , "NO","No","no", "y" , "n"]:
            print("\n please tell me clearly , YES or NO")
            continue
        elif user_input.lower() == "yes" or user_input.lower()=="y":
            if highest_ram_process in allowed_apps:
                if psutil.pid_exists(rammid):
                    process=psutil.Process(rammid)
                    print("safe to proceed")
                    process.terminate()
                    print(f"{process} closed successfully.")
                    break
                else:
                    print("process no longer exists !")
            else:
                print("not allowed")
                break
        else:
            print("ok ")
            break
            
