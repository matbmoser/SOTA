# coding=UTF-8
import os,sys,traceback
currentFile=os.path.abspath(__file__)
baseFilename=os.path.basename(currentFile)
currentDir=os.path.dirname(currentFile)
toolsPath=os.path.abspath(os.path.join(currentDir, "../..", "tools"))
sys.path.append(toolsPath)
import envTools, logTools, fileTools, smtpTools, generationTools, jsonTools, op
tmpEnv=envTools.env()
tmpEnv.setEnvironment(processFile=currentFile)
import json
import fileinput
import subprocess

OBJECTIVES = list()
OUTPUT = json.loads('{"results": []}')

def checkResults(test):
  global OBJECTIVES,RESULTS
  localDirectory = os.getcwd()
  path = localDirectory+"/"+test
  resultsFile = open(path+"/results/TESTSERVERperformance.log", "r")
  last_line = resultsFile.readlines()[-1]
  resultsFile.close()
  try:
    parsedLine = json.loads(last_line.rstrip())
    processed = int(parsedLine["messagesprocessed"])
    objetive = int(OBJECTIVES[test])
    text = {"test": test, "objetive": objetive, "processed": processed}
    if(objetive <= processed):
      print("TEST "+test+" [PASSED]")
      text["status"] = "PASSED"
    else:
      print("TEST "+test+" [FAILED]")
      text["status"] = "FAILED"
    OUTPUT["results"].append(text)
  except Exception as e:
    logTools.printLog(logType="EXCEPTION", e=e, messageStr="checkResults: There was a parsing problem")
    traceback.print_exc()

if __name__ == "__main__":
  objectivesFile = "testObjectives.json"
  outputFile = "testResults.json"
  # Opening JSON file
  f = open(objectivesFile)
  
  # returns JSON object as
  # a dictionary
  OBJECTIVES = json.load(f)
  
  f.close()
  
  print("Starting calculation of test results...")
  
  for dir in os.listdir():
    if "PT" in dir:
      checkResults(dir)
      
  print("Finishing calculation of test results...")
  print("Storing results in ["+outputFile+"] file...")
  
  with open(outputFile, 'w') as outfile:
    json.dump(OUTPUT, outfile, indent=2, sort_keys=True)
  
  print("Results stored in ["+outputFile+"] file...")  
  input("Press any key to finish...")