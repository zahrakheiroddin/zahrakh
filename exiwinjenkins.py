import subprocess

def is_jenkins_installed():
    try:
        # Check if Jenkins service exists and is running
        result = subprocess.run(["sc", "query", "jenkins"], capture_output=True, text=True)
        output = result.stdout.lower()

        if "state" in output and ("running" in output or "stopped" in output):
            print("✅ Jenkins service is installed.")
            if "running" in output:
                print("🔄 Jenkins service is currently running.")
            else:
                print("⏹️ Jenkins service is installed but not running.")
            return True
        else:
            print("❌ Jenkins service not found.")
    except Exception as e:
        print("⚠️ Error checking Jenkins service:", e)

    print("❌ Jenkins does not appear to be installed.")
    return False

# Run the check
is_jenkins_installed()
