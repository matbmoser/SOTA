# Set log levels
LOGLEVELS = {"NONE": 0, "CRITICAL": 1, "EXCEPTION": 2,
             "ERROR": 3, "WARNING": 4, "INFO": 5, "STATS": 6, "DEBUG": 7}
LOGLEVEL = LOGLEVELS["DEBUG"]

# Clas that defines operations


class op:

    # Method to set value empty by default
    @staticmethod
    def valueEmpty(obj):
        return "" if obj == None or obj == "" else obj

    # Method to set value none by default
    @staticmethod
    def valueNone(obj):
        return None if obj == None or obj == "" else obj

    # Print log Operation
    @staticmethod
    def printLog(messageStr, logType="DEBUG", e=None):
        global LOGLEVEL, LOGLEVELS
        # If the log level requested is lower than the actual log level
        if LOGLEVEL < LOGLEVELS[logType]:
            return None

        # Add the log description and exception if not empty
        logInfo = "["+logType+"]:"
        if(e != None):
            logInfo += "[" + str(e) + "]."

        # Print the log

        return print(" ".join([logInfo, messageStr]))

    # Init dinamically the new class
    @staticmethod
    def createClass(newClass, *args, **kwargs):
        # Get slices
        slices = newClass.split('.')

        # Count the number of slices
        lenSlices = len(slices)

        # Check if the number of slices
        if lenSlices == 1:
            slices.append(slices[0])

        # Import Class
        importedClass = __import__(".".join(slices[:-1]))

        # For every component add attributes
        for component in slices[1:]:
            importedClass = getattr(importedClass, component)

        # Create the class
        return importedClass(*args, **kwargs)
