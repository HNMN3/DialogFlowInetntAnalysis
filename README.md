# DialogFlowAgentAnalysis
## Requirements:
- Python3
- A machine(virtual or physical) with Ubuntu 16 or higher.
---

## Steps to deploy the code:

* Login to the instance
* Clone the repo on instance using following command:
> git clone https://github.com/HNMN3/DialogFlowIntentAnalysis.git
* cd into the directory DialogFlowIntentAnalysis
* Add execute rights to setup.sh file using following command:
> chmod +x setup.sh
* Run the setup.sh file
> ./setup.sh
* Provide the required details in the env variable using following command:
	(this step needs to be performed again if you logout from machine)
> export PROJECT_ID="project_id_here"

> export GOOGLE_APPLICATION_CREDENTIALS="path_to_credential_file_here"
* Make sure that the input is given in the file named "input.csv"
* Run the program using following command
> python3 main.py
	 