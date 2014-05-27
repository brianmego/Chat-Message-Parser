'''Setup file to run when initially creating your environment'''
import subprocess

subprocess.call(["pip", "install", "-r", "requirements.txt"])
